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
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
goog.exportSymbol('proto.dlkit.proto.osid.Osid', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidAggregateableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidAggregateableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidAggregateableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidAggregateableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidBrowsableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidBrowsableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidBrowsableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidBrowsableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCapsule', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCapsuleForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCapsuleQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCapsuleQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCapsuleSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCatalog', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCatalogForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCatalogQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCatalogQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCatalogSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCompendium', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCompendiumForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCompendiumQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCompendiumQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCompendiumSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidCondition', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidConstrainer', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidConstrainerForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidConstrainerQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidConstrainerQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidConstrainerSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidContainableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidContainableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidContainableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidContainableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidEnabler', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidEnablerForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidEnablerQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidEnablerQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidEnablerSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidExtensibleForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidExtensibleQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidExtensibleQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidExtensibleSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidFederateableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidFederateableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidFederateableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidFederateableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidGovernator', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidGovernatorForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidGovernatorQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidGovernatorQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidGovernatorSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidIdentifiableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidIdentifiableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidIdentifiableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidIdentifiableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidInput', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidList', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidNode', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidObject', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidObjectForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidObjectQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidObjectQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidObjectSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidOperableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidOperableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidOperableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidOperableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidProcessor', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidProcessorForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidProcessorQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidProcessorQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidProcessorSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRelationship', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRelationshipForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRelationshipQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRelationshipQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRelationshipSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidResult', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRule', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRuleForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRuleQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRuleQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidRuleSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSourceableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSourceableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSourceableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSourceableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSubjugateableForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSubjugateableQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSubjugateableQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidSubjugateableSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidTemporalForm', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidTemporalQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidTemporalQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.osid.OsidTemporalSearchOrder', null, global);

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.osid.OsidCondition = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCondition, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCondition.displayName = 'proto.dlkit.proto.osid.OsidCondition';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCondition.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCondition.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCondition} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCondition.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCondition}
 */
proto.dlkit.proto.osid.OsidCondition.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCondition;
  return proto.dlkit.proto.osid.OsidCondition.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCondition} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCondition}
 */
proto.dlkit.proto.osid.OsidCondition.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCondition.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCondition.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCondition} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCondition.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidInput = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidInput, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidInput.displayName = 'proto.dlkit.proto.osid.OsidInput';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidInput.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidInput.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidInput} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidInput.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidInput}
 */
proto.dlkit.proto.osid.OsidInput.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidInput;
  return proto.dlkit.proto.osid.OsidInput.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidInput} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidInput}
 */
proto.dlkit.proto.osid.OsidInput.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidInput.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidInput.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidInput} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidInput.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidResult = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidResult, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidResult.displayName = 'proto.dlkit.proto.osid.OsidResult';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidResult.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidResult.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidResult} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidResult.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidResult}
 */
proto.dlkit.proto.osid.OsidResult.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidResult;
  return proto.dlkit.proto.osid.OsidResult.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidResult} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidResult}
 */
proto.dlkit.proto.osid.OsidResult.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidResult.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidResult.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidResult} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidResult.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidObject = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidObject, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidObject.displayName = 'proto.dlkit.proto.osid.OsidObject';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidObject.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidObject.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidObject} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObject.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidObject}
 */
proto.dlkit.proto.osid.OsidObject.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidObject;
  return proto.dlkit.proto.osid.OsidObject.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidObject} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidObject}
 */
proto.dlkit.proto.osid.OsidObject.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidObject.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidObject.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidObject} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObject.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRelationship = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.osid.OsidRelationship.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRelationship, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRelationship.displayName = 'proto.dlkit.proto.osid.OsidRelationship';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.osid.OsidRelationship.repeatedFields_ = [6];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRelationship.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRelationship} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationship.toObject = function(includeInstance, msg) {
  var f, obj = {
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.osid.OsidRelationship}
 */
proto.dlkit.proto.osid.OsidRelationship.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRelationship;
  return proto.dlkit.proto.osid.OsidRelationship.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRelationship} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRelationship}
 */
proto.dlkit.proto.osid.OsidRelationship.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    case 6:
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
proto.dlkit.proto.osid.OsidRelationship.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRelationship.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRelationship} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationship.serializeBinaryToWriter = function(message, writer) {
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
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      6,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 1;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidRelationship.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidRelationship.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidRelationship.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.osid.OsidRelationship.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.osid.OsidRelationship.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.osid.OsidRelationship.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidRelationship.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.osid.OsidRelationship.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional OsidCatalog no_catalog = 5;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 5));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidRelationship.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.osid.OsidRelationship.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.hasNoCatalog = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 6;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 6));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.osid.OsidRelationship.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 6, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidRelationship.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 6, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.osid.OsidRelationship.prototype.clearRecordTypeIdsList = function() {
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
proto.dlkit.proto.osid.OsidCatalog = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.osid.OsidCatalog.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCatalog, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCatalog.displayName = 'proto.dlkit.proto.osid.OsidCatalog';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.osid.OsidCatalog.repeatedFields_ = [6];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCatalog.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCatalog} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalog.toObject = function(includeInstance, msg) {
  var f, obj = {
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidCatalog.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCatalog;
  return proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCatalog} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    case 6:
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
proto.dlkit.proto.osid.OsidCatalog.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCatalog} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter = function(message, writer) {
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
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      6,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 1;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidCatalog.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidCatalog.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidCatalog.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.osid.OsidCatalog.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.osid.OsidCatalog.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.osid.OsidCatalog.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidCatalog.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.osid.OsidCatalog.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional OsidCatalog no_catalog = 5;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 5));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidCatalog.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.osid.OsidCatalog.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.hasNoCatalog = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 6;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 6));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.osid.OsidCatalog.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 6, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidCatalog.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 6, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.osid.OsidCatalog.prototype.clearRecordTypeIdsList = function() {
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
proto.dlkit.proto.osid.OsidRule = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.osid.OsidRule.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRule, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRule.displayName = 'proto.dlkit.proto.osid.OsidRule';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.osid.OsidRule.repeatedFields_ = [6];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRule.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRule.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRule} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRule.toObject = function(includeInstance, msg) {
  var f, obj = {
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    rule: (f = msg.getRule()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.osid.OsidRule}
 */
proto.dlkit.proto.osid.OsidRule.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRule;
  return proto.dlkit.proto.osid.OsidRule.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRule} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRule}
 */
proto.dlkit.proto.osid.OsidRule.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    case 6:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    case 7:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setRule(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.osid.OsidRule.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRule.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRule} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRule.serializeBinaryToWriter = function(message, writer) {
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
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      6,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getRule();
  if (f != null) {
    writer.writeMessage(
      7,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 1;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidRule.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidRule.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidRule.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRule.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidRule.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidRule.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.osid.OsidRule.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRule.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidRule.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.osid.OsidRule.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.osid.OsidRule.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRule.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidRule.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidRule.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.osid.OsidRule.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRule.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional OsidCatalog no_catalog = 5;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidRule.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 5));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidRule.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.osid.OsidRule.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRule.prototype.hasNoCatalog = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 6;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.osid.OsidRule.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 6));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.osid.OsidRule.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 6, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidRule.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 6, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.osid.OsidRule.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};


/**
 * optional dlkit.primordium.id.primitives.Id rule = 7;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidRule.prototype.getRule = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 7));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidRule.prototype.setRule = function(value) {
  jspb.Message.setWrapperField(this, 7, value);
};


proto.dlkit.proto.osid.OsidRule.prototype.clearRule = function() {
  this.setRule(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidRule.prototype.hasRule = function() {
  return jspb.Message.getField(this, 7) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.osid.OsidEnabler = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidEnabler, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidEnabler.displayName = 'proto.dlkit.proto.osid.OsidEnabler';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidEnabler.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidEnabler} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnabler.toObject = function(includeInstance, msg) {
  var f, obj = {
    cyclicEvent: (f = msg.getCyclicEvent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    demographic: (f = msg.getDemographic()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    event: (f = msg.getEvent()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f),
    schedule: (f = msg.getSchedule()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.osid.OsidEnabler}
 */
proto.dlkit.proto.osid.OsidEnabler.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidEnabler;
  return proto.dlkit.proto.osid.OsidEnabler.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidEnabler} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidEnabler}
 */
proto.dlkit.proto.osid.OsidEnabler.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCyclicEvent(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setDemographic(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setEvent(value);
      break;
    case 4:
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    case 5:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setSchedule(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidEnabler.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidEnabler} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnabler.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCyclicEvent();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getDemographic();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getEvent();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getSchedule();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id cyclic_event = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.getCyclicEvent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidEnabler.prototype.setCyclicEvent = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidEnabler.prototype.clearCyclicEvent = function() {
  this.setCyclicEvent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.hasCyclicEvent = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id demographic = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.getDemographic = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidEnabler.prototype.setDemographic = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.osid.OsidEnabler.prototype.clearDemographic = function() {
  this.setDemographic(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.hasDemographic = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id event = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.getEvent = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidEnabler.prototype.setEvent = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.osid.OsidEnabler.prototype.clearEvent = function() {
  this.setEvent(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.hasEvent = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional OsidCatalog no_catalog = 4;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 4));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidEnabler.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.osid.OsidEnabler.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.hasNoCatalog = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id schedule = 5;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.getSchedule = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 5));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidEnabler.prototype.setSchedule = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.osid.OsidEnabler.prototype.clearSchedule = function() {
  this.setSchedule(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidEnabler.prototype.hasSchedule = function() {
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
proto.dlkit.proto.osid.OsidConstrainer = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidConstrainer, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidConstrainer.displayName = 'proto.dlkit.proto.osid.OsidConstrainer';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidConstrainer.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidConstrainer.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidConstrainer} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainer.toObject = function(includeInstance, msg) {
  var f, obj = {
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.osid.OsidConstrainer}
 */
proto.dlkit.proto.osid.OsidConstrainer.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidConstrainer;
  return proto.dlkit.proto.osid.OsidConstrainer.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidConstrainer} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidConstrainer}
 */
proto.dlkit.proto.osid.OsidConstrainer.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.osid.OsidConstrainer.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidConstrainer.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidConstrainer} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainer.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
    );
  }
};


/**
 * optional OsidCatalog no_catalog = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidConstrainer.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidConstrainer.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidConstrainer.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidConstrainer.prototype.hasNoCatalog = function() {
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
proto.dlkit.proto.osid.OsidProcessor = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidProcessor, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidProcessor.displayName = 'proto.dlkit.proto.osid.OsidProcessor';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidProcessor.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidProcessor.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidProcessor} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessor.toObject = function(includeInstance, msg) {
  var f, obj = {
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.osid.OsidProcessor}
 */
proto.dlkit.proto.osid.OsidProcessor.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidProcessor;
  return proto.dlkit.proto.osid.OsidProcessor.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidProcessor} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidProcessor}
 */
proto.dlkit.proto.osid.OsidProcessor.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.osid.OsidProcessor.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidProcessor.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidProcessor} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessor.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
    );
  }
};


/**
 * optional OsidCatalog no_catalog = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidProcessor.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidProcessor.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidProcessor.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidProcessor.prototype.hasNoCatalog = function() {
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
proto.dlkit.proto.osid.OsidGovernator = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.osid.OsidGovernator.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidGovernator, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidGovernator.displayName = 'proto.dlkit.proto.osid.OsidGovernator';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.osid.OsidGovernator.repeatedFields_ = [6];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidGovernator.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidGovernator} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernator.toObject = function(includeInstance, msg) {
  var f, obj = {
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.osid.OsidGovernator}
 */
proto.dlkit.proto.osid.OsidGovernator.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidGovernator;
  return proto.dlkit.proto.osid.OsidGovernator.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidGovernator} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidGovernator}
 */
proto.dlkit.proto.osid.OsidGovernator.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    case 6:
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
proto.dlkit.proto.osid.OsidGovernator.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidGovernator.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidGovernator} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernator.serializeBinaryToWriter = function(message, writer) {
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
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getRecordTypeIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      6,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 1;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidGovernator.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidGovernator.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidGovernator.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.osid.OsidGovernator.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.osid.OsidGovernator.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.osid.OsidGovernator.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidGovernator.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.osid.OsidGovernator.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional OsidCatalog no_catalog = 5;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 5));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidGovernator.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.osid.OsidGovernator.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.hasNoCatalog = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 6;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 6));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.osid.OsidGovernator.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 6, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidGovernator.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 6, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.osid.OsidGovernator.prototype.clearRecordTypeIdsList = function() {
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
proto.dlkit.proto.osid.OsidCompendium = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.osid.OsidCompendium.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCompendium, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCompendium.displayName = 'proto.dlkit.proto.osid.OsidCompendium';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.osid.OsidCompendium.repeatedFields_ = [9];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCompendium.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCompendium} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendium.toObject = function(includeInstance, msg) {
  var f, obj = {
    description: (f = msg.getDescription()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    displayName: (f = msg.getDisplayName()) && dlkit_primordium_locale_primitives_pb.DisplayText.toObject(includeInstance, f),
    endDate: (f = msg.getEndDate()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    extrapolated: jspb.Message.getFieldWithDefault(msg, 4, false),
    genusTypeId: (f = msg.getGenusTypeId()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    id: (f = msg.getId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    interpolated: jspb.Message.getFieldWithDefault(msg, 7, false),
    noCatalog: (f = msg.getNoCatalog()) && proto.dlkit.proto.osid.OsidCatalog.toObject(includeInstance, f),
    recordTypeIdsList: jspb.Message.toObjectList(msg.getRecordTypeIdsList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    startDate: (f = msg.getStartDate()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.osid.OsidCompendium}
 */
proto.dlkit.proto.osid.OsidCompendium.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCompendium;
  return proto.dlkit.proto.osid.OsidCompendium.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCompendium} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCompendium}
 */
proto.dlkit.proto.osid.OsidCompendium.deserializeBinaryFromReader = function(msg, reader) {
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
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setEndDate(value);
      break;
    case 4:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setExtrapolated(value);
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
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setInterpolated(value);
      break;
    case 8:
      var value = new proto.dlkit.proto.osid.OsidCatalog;
      reader.readMessage(value,proto.dlkit.proto.osid.OsidCatalog.deserializeBinaryFromReader);
      msg.setNoCatalog(value);
      break;
    case 9:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addRecordTypeIds(value);
      break;
    case 10:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setStartDate(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCompendium.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCompendium} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendium.serializeBinaryToWriter = function(message, writer) {
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
  f = message.getEndDate();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getExtrapolated();
  if (f) {
    writer.writeBool(
      4,
      f
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
  f = message.getInterpolated();
  if (f) {
    writer.writeBool(
      7,
      f
    );
  }
  f = message.getNoCatalog();
  if (f != null) {
    writer.writeMessage(
      8,
      f,
      proto.dlkit.proto.osid.OsidCatalog.serializeBinaryToWriter
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
  f = message.getStartDate();
  if (f != null) {
    writer.writeMessage(
      10,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText description = 1;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp end_date = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getEndDate = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setEndDate = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearEndDate = function() {
  this.setEndDate(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.hasEndDate = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional bool extrapolated = 4;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getExtrapolated = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 4, false));
};


/** @param {boolean} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setExtrapolated = function(value) {
  jspb.Message.setProto3BooleanField(this, 4, value);
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 5;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 5));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 6;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 6));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 6, value);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.hasId = function() {
  return jspb.Message.getField(this, 6) != null;
};


/**
 * optional bool interpolated = 7;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getInterpolated = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 7, false));
};


/** @param {boolean} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setInterpolated = function(value) {
  jspb.Message.setProto3BooleanField(this, 7, value);
};


/**
 * optional OsidCatalog no_catalog = 8;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getNoCatalog = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.osid.OsidCatalog, 8));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setNoCatalog = function(value) {
  jspb.Message.setWrapperField(this, 8, value);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearNoCatalog = function() {
  this.setNoCatalog(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.hasNoCatalog = function() {
  return jspb.Message.getField(this, 8) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 9;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 9));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 9, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 9, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearRecordTypeIdsList = function() {
  this.setRecordTypeIdsList([]);
};


/**
 * optional google.protobuf.Timestamp start_date = 10;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.getStartDate = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 10));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.osid.OsidCompendium.prototype.setStartDate = function(value) {
  jspb.Message.setWrapperField(this, 10, value);
};


proto.dlkit.proto.osid.OsidCompendium.prototype.clearStartDate = function() {
  this.setStartDate(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.osid.OsidCompendium.prototype.hasStartDate = function() {
  return jspb.Message.getField(this, 10) != null;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.osid.OsidCapsule = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCapsule, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCapsule.displayName = 'proto.dlkit.proto.osid.OsidCapsule';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCapsule.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCapsule.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCapsule} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsule.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCapsule}
 */
proto.dlkit.proto.osid.OsidCapsule.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCapsule;
  return proto.dlkit.proto.osid.OsidCapsule.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCapsule} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCapsule}
 */
proto.dlkit.proto.osid.OsidCapsule.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCapsule.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCapsule.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCapsule} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsule.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidQuery.displayName = 'proto.dlkit.proto.osid.OsidQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidQuery}
 */
proto.dlkit.proto.osid.OsidQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidQuery;
  return proto.dlkit.proto.osid.OsidQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidQuery}
 */
proto.dlkit.proto.osid.OsidQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidIdentifiableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidIdentifiableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidIdentifiableQuery.displayName = 'proto.dlkit.proto.osid.OsidIdentifiableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidIdentifiableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidIdentifiableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableQuery}
 */
proto.dlkit.proto.osid.OsidIdentifiableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidIdentifiableQuery;
  return proto.dlkit.proto.osid.OsidIdentifiableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableQuery}
 */
proto.dlkit.proto.osid.OsidIdentifiableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidIdentifiableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidIdentifiableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidExtensibleQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidExtensibleQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidExtensibleQuery.displayName = 'proto.dlkit.proto.osid.OsidExtensibleQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidExtensibleQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidExtensibleQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidExtensibleQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidExtensibleQuery}
 */
proto.dlkit.proto.osid.OsidExtensibleQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidExtensibleQuery;
  return proto.dlkit.proto.osid.OsidExtensibleQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidExtensibleQuery}
 */
proto.dlkit.proto.osid.OsidExtensibleQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidExtensibleQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidExtensibleQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidBrowsableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidBrowsableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidBrowsableQuery.displayName = 'proto.dlkit.proto.osid.OsidBrowsableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidBrowsableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidBrowsableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidBrowsableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidBrowsableQuery}
 */
proto.dlkit.proto.osid.OsidBrowsableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidBrowsableQuery;
  return proto.dlkit.proto.osid.OsidBrowsableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidBrowsableQuery}
 */
proto.dlkit.proto.osid.OsidBrowsableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidBrowsableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidBrowsableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidTemporalQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidTemporalQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidTemporalQuery.displayName = 'proto.dlkit.proto.osid.OsidTemporalQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidTemporalQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidTemporalQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidTemporalQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidTemporalQuery}
 */
proto.dlkit.proto.osid.OsidTemporalQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidTemporalQuery;
  return proto.dlkit.proto.osid.OsidTemporalQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidTemporalQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidTemporalQuery}
 */
proto.dlkit.proto.osid.OsidTemporalQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidTemporalQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidTemporalQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidTemporalQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSubjugateableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSubjugateableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSubjugateableQuery.displayName = 'proto.dlkit.proto.osid.OsidSubjugateableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSubjugateableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSubjugateableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableQuery}
 */
proto.dlkit.proto.osid.OsidSubjugateableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSubjugateableQuery;
  return proto.dlkit.proto.osid.OsidSubjugateableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableQuery}
 */
proto.dlkit.proto.osid.OsidSubjugateableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSubjugateableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSubjugateableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidAggregateableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidAggregateableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidAggregateableQuery.displayName = 'proto.dlkit.proto.osid.OsidAggregateableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidAggregateableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidAggregateableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidAggregateableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidAggregateableQuery}
 */
proto.dlkit.proto.osid.OsidAggregateableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidAggregateableQuery;
  return proto.dlkit.proto.osid.OsidAggregateableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidAggregateableQuery}
 */
proto.dlkit.proto.osid.OsidAggregateableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidAggregateableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidAggregateableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidContainableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidContainableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidContainableQuery.displayName = 'proto.dlkit.proto.osid.OsidContainableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidContainableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidContainableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidContainableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidContainableQuery}
 */
proto.dlkit.proto.osid.OsidContainableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidContainableQuery;
  return proto.dlkit.proto.osid.OsidContainableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidContainableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidContainableQuery}
 */
proto.dlkit.proto.osid.OsidContainableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidContainableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidContainableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidContainableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSourceableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSourceableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSourceableQuery.displayName = 'proto.dlkit.proto.osid.OsidSourceableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSourceableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSourceableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSourceableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSourceableQuery}
 */
proto.dlkit.proto.osid.OsidSourceableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSourceableQuery;
  return proto.dlkit.proto.osid.OsidSourceableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSourceableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSourceableQuery}
 */
proto.dlkit.proto.osid.OsidSourceableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSourceableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSourceableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSourceableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidFederateableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidFederateableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidFederateableQuery.displayName = 'proto.dlkit.proto.osid.OsidFederateableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidFederateableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidFederateableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidFederateableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidFederateableQuery}
 */
proto.dlkit.proto.osid.OsidFederateableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidFederateableQuery;
  return proto.dlkit.proto.osid.OsidFederateableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidFederateableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidFederateableQuery}
 */
proto.dlkit.proto.osid.OsidFederateableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidFederateableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidFederateableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidFederateableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidOperableQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidOperableQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidOperableQuery.displayName = 'proto.dlkit.proto.osid.OsidOperableQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidOperableQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidOperableQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidOperableQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidOperableQuery}
 */
proto.dlkit.proto.osid.OsidOperableQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidOperableQuery;
  return proto.dlkit.proto.osid.OsidOperableQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidOperableQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidOperableQuery}
 */
proto.dlkit.proto.osid.OsidOperableQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidOperableQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidOperableQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidOperableQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidObjectQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidObjectQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidObjectQuery.displayName = 'proto.dlkit.proto.osid.OsidObjectQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidObjectQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidObjectQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidObjectQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidObjectQuery}
 */
proto.dlkit.proto.osid.OsidObjectQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidObjectQuery;
  return proto.dlkit.proto.osid.OsidObjectQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidObjectQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidObjectQuery}
 */
proto.dlkit.proto.osid.OsidObjectQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidObjectQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidObjectQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidObjectQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRelationshipQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRelationshipQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRelationshipQuery.displayName = 'proto.dlkit.proto.osid.OsidRelationshipQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRelationshipQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRelationshipQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRelationshipQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRelationshipQuery}
 */
proto.dlkit.proto.osid.OsidRelationshipQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRelationshipQuery;
  return proto.dlkit.proto.osid.OsidRelationshipQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRelationshipQuery}
 */
proto.dlkit.proto.osid.OsidRelationshipQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRelationshipQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRelationshipQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCatalogQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCatalogQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCatalogQuery.displayName = 'proto.dlkit.proto.osid.OsidCatalogQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCatalogQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCatalogQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCatalogQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCatalogQuery}
 */
proto.dlkit.proto.osid.OsidCatalogQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCatalogQuery;
  return proto.dlkit.proto.osid.OsidCatalogQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCatalogQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCatalogQuery}
 */
proto.dlkit.proto.osid.OsidCatalogQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCatalogQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCatalogQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCatalogQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRuleQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRuleQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRuleQuery.displayName = 'proto.dlkit.proto.osid.OsidRuleQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRuleQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRuleQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRuleQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRuleQuery}
 */
proto.dlkit.proto.osid.OsidRuleQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRuleQuery;
  return proto.dlkit.proto.osid.OsidRuleQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRuleQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRuleQuery}
 */
proto.dlkit.proto.osid.OsidRuleQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRuleQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRuleQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRuleQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidEnablerQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidEnablerQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidEnablerQuery.displayName = 'proto.dlkit.proto.osid.OsidEnablerQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidEnablerQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidEnablerQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidEnablerQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidEnablerQuery}
 */
proto.dlkit.proto.osid.OsidEnablerQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidEnablerQuery;
  return proto.dlkit.proto.osid.OsidEnablerQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidEnablerQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidEnablerQuery}
 */
proto.dlkit.proto.osid.OsidEnablerQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidEnablerQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidEnablerQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidEnablerQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidConstrainerQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidConstrainerQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidConstrainerQuery.displayName = 'proto.dlkit.proto.osid.OsidConstrainerQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidConstrainerQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidConstrainerQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidConstrainerQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidConstrainerQuery}
 */
proto.dlkit.proto.osid.OsidConstrainerQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidConstrainerQuery;
  return proto.dlkit.proto.osid.OsidConstrainerQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidConstrainerQuery}
 */
proto.dlkit.proto.osid.OsidConstrainerQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidConstrainerQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidConstrainerQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidProcessorQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidProcessorQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidProcessorQuery.displayName = 'proto.dlkit.proto.osid.OsidProcessorQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidProcessorQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidProcessorQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidProcessorQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidProcessorQuery}
 */
proto.dlkit.proto.osid.OsidProcessorQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidProcessorQuery;
  return proto.dlkit.proto.osid.OsidProcessorQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidProcessorQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidProcessorQuery}
 */
proto.dlkit.proto.osid.OsidProcessorQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidProcessorQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidProcessorQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidProcessorQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidGovernatorQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidGovernatorQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidGovernatorQuery.displayName = 'proto.dlkit.proto.osid.OsidGovernatorQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidGovernatorQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidGovernatorQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidGovernatorQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidGovernatorQuery}
 */
proto.dlkit.proto.osid.OsidGovernatorQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidGovernatorQuery;
  return proto.dlkit.proto.osid.OsidGovernatorQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidGovernatorQuery}
 */
proto.dlkit.proto.osid.OsidGovernatorQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidGovernatorQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidGovernatorQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCompendiumQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCompendiumQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCompendiumQuery.displayName = 'proto.dlkit.proto.osid.OsidCompendiumQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCompendiumQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCompendiumQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCompendiumQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCompendiumQuery}
 */
proto.dlkit.proto.osid.OsidCompendiumQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCompendiumQuery;
  return proto.dlkit.proto.osid.OsidCompendiumQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCompendiumQuery}
 */
proto.dlkit.proto.osid.OsidCompendiumQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCompendiumQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCompendiumQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCapsuleQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCapsuleQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCapsuleQuery.displayName = 'proto.dlkit.proto.osid.OsidCapsuleQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCapsuleQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCapsuleQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCapsuleQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleQuery.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCapsuleQuery}
 */
proto.dlkit.proto.osid.OsidCapsuleQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCapsuleQuery;
  return proto.dlkit.proto.osid.OsidCapsuleQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCapsuleQuery}
 */
proto.dlkit.proto.osid.OsidCapsuleQuery.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCapsuleQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCapsuleQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleQuery.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidQueryInspector}
 */
proto.dlkit.proto.osid.OsidQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidQueryInspector;
  return proto.dlkit.proto.osid.OsidQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidQueryInspector}
 */
proto.dlkit.proto.osid.OsidQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidIdentifiableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidIdentifiableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidIdentifiableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableQueryInspector}
 */
proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidIdentifiableQueryInspector;
  return proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableQueryInspector}
 */
proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidExtensibleQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidExtensibleQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidExtensibleQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidExtensibleQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidExtensibleQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidExtensibleQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidExtensibleQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidExtensibleQueryInspector}
 */
proto.dlkit.proto.osid.OsidExtensibleQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidExtensibleQueryInspector;
  return proto.dlkit.proto.osid.OsidExtensibleQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidExtensibleQueryInspector}
 */
proto.dlkit.proto.osid.OsidExtensibleQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidExtensibleQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidExtensibleQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidBrowsableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidBrowsableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidBrowsableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidBrowsableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidBrowsableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidBrowsableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidBrowsableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidBrowsableQueryInspector}
 */
proto.dlkit.proto.osid.OsidBrowsableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidBrowsableQueryInspector;
  return proto.dlkit.proto.osid.OsidBrowsableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidBrowsableQueryInspector}
 */
proto.dlkit.proto.osid.OsidBrowsableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidBrowsableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidBrowsableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidTemporalQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidTemporalQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidTemporalQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidTemporalQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidTemporalQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidTemporalQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidTemporalQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidTemporalQueryInspector}
 */
proto.dlkit.proto.osid.OsidTemporalQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidTemporalQueryInspector;
  return proto.dlkit.proto.osid.OsidTemporalQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidTemporalQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidTemporalQueryInspector}
 */
proto.dlkit.proto.osid.OsidTemporalQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidTemporalQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidTemporalQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidTemporalQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSubjugateableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSubjugateableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidSubjugateableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableQueryInspector}
 */
proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSubjugateableQueryInspector;
  return proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableQueryInspector}
 */
proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidAggregateableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidAggregateableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidAggregateableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidAggregateableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidAggregateableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidAggregateableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidAggregateableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidAggregateableQueryInspector}
 */
proto.dlkit.proto.osid.OsidAggregateableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidAggregateableQueryInspector;
  return proto.dlkit.proto.osid.OsidAggregateableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidAggregateableQueryInspector}
 */
proto.dlkit.proto.osid.OsidAggregateableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidAggregateableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidAggregateableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidContainableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidContainableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidContainableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidContainableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidContainableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidContainableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidContainableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidContainableQueryInspector}
 */
proto.dlkit.proto.osid.OsidContainableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidContainableQueryInspector;
  return proto.dlkit.proto.osid.OsidContainableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidContainableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidContainableQueryInspector}
 */
proto.dlkit.proto.osid.OsidContainableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidContainableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidContainableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidContainableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSourceableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSourceableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSourceableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidSourceableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSourceableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSourceableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSourceableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSourceableQueryInspector}
 */
proto.dlkit.proto.osid.OsidSourceableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSourceableQueryInspector;
  return proto.dlkit.proto.osid.OsidSourceableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSourceableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSourceableQueryInspector}
 */
proto.dlkit.proto.osid.OsidSourceableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSourceableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSourceableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSourceableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidFederateableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidFederateableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidFederateableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidFederateableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidFederateableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidFederateableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidFederateableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidFederateableQueryInspector}
 */
proto.dlkit.proto.osid.OsidFederateableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidFederateableQueryInspector;
  return proto.dlkit.proto.osid.OsidFederateableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidFederateableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidFederateableQueryInspector}
 */
proto.dlkit.proto.osid.OsidFederateableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidFederateableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidFederateableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidFederateableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidOperableQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidOperableQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidOperableQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidOperableQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidOperableQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidOperableQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidOperableQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidOperableQueryInspector}
 */
proto.dlkit.proto.osid.OsidOperableQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidOperableQueryInspector;
  return proto.dlkit.proto.osid.OsidOperableQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidOperableQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidOperableQueryInspector}
 */
proto.dlkit.proto.osid.OsidOperableQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidOperableQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidOperableQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidOperableQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidObjectQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidObjectQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidObjectQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidObjectQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidObjectQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidObjectQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidObjectQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidObjectQueryInspector}
 */
proto.dlkit.proto.osid.OsidObjectQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidObjectQueryInspector;
  return proto.dlkit.proto.osid.OsidObjectQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidObjectQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidObjectQueryInspector}
 */
proto.dlkit.proto.osid.OsidObjectQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidObjectQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidObjectQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidObjectQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRelationshipQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRelationshipQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRelationshipQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidRelationshipQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRelationshipQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRelationshipQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRelationshipQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRelationshipQueryInspector}
 */
proto.dlkit.proto.osid.OsidRelationshipQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRelationshipQueryInspector;
  return proto.dlkit.proto.osid.OsidRelationshipQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRelationshipQueryInspector}
 */
proto.dlkit.proto.osid.OsidRelationshipQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRelationshipQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRelationshipQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCatalogQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCatalogQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCatalogQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidCatalogQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCatalogQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCatalogQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCatalogQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCatalogQueryInspector}
 */
proto.dlkit.proto.osid.OsidCatalogQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCatalogQueryInspector;
  return proto.dlkit.proto.osid.OsidCatalogQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCatalogQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCatalogQueryInspector}
 */
proto.dlkit.proto.osid.OsidCatalogQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCatalogQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCatalogQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCatalogQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRuleQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRuleQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRuleQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidRuleQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRuleQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRuleQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRuleQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRuleQueryInspector}
 */
proto.dlkit.proto.osid.OsidRuleQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRuleQueryInspector;
  return proto.dlkit.proto.osid.OsidRuleQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRuleQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRuleQueryInspector}
 */
proto.dlkit.proto.osid.OsidRuleQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRuleQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRuleQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRuleQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidEnablerQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidEnablerQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidEnablerQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidEnablerQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidEnablerQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidEnablerQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidEnablerQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidEnablerQueryInspector}
 */
proto.dlkit.proto.osid.OsidEnablerQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidEnablerQueryInspector;
  return proto.dlkit.proto.osid.OsidEnablerQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidEnablerQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidEnablerQueryInspector}
 */
proto.dlkit.proto.osid.OsidEnablerQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidEnablerQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidEnablerQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidEnablerQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidConstrainerQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidConstrainerQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidConstrainerQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidConstrainerQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidConstrainerQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidConstrainerQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidConstrainerQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidConstrainerQueryInspector}
 */
proto.dlkit.proto.osid.OsidConstrainerQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidConstrainerQueryInspector;
  return proto.dlkit.proto.osid.OsidConstrainerQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidConstrainerQueryInspector}
 */
proto.dlkit.proto.osid.OsidConstrainerQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidConstrainerQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidConstrainerQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidProcessorQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidProcessorQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidProcessorQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidProcessorQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidProcessorQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidProcessorQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidProcessorQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidProcessorQueryInspector}
 */
proto.dlkit.proto.osid.OsidProcessorQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidProcessorQueryInspector;
  return proto.dlkit.proto.osid.OsidProcessorQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidProcessorQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidProcessorQueryInspector}
 */
proto.dlkit.proto.osid.OsidProcessorQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidProcessorQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidProcessorQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidProcessorQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidGovernatorQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidGovernatorQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidGovernatorQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidGovernatorQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidGovernatorQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidGovernatorQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidGovernatorQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidGovernatorQueryInspector}
 */
proto.dlkit.proto.osid.OsidGovernatorQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidGovernatorQueryInspector;
  return proto.dlkit.proto.osid.OsidGovernatorQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidGovernatorQueryInspector}
 */
proto.dlkit.proto.osid.OsidGovernatorQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidGovernatorQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidGovernatorQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCompendiumQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCompendiumQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCompendiumQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidCompendiumQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCompendiumQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCompendiumQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCompendiumQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCompendiumQueryInspector}
 */
proto.dlkit.proto.osid.OsidCompendiumQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCompendiumQueryInspector;
  return proto.dlkit.proto.osid.OsidCompendiumQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCompendiumQueryInspector}
 */
proto.dlkit.proto.osid.OsidCompendiumQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCompendiumQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCompendiumQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCapsuleQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCapsuleQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCapsuleQueryInspector.displayName = 'proto.dlkit.proto.osid.OsidCapsuleQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCapsuleQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCapsuleQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCapsuleQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleQueryInspector.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCapsuleQueryInspector}
 */
proto.dlkit.proto.osid.OsidCapsuleQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCapsuleQueryInspector;
  return proto.dlkit.proto.osid.OsidCapsuleQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCapsuleQueryInspector}
 */
proto.dlkit.proto.osid.OsidCapsuleQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCapsuleQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCapsuleQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleQueryInspector.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidForm.displayName = 'proto.dlkit.proto.osid.OsidForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidForm}
 */
proto.dlkit.proto.osid.OsidForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidForm;
  return proto.dlkit.proto.osid.OsidForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidForm}
 */
proto.dlkit.proto.osid.OsidForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidIdentifiableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidIdentifiableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidIdentifiableForm.displayName = 'proto.dlkit.proto.osid.OsidIdentifiableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidIdentifiableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidIdentifiableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableForm}
 */
proto.dlkit.proto.osid.OsidIdentifiableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidIdentifiableForm;
  return proto.dlkit.proto.osid.OsidIdentifiableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableForm}
 */
proto.dlkit.proto.osid.OsidIdentifiableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidIdentifiableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidIdentifiableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidExtensibleForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidExtensibleForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidExtensibleForm.displayName = 'proto.dlkit.proto.osid.OsidExtensibleForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidExtensibleForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidExtensibleForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidExtensibleForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidExtensibleForm}
 */
proto.dlkit.proto.osid.OsidExtensibleForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidExtensibleForm;
  return proto.dlkit.proto.osid.OsidExtensibleForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidExtensibleForm}
 */
proto.dlkit.proto.osid.OsidExtensibleForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidExtensibleForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidExtensibleForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidBrowsableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidBrowsableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidBrowsableForm.displayName = 'proto.dlkit.proto.osid.OsidBrowsableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidBrowsableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidBrowsableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidBrowsableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidBrowsableForm}
 */
proto.dlkit.proto.osid.OsidBrowsableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidBrowsableForm;
  return proto.dlkit.proto.osid.OsidBrowsableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidBrowsableForm}
 */
proto.dlkit.proto.osid.OsidBrowsableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidBrowsableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidBrowsableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidTemporalForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidTemporalForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidTemporalForm.displayName = 'proto.dlkit.proto.osid.OsidTemporalForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidTemporalForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidTemporalForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidTemporalForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidTemporalForm}
 */
proto.dlkit.proto.osid.OsidTemporalForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidTemporalForm;
  return proto.dlkit.proto.osid.OsidTemporalForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidTemporalForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidTemporalForm}
 */
proto.dlkit.proto.osid.OsidTemporalForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidTemporalForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidTemporalForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidTemporalForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSubjugateableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSubjugateableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSubjugateableForm.displayName = 'proto.dlkit.proto.osid.OsidSubjugateableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSubjugateableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSubjugateableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableForm}
 */
proto.dlkit.proto.osid.OsidSubjugateableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSubjugateableForm;
  return proto.dlkit.proto.osid.OsidSubjugateableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableForm}
 */
proto.dlkit.proto.osid.OsidSubjugateableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSubjugateableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSubjugateableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidAggregateableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidAggregateableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidAggregateableForm.displayName = 'proto.dlkit.proto.osid.OsidAggregateableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidAggregateableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidAggregateableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidAggregateableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidAggregateableForm}
 */
proto.dlkit.proto.osid.OsidAggregateableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidAggregateableForm;
  return proto.dlkit.proto.osid.OsidAggregateableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidAggregateableForm}
 */
proto.dlkit.proto.osid.OsidAggregateableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidAggregateableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidAggregateableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidContainableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidContainableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidContainableForm.displayName = 'proto.dlkit.proto.osid.OsidContainableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidContainableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidContainableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidContainableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidContainableForm}
 */
proto.dlkit.proto.osid.OsidContainableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidContainableForm;
  return proto.dlkit.proto.osid.OsidContainableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidContainableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidContainableForm}
 */
proto.dlkit.proto.osid.OsidContainableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidContainableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidContainableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidContainableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSourceableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSourceableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSourceableForm.displayName = 'proto.dlkit.proto.osid.OsidSourceableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSourceableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSourceableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSourceableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSourceableForm}
 */
proto.dlkit.proto.osid.OsidSourceableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSourceableForm;
  return proto.dlkit.proto.osid.OsidSourceableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSourceableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSourceableForm}
 */
proto.dlkit.proto.osid.OsidSourceableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSourceableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSourceableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSourceableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidFederateableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidFederateableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidFederateableForm.displayName = 'proto.dlkit.proto.osid.OsidFederateableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidFederateableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidFederateableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidFederateableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidFederateableForm}
 */
proto.dlkit.proto.osid.OsidFederateableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidFederateableForm;
  return proto.dlkit.proto.osid.OsidFederateableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidFederateableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidFederateableForm}
 */
proto.dlkit.proto.osid.OsidFederateableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidFederateableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidFederateableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidFederateableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidOperableForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidOperableForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidOperableForm.displayName = 'proto.dlkit.proto.osid.OsidOperableForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidOperableForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidOperableForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidOperableForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidOperableForm}
 */
proto.dlkit.proto.osid.OsidOperableForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidOperableForm;
  return proto.dlkit.proto.osid.OsidOperableForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidOperableForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidOperableForm}
 */
proto.dlkit.proto.osid.OsidOperableForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidOperableForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidOperableForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidOperableForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidObjectForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidObjectForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidObjectForm.displayName = 'proto.dlkit.proto.osid.OsidObjectForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidObjectForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidObjectForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidObjectForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidObjectForm}
 */
proto.dlkit.proto.osid.OsidObjectForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidObjectForm;
  return proto.dlkit.proto.osid.OsidObjectForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidObjectForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidObjectForm}
 */
proto.dlkit.proto.osid.OsidObjectForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidObjectForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidObjectForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidObjectForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRelationshipForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRelationshipForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRelationshipForm.displayName = 'proto.dlkit.proto.osid.OsidRelationshipForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRelationshipForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRelationshipForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRelationshipForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRelationshipForm}
 */
proto.dlkit.proto.osid.OsidRelationshipForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRelationshipForm;
  return proto.dlkit.proto.osid.OsidRelationshipForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRelationshipForm}
 */
proto.dlkit.proto.osid.OsidRelationshipForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRelationshipForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRelationshipForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCatalogForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCatalogForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCatalogForm.displayName = 'proto.dlkit.proto.osid.OsidCatalogForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCatalogForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCatalogForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCatalogForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCatalogForm}
 */
proto.dlkit.proto.osid.OsidCatalogForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCatalogForm;
  return proto.dlkit.proto.osid.OsidCatalogForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCatalogForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCatalogForm}
 */
proto.dlkit.proto.osid.OsidCatalogForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCatalogForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCatalogForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCatalogForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRuleForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRuleForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRuleForm.displayName = 'proto.dlkit.proto.osid.OsidRuleForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRuleForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRuleForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRuleForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRuleForm}
 */
proto.dlkit.proto.osid.OsidRuleForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRuleForm;
  return proto.dlkit.proto.osid.OsidRuleForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRuleForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRuleForm}
 */
proto.dlkit.proto.osid.OsidRuleForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRuleForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRuleForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRuleForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidEnablerForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidEnablerForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidEnablerForm.displayName = 'proto.dlkit.proto.osid.OsidEnablerForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidEnablerForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidEnablerForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidEnablerForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidEnablerForm}
 */
proto.dlkit.proto.osid.OsidEnablerForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidEnablerForm;
  return proto.dlkit.proto.osid.OsidEnablerForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidEnablerForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidEnablerForm}
 */
proto.dlkit.proto.osid.OsidEnablerForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidEnablerForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidEnablerForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidEnablerForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidConstrainerForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidConstrainerForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidConstrainerForm.displayName = 'proto.dlkit.proto.osid.OsidConstrainerForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidConstrainerForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidConstrainerForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidConstrainerForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidConstrainerForm}
 */
proto.dlkit.proto.osid.OsidConstrainerForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidConstrainerForm;
  return proto.dlkit.proto.osid.OsidConstrainerForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidConstrainerForm}
 */
proto.dlkit.proto.osid.OsidConstrainerForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidConstrainerForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidConstrainerForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidProcessorForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidProcessorForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidProcessorForm.displayName = 'proto.dlkit.proto.osid.OsidProcessorForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidProcessorForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidProcessorForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidProcessorForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidProcessorForm}
 */
proto.dlkit.proto.osid.OsidProcessorForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidProcessorForm;
  return proto.dlkit.proto.osid.OsidProcessorForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidProcessorForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidProcessorForm}
 */
proto.dlkit.proto.osid.OsidProcessorForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidProcessorForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidProcessorForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidProcessorForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidGovernatorForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidGovernatorForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidGovernatorForm.displayName = 'proto.dlkit.proto.osid.OsidGovernatorForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidGovernatorForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidGovernatorForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidGovernatorForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidGovernatorForm}
 */
proto.dlkit.proto.osid.OsidGovernatorForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidGovernatorForm;
  return proto.dlkit.proto.osid.OsidGovernatorForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidGovernatorForm}
 */
proto.dlkit.proto.osid.OsidGovernatorForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidGovernatorForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidGovernatorForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCompendiumForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCompendiumForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCompendiumForm.displayName = 'proto.dlkit.proto.osid.OsidCompendiumForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCompendiumForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCompendiumForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCompendiumForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCompendiumForm}
 */
proto.dlkit.proto.osid.OsidCompendiumForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCompendiumForm;
  return proto.dlkit.proto.osid.OsidCompendiumForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCompendiumForm}
 */
proto.dlkit.proto.osid.OsidCompendiumForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCompendiumForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCompendiumForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCapsuleForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCapsuleForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCapsuleForm.displayName = 'proto.dlkit.proto.osid.OsidCapsuleForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCapsuleForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCapsuleForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCapsuleForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleForm.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCapsuleForm}
 */
proto.dlkit.proto.osid.OsidCapsuleForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCapsuleForm;
  return proto.dlkit.proto.osid.OsidCapsuleForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCapsuleForm}
 */
proto.dlkit.proto.osid.OsidCapsuleForm.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCapsuleForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCapsuleForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleForm.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSearchOrder}
 */
proto.dlkit.proto.osid.OsidSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSearchOrder;
  return proto.dlkit.proto.osid.OsidSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSearchOrder}
 */
proto.dlkit.proto.osid.OsidSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidIdentifiableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidIdentifiableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidIdentifiableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableSearchOrder}
 */
proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidIdentifiableSearchOrder;
  return proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidIdentifiableSearchOrder}
 */
proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidIdentifiableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidIdentifiableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidExtensibleSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidExtensibleSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidExtensibleSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidExtensibleSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidExtensibleSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidExtensibleSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidExtensibleSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidExtensibleSearchOrder}
 */
proto.dlkit.proto.osid.OsidExtensibleSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidExtensibleSearchOrder;
  return proto.dlkit.proto.osid.OsidExtensibleSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidExtensibleSearchOrder}
 */
proto.dlkit.proto.osid.OsidExtensibleSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidExtensibleSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidExtensibleSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidExtensibleSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidExtensibleSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidBrowsableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidBrowsableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidBrowsableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidBrowsableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidBrowsableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidBrowsableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidBrowsableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidBrowsableSearchOrder}
 */
proto.dlkit.proto.osid.OsidBrowsableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidBrowsableSearchOrder;
  return proto.dlkit.proto.osid.OsidBrowsableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidBrowsableSearchOrder}
 */
proto.dlkit.proto.osid.OsidBrowsableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidBrowsableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidBrowsableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidBrowsableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidBrowsableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidTemporalSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidTemporalSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidTemporalSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidTemporalSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidTemporalSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidTemporalSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidTemporalSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidTemporalSearchOrder}
 */
proto.dlkit.proto.osid.OsidTemporalSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidTemporalSearchOrder;
  return proto.dlkit.proto.osid.OsidTemporalSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidTemporalSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidTemporalSearchOrder}
 */
proto.dlkit.proto.osid.OsidTemporalSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidTemporalSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidTemporalSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidTemporalSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidTemporalSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSubjugateableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSubjugateableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidSubjugateableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableSearchOrder}
 */
proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSubjugateableSearchOrder;
  return proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSubjugateableSearchOrder}
 */
proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSubjugateableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSubjugateableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidAggregateableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidAggregateableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidAggregateableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidAggregateableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidAggregateableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidAggregateableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidAggregateableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidAggregateableSearchOrder}
 */
proto.dlkit.proto.osid.OsidAggregateableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidAggregateableSearchOrder;
  return proto.dlkit.proto.osid.OsidAggregateableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidAggregateableSearchOrder}
 */
proto.dlkit.proto.osid.OsidAggregateableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidAggregateableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidAggregateableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidAggregateableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidAggregateableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidContainableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidContainableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidContainableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidContainableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidContainableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidContainableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidContainableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidContainableSearchOrder}
 */
proto.dlkit.proto.osid.OsidContainableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidContainableSearchOrder;
  return proto.dlkit.proto.osid.OsidContainableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidContainableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidContainableSearchOrder}
 */
proto.dlkit.proto.osid.OsidContainableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidContainableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidContainableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidContainableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidContainableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSourceableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSourceableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSourceableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidSourceableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSourceableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSourceableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSourceableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSourceableSearchOrder}
 */
proto.dlkit.proto.osid.OsidSourceableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSourceableSearchOrder;
  return proto.dlkit.proto.osid.OsidSourceableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSourceableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSourceableSearchOrder}
 */
proto.dlkit.proto.osid.OsidSourceableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSourceableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSourceableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSourceableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSourceableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidFederateableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidFederateableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidFederateableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidFederateableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidFederateableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidFederateableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidFederateableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidFederateableSearchOrder}
 */
proto.dlkit.proto.osid.OsidFederateableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidFederateableSearchOrder;
  return proto.dlkit.proto.osid.OsidFederateableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidFederateableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidFederateableSearchOrder}
 */
proto.dlkit.proto.osid.OsidFederateableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidFederateableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidFederateableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidFederateableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidFederateableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidOperableSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidOperableSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidOperableSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidOperableSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidOperableSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidOperableSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidOperableSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidOperableSearchOrder}
 */
proto.dlkit.proto.osid.OsidOperableSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidOperableSearchOrder;
  return proto.dlkit.proto.osid.OsidOperableSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidOperableSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidOperableSearchOrder}
 */
proto.dlkit.proto.osid.OsidOperableSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidOperableSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidOperableSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidOperableSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidOperableSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidObjectSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidObjectSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidObjectSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidObjectSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidObjectSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidObjectSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidObjectSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidObjectSearchOrder}
 */
proto.dlkit.proto.osid.OsidObjectSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidObjectSearchOrder;
  return proto.dlkit.proto.osid.OsidObjectSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidObjectSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidObjectSearchOrder}
 */
proto.dlkit.proto.osid.OsidObjectSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidObjectSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidObjectSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidObjectSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidObjectSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRelationshipSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRelationshipSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRelationshipSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidRelationshipSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRelationshipSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRelationshipSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRelationshipSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRelationshipSearchOrder}
 */
proto.dlkit.proto.osid.OsidRelationshipSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRelationshipSearchOrder;
  return proto.dlkit.proto.osid.OsidRelationshipSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRelationshipSearchOrder}
 */
proto.dlkit.proto.osid.OsidRelationshipSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRelationshipSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRelationshipSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRelationshipSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRelationshipSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCatalogSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCatalogSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCatalogSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidCatalogSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCatalogSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCatalogSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCatalogSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCatalogSearchOrder}
 */
proto.dlkit.proto.osid.OsidCatalogSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCatalogSearchOrder;
  return proto.dlkit.proto.osid.OsidCatalogSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCatalogSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCatalogSearchOrder}
 */
proto.dlkit.proto.osid.OsidCatalogSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCatalogSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCatalogSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCatalogSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCatalogSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidRuleSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidRuleSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidRuleSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidRuleSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidRuleSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidRuleSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidRuleSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidRuleSearchOrder}
 */
proto.dlkit.proto.osid.OsidRuleSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidRuleSearchOrder;
  return proto.dlkit.proto.osid.OsidRuleSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidRuleSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidRuleSearchOrder}
 */
proto.dlkit.proto.osid.OsidRuleSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidRuleSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidRuleSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidRuleSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidRuleSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidEnablerSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidEnablerSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidEnablerSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidEnablerSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidEnablerSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidEnablerSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidEnablerSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidEnablerSearchOrder}
 */
proto.dlkit.proto.osid.OsidEnablerSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidEnablerSearchOrder;
  return proto.dlkit.proto.osid.OsidEnablerSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidEnablerSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidEnablerSearchOrder}
 */
proto.dlkit.proto.osid.OsidEnablerSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidEnablerSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidEnablerSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidEnablerSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidEnablerSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidConstrainerSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidConstrainerSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidConstrainerSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidConstrainerSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidConstrainerSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidConstrainerSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidConstrainerSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidConstrainerSearchOrder}
 */
proto.dlkit.proto.osid.OsidConstrainerSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidConstrainerSearchOrder;
  return proto.dlkit.proto.osid.OsidConstrainerSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidConstrainerSearchOrder}
 */
proto.dlkit.proto.osid.OsidConstrainerSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidConstrainerSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidConstrainerSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidConstrainerSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidConstrainerSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidProcessorSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidProcessorSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidProcessorSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidProcessorSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidProcessorSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidProcessorSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidProcessorSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidProcessorSearchOrder}
 */
proto.dlkit.proto.osid.OsidProcessorSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidProcessorSearchOrder;
  return proto.dlkit.proto.osid.OsidProcessorSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidProcessorSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidProcessorSearchOrder}
 */
proto.dlkit.proto.osid.OsidProcessorSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidProcessorSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidProcessorSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidProcessorSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidProcessorSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidGovernatorSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidGovernatorSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidGovernatorSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidGovernatorSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidGovernatorSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidGovernatorSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidGovernatorSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidGovernatorSearchOrder}
 */
proto.dlkit.proto.osid.OsidGovernatorSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidGovernatorSearchOrder;
  return proto.dlkit.proto.osid.OsidGovernatorSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidGovernatorSearchOrder}
 */
proto.dlkit.proto.osid.OsidGovernatorSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidGovernatorSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidGovernatorSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidGovernatorSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidGovernatorSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCompendiumSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCompendiumSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCompendiumSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidCompendiumSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCompendiumSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCompendiumSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCompendiumSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCompendiumSearchOrder}
 */
proto.dlkit.proto.osid.OsidCompendiumSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCompendiumSearchOrder;
  return proto.dlkit.proto.osid.OsidCompendiumSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCompendiumSearchOrder}
 */
proto.dlkit.proto.osid.OsidCompendiumSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCompendiumSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCompendiumSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCompendiumSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCompendiumSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidCapsuleSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidCapsuleSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidCapsuleSearchOrder.displayName = 'proto.dlkit.proto.osid.OsidCapsuleSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidCapsuleSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidCapsuleSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidCapsuleSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleSearchOrder.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidCapsuleSearchOrder}
 */
proto.dlkit.proto.osid.OsidCapsuleSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidCapsuleSearchOrder;
  return proto.dlkit.proto.osid.OsidCapsuleSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidCapsuleSearchOrder}
 */
proto.dlkit.proto.osid.OsidCapsuleSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidCapsuleSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidCapsuleSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidCapsuleSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidCapsuleSearchOrder.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSearch.displayName = 'proto.dlkit.proto.osid.OsidSearch';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSearch.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSearch}
 */
proto.dlkit.proto.osid.OsidSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSearch;
  return proto.dlkit.proto.osid.OsidSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSearch}
 */
proto.dlkit.proto.osid.OsidSearch.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSearch.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidSearchResults.displayName = 'proto.dlkit.proto.osid.OsidSearchResults';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSearchResults.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidSearchResults}
 */
proto.dlkit.proto.osid.OsidSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidSearchResults;
  return proto.dlkit.proto.osid.OsidSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidSearchResults}
 */
proto.dlkit.proto.osid.OsidSearchResults.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidSearchResults.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.osid.OsidList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidList.displayName = 'proto.dlkit.proto.osid.OsidList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.osid.OsidList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidList.toObject = function(includeInstance, msg) {
  var f, obj = {
    osidsList: jspb.Message.toObjectList(msg.getOsidsList(),
    proto.dlkit.proto.osid.Osid.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.osid.OsidList}
 */
proto.dlkit.proto.osid.OsidList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidList;
  return proto.dlkit.proto.osid.OsidList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidList}
 */
proto.dlkit.proto.osid.OsidList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.osid.Osid;
      reader.readMessage(value,proto.dlkit.proto.osid.Osid.deserializeBinaryFromReader);
      msg.addOsids(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.osid.OsidList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getOsidsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.osid.Osid.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Osid osids = 1;
 * @return {!Array.<!proto.dlkit.proto.osid.Osid>}
 */
proto.dlkit.proto.osid.OsidList.prototype.getOsidsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.osid.Osid>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.osid.Osid, 1));
};


/** @param {!Array.<!proto.dlkit.proto.osid.Osid>} value */
proto.dlkit.proto.osid.OsidList.prototype.setOsidsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.osid.Osid=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.osid.Osid}
 */
proto.dlkit.proto.osid.OsidList.prototype.addOsids = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.osid.Osid, opt_index);
};


proto.dlkit.proto.osid.OsidList.prototype.clearOsidsList = function() {
  this.setOsidsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.osid.Osid = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.Osid, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.Osid.displayName = 'proto.dlkit.proto.osid.Osid';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.Osid.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.Osid.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.Osid} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.Osid.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.Osid}
 */
proto.dlkit.proto.osid.Osid.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.Osid;
  return proto.dlkit.proto.osid.Osid.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.Osid} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.Osid}
 */
proto.dlkit.proto.osid.Osid.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.Osid.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.Osid.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.Osid} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.Osid.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.osid.OsidNode = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.osid.OsidNode, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.osid.OsidNode.displayName = 'proto.dlkit.proto.osid.OsidNode';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.osid.OsidNode.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.osid.OsidNode.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.osid.OsidNode} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidNode.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.osid.OsidNode}
 */
proto.dlkit.proto.osid.OsidNode.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.osid.OsidNode;
  return proto.dlkit.proto.osid.OsidNode.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.osid.OsidNode} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.osid.OsidNode}
 */
proto.dlkit.proto.osid.OsidNode.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.osid.OsidNode.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.osid.OsidNode.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.osid.OsidNode} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.osid.OsidNode.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};


goog.object.extend(exports, proto.dlkit.proto.osid);
