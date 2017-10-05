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
var dlkit_proto_resource_pb = require('../../dlkit/proto/resource_pb.js');
var google_protobuf_timestamp_pb = require('google-protobuf/google/protobuf/timestamp_pb.js');
goog.exportSymbol('proto.dlkit.proto.commenting.AddChildBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AddChildBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AddRootBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AddRootBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AliasBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AliasBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AliasCommentReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AliasCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AssignCommentToBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.AssignCommentToBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.Book', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookForm', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookList', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookNode', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookNodeList', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.BookSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanAccessBookHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanAssignCommentsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanAssignCommentsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanAssignCommentsToBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateBooksReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateCommentsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanCreateCommentsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanDeleteBooksReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanDeleteBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanDeleteCommentsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanDeleteCommentsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanLookupBooksReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanLookupBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanLookupCommentsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanLookupCommentsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanManageBookAliasesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanManageBookAliasesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanManageCommentAliasesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanManageCommentAliasesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanModifyBookHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanSearchCommentsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanSearchCommentsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanUpdateBooksReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanUpdateBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanUpdateCommentsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CanUpdateCommentsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.Comment', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CommentForm', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CommentList', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CommentQuery', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CommentQueryInspector', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CommentSearch', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CommentSearchOrder', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CommentSearchResults', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CreateBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CreateBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CreateCommentReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.CreateCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.DeleteBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.DeleteBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.DeleteCommentReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.DeleteCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetAssignableBookIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookFormForCreateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookFormForCreateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookFormForUpdateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookFormForUpdateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookHierarchyIdReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookHierarchyIdRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookHierarchyReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookHierarchyRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookIdReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookIdRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookIdsByCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookNodeIdsReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookNodeIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookNodesReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookNodesRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBooksByCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBooksByIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBooksByProviderRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetChildBookIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetChildBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentFormForCreateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentFormForCreateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentFormForUpdateReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentIdsByBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentQueryReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByQueryRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsForCommentorRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsForReferenceRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsOnDateRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetCommentsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetParentBookIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetParentBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetRootBookIdsRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.GetRootBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.HasChildBooksReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.HasChildBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.HasParentBooksReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.HasParentBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsAncestorOfBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsAncestorOfBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsChildOfBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsChildOfBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsDescendantOfBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsDescendantOfBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsParentOfBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.IsParentOfBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.ReassignCommentToBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.ReassignCommentToBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.RemoveChildBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.RemoveChildBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.RemoveChildBooksReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.RemoveChildBooksRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.RemoveRootBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.RemoveRootBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UnassignCommentFromBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UnassignCommentFromBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UpdateBookReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UpdateBookRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UpdateCommentReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UpdateCommentRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseComparativeBookViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseComparativeBookViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseComparativeCommentViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseComparativeCommentViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseEffectiveCommentViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseFederatedBookViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseFederatedBookViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseIsolatedBookViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UseIsolatedBookViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UsePlenaryBookViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UsePlenaryBookViewRequest', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UsePlenaryCommentViewReply', null, global);
goog.exportSymbol('proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest', null, global);

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.Comment = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.Comment, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.Comment.displayName = 'proto.dlkit.proto.commenting.Comment';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.Comment.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.Comment.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.Comment} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.Comment.toObject = function(includeInstance, msg) {
  var f, obj = {
    book: (f = msg.getBook()) && dlkit_proto_osid_pb.OsidCatalog.toObject(includeInstance, f),
    commentor: (f = msg.getCommentor()) && dlkit_proto_resource_pb.Resource.toObject(includeInstance, f),
    rating: (f = msg.getRating()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    reference: (f = msg.getReference()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    text: jspb.Message.getFieldWithDefault(msg, 5, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.Comment}
 */
proto.dlkit.proto.commenting.Comment.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.Comment;
  return proto.dlkit.proto.commenting.Comment.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.Comment} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.Comment}
 */
proto.dlkit.proto.commenting.Comment.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_proto_osid_pb.OsidCatalog;
      reader.readMessage(value,dlkit_proto_osid_pb.OsidCatalog.deserializeBinaryFromReader);
      msg.setBook(value);
      break;
    case 2:
      var value = new dlkit_proto_resource_pb.Resource;
      reader.readMessage(value,dlkit_proto_resource_pb.Resource.deserializeBinaryFromReader);
      msg.setCommentor(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setRating(value);
      break;
    case 4:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReference(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setText(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.Comment.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.Comment.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.Comment} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.Comment.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBook();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_proto_osid_pb.OsidCatalog.serializeBinaryToWriter
    );
  }
  f = message.getCommentor();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_proto_resource_pb.Resource.serializeBinaryToWriter
    );
  }
  f = message.getRating();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getReference();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getText();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
};


/**
 * optional dlkit.proto.osid.OsidCatalog book = 1;
 * @return {?proto.dlkit.proto.osid.OsidCatalog}
 */
proto.dlkit.proto.commenting.Comment.prototype.getBook = function() {
  return /** @type{?proto.dlkit.proto.osid.OsidCatalog} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_osid_pb.OsidCatalog, 1));
};


/** @param {?proto.dlkit.proto.osid.OsidCatalog|undefined} value */
proto.dlkit.proto.commenting.Comment.prototype.setBook = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.Comment.prototype.clearBook = function() {
  this.setBook(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Comment.prototype.hasBook = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.proto.resource.Resource commentor = 2;
 * @return {?proto.dlkit.proto.resource.Resource}
 */
proto.dlkit.proto.commenting.Comment.prototype.getCommentor = function() {
  return /** @type{?proto.dlkit.proto.resource.Resource} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_resource_pb.Resource, 2));
};


/** @param {?proto.dlkit.proto.resource.Resource|undefined} value */
proto.dlkit.proto.commenting.Comment.prototype.setCommentor = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.Comment.prototype.clearCommentor = function() {
  this.setCommentor(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Comment.prototype.hasCommentor = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id rating = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.Comment.prototype.getRating = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.Comment.prototype.setRating = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.Comment.prototype.clearRating = function() {
  this.setRating(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Comment.prototype.hasRating = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id reference = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.Comment.prototype.getReference = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.Comment.prototype.setReference = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.commenting.Comment.prototype.clearReference = function() {
  this.setReference(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Comment.prototype.hasReference = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional string text = 5;
 * @return {string}
 */
proto.dlkit.proto.commenting.Comment.prototype.getText = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/** @param {string} value */
proto.dlkit.proto.commenting.Comment.prototype.setText = function(value) {
  jspb.Message.setProto3StringField(this, 5, value);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CommentQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CommentQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CommentQuery.displayName = 'proto.dlkit.proto.commenting.CommentQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CommentQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CommentQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CommentQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentQuery.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CommentQuery}
 */
proto.dlkit.proto.commenting.CommentQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CommentQuery;
  return proto.dlkit.proto.commenting.CommentQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CommentQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CommentQuery}
 */
proto.dlkit.proto.commenting.CommentQuery.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CommentQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CommentQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CommentQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentQuery.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CommentQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CommentQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CommentQueryInspector.displayName = 'proto.dlkit.proto.commenting.CommentQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CommentQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CommentQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CommentQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentQueryInspector.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CommentQueryInspector}
 */
proto.dlkit.proto.commenting.CommentQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CommentQueryInspector;
  return proto.dlkit.proto.commenting.CommentQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CommentQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CommentQueryInspector}
 */
proto.dlkit.proto.commenting.CommentQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CommentQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CommentQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CommentQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentQueryInspector.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CommentForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CommentForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CommentForm.displayName = 'proto.dlkit.proto.commenting.CommentForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CommentForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CommentForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CommentForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentForm.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CommentForm}
 */
proto.dlkit.proto.commenting.CommentForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CommentForm;
  return proto.dlkit.proto.commenting.CommentForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CommentForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CommentForm}
 */
proto.dlkit.proto.commenting.CommentForm.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CommentForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CommentForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CommentForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentForm.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CommentSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CommentSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CommentSearchOrder.displayName = 'proto.dlkit.proto.commenting.CommentSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CommentSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CommentSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CommentSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentSearchOrder.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CommentSearchOrder}
 */
proto.dlkit.proto.commenting.CommentSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CommentSearchOrder;
  return proto.dlkit.proto.commenting.CommentSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CommentSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CommentSearchOrder}
 */
proto.dlkit.proto.commenting.CommentSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CommentSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CommentSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CommentSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentSearchOrder.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CommentSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CommentSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CommentSearch.displayName = 'proto.dlkit.proto.commenting.CommentSearch';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CommentSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CommentSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CommentSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentSearch.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CommentSearch}
 */
proto.dlkit.proto.commenting.CommentSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CommentSearch;
  return proto.dlkit.proto.commenting.CommentSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CommentSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CommentSearch}
 */
proto.dlkit.proto.commenting.CommentSearch.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CommentSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CommentSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CommentSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentSearch.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CommentSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CommentSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CommentSearchResults.displayName = 'proto.dlkit.proto.commenting.CommentSearchResults';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CommentSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CommentSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CommentSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentSearchResults.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CommentSearchResults}
 */
proto.dlkit.proto.commenting.CommentSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CommentSearchResults;
  return proto.dlkit.proto.commenting.CommentSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CommentSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CommentSearchResults}
 */
proto.dlkit.proto.commenting.CommentSearchResults.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CommentSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CommentSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CommentSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentSearchResults.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CommentList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.CommentList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.CommentList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CommentList.displayName = 'proto.dlkit.proto.commenting.CommentList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.CommentList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CommentList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CommentList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CommentList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentList.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentsList: jspb.Message.toObjectList(msg.getCommentsList(),
    proto.dlkit.proto.commenting.Comment.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CommentList}
 */
proto.dlkit.proto.commenting.CommentList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CommentList;
  return proto.dlkit.proto.commenting.CommentList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CommentList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CommentList}
 */
proto.dlkit.proto.commenting.CommentList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.Comment;
      reader.readMessage(value,proto.dlkit.proto.commenting.Comment.deserializeBinaryFromReader);
      msg.addComments(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CommentList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CommentList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CommentList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CommentList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.commenting.Comment.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Comment comments = 1;
 * @return {!Array.<!proto.dlkit.proto.commenting.Comment>}
 */
proto.dlkit.proto.commenting.CommentList.prototype.getCommentsList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.commenting.Comment>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.commenting.Comment, 1));
};


/** @param {!Array.<!proto.dlkit.proto.commenting.Comment>} value */
proto.dlkit.proto.commenting.CommentList.prototype.setCommentsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.commenting.Comment=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.commenting.Comment}
 */
proto.dlkit.proto.commenting.CommentList.prototype.addComments = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.commenting.Comment, opt_index);
};


proto.dlkit.proto.commenting.CommentList.prototype.clearCommentsList = function() {
  this.setCommentsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.Book = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.Book.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.Book, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.Book.displayName = 'proto.dlkit.proto.commenting.Book';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.Book.repeatedFields_ = [5];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.Book.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.Book.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.Book} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.Book.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.Book}
 */
proto.dlkit.proto.commenting.Book.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.Book;
  return proto.dlkit.proto.commenting.Book.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.Book} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.Book}
 */
proto.dlkit.proto.commenting.Book.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.Book.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.Book.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.Book} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.Book.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.Book.prototype.getDescription = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 1));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.commenting.Book.prototype.setDescription = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.Book.prototype.clearDescription = function() {
  this.setDescription(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Book.prototype.hasDescription = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.locale.primitives.DisplayText display_name = 2;
 * @return {?proto.dlkit.primordium.locale.primitives.DisplayText}
 */
proto.dlkit.proto.commenting.Book.prototype.getDisplayName = function() {
  return /** @type{?proto.dlkit.primordium.locale.primitives.DisplayText} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_locale_primitives_pb.DisplayText, 2));
};


/** @param {?proto.dlkit.primordium.locale.primitives.DisplayText|undefined} value */
proto.dlkit.proto.commenting.Book.prototype.setDisplayName = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.Book.prototype.clearDisplayName = function() {
  this.setDisplayName(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Book.prototype.hasDisplayName = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.type.primitives.Type genus_type_id = 3;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.Book.prototype.getGenusTypeId = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 3));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.Book.prototype.setGenusTypeId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.Book.prototype.clearGenusTypeId = function() {
  this.setGenusTypeId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Book.prototype.hasGenusTypeId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.Book.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.Book.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.commenting.Book.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.Book.prototype.hasId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * repeated dlkit.primordium.type.primitives.Type record_type_ids = 5;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.commenting.Book.prototype.getRecordTypeIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 5));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.commenting.Book.prototype.setRecordTypeIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 5, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.Book.prototype.addRecordTypeIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 5, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.commenting.Book.prototype.clearRecordTypeIdsList = function() {
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
proto.dlkit.proto.commenting.BookQuery = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookQuery, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookQuery.displayName = 'proto.dlkit.proto.commenting.BookQuery';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookQuery.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookQuery.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookQuery} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookQuery.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookQuery}
 */
proto.dlkit.proto.commenting.BookQuery.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookQuery;
  return proto.dlkit.proto.commenting.BookQuery.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookQuery} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookQuery}
 */
proto.dlkit.proto.commenting.BookQuery.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookQuery.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookQuery.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookQuery} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookQuery.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookQueryInspector = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookQueryInspector, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookQueryInspector.displayName = 'proto.dlkit.proto.commenting.BookQueryInspector';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookQueryInspector.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookQueryInspector.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookQueryInspector} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookQueryInspector.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookQueryInspector}
 */
proto.dlkit.proto.commenting.BookQueryInspector.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookQueryInspector;
  return proto.dlkit.proto.commenting.BookQueryInspector.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookQueryInspector} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookQueryInspector}
 */
proto.dlkit.proto.commenting.BookQueryInspector.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookQueryInspector.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookQueryInspector.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookQueryInspector} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookQueryInspector.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookForm = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookForm, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookForm.displayName = 'proto.dlkit.proto.commenting.BookForm';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookForm.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookForm.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookForm} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookForm.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookForm}
 */
proto.dlkit.proto.commenting.BookForm.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookForm;
  return proto.dlkit.proto.commenting.BookForm.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookForm} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookForm}
 */
proto.dlkit.proto.commenting.BookForm.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookForm.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookForm.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookForm} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookForm.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookSearchOrder = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookSearchOrder, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookSearchOrder.displayName = 'proto.dlkit.proto.commenting.BookSearchOrder';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookSearchOrder.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookSearchOrder.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookSearchOrder} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookSearchOrder.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookSearchOrder}
 */
proto.dlkit.proto.commenting.BookSearchOrder.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookSearchOrder;
  return proto.dlkit.proto.commenting.BookSearchOrder.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookSearchOrder} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookSearchOrder}
 */
proto.dlkit.proto.commenting.BookSearchOrder.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookSearchOrder.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookSearchOrder.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookSearchOrder} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookSearchOrder.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookSearch = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookSearch, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookSearch.displayName = 'proto.dlkit.proto.commenting.BookSearch';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookSearch.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookSearch.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookSearch} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookSearch.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookSearch}
 */
proto.dlkit.proto.commenting.BookSearch.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookSearch;
  return proto.dlkit.proto.commenting.BookSearch.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookSearch} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookSearch}
 */
proto.dlkit.proto.commenting.BookSearch.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookSearch.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookSearch.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookSearch} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookSearch.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookSearchResults = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookSearchResults, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookSearchResults.displayName = 'proto.dlkit.proto.commenting.BookSearchResults';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookSearchResults.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookSearchResults.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookSearchResults} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookSearchResults.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookSearchResults}
 */
proto.dlkit.proto.commenting.BookSearchResults.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookSearchResults;
  return proto.dlkit.proto.commenting.BookSearchResults.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookSearchResults} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookSearchResults}
 */
proto.dlkit.proto.commenting.BookSearchResults.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookSearchResults.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookSearchResults.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookSearchResults} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookSearchResults.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.BookList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookList.displayName = 'proto.dlkit.proto.commenting.BookList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.BookList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookList.toObject = function(includeInstance, msg) {
  var f, obj = {
    booksList: jspb.Message.toObjectList(msg.getBooksList(),
    proto.dlkit.proto.commenting.Book.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookList}
 */
proto.dlkit.proto.commenting.BookList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookList;
  return proto.dlkit.proto.commenting.BookList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookList}
 */
proto.dlkit.proto.commenting.BookList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.Book;
      reader.readMessage(value,proto.dlkit.proto.commenting.Book.deserializeBinaryFromReader);
      msg.addBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBooksList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.commenting.Book.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Book books = 1;
 * @return {!Array.<!proto.dlkit.proto.commenting.Book>}
 */
proto.dlkit.proto.commenting.BookList.prototype.getBooksList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.commenting.Book>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.commenting.Book, 1));
};


/** @param {!Array.<!proto.dlkit.proto.commenting.Book>} value */
proto.dlkit.proto.commenting.BookList.prototype.setBooksList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.commenting.Book=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.commenting.Book}
 */
proto.dlkit.proto.commenting.BookList.prototype.addBooks = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.commenting.Book, opt_index);
};


proto.dlkit.proto.commenting.BookList.prototype.clearBooksList = function() {
  this.setBooksList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookNode = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookNode, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookNode.displayName = 'proto.dlkit.proto.commenting.BookNode';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookNode.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookNode.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookNode} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookNode.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookNode}
 */
proto.dlkit.proto.commenting.BookNode.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookNode;
  return proto.dlkit.proto.commenting.BookNode.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookNode} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookNode}
 */
proto.dlkit.proto.commenting.BookNode.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookNode.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookNode.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookNode} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookNode.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.BookNodeList = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.BookNodeList.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.BookNodeList, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.BookNodeList.displayName = 'proto.dlkit.proto.commenting.BookNodeList';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.BookNodeList.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.BookNodeList.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.BookNodeList.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.BookNodeList} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookNodeList.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookNodesList: jspb.Message.toObjectList(msg.getBookNodesList(),
    proto.dlkit.proto.commenting.BookNode.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.BookNodeList}
 */
proto.dlkit.proto.commenting.BookNodeList.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.BookNodeList;
  return proto.dlkit.proto.commenting.BookNodeList.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.BookNodeList} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.BookNodeList}
 */
proto.dlkit.proto.commenting.BookNodeList.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.BookNode;
      reader.readMessage(value,proto.dlkit.proto.commenting.BookNode.deserializeBinaryFromReader);
      msg.addBookNodes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.BookNodeList.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.BookNodeList.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.BookNodeList} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.BookNodeList.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookNodesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.dlkit.proto.commenting.BookNode.serializeBinaryToWriter
    );
  }
};


/**
 * repeated BookNode book_nodes = 1;
 * @return {!Array.<!proto.dlkit.proto.commenting.BookNode>}
 */
proto.dlkit.proto.commenting.BookNodeList.prototype.getBookNodesList = function() {
  return /** @type{!Array.<!proto.dlkit.proto.commenting.BookNode>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.dlkit.proto.commenting.BookNode, 1));
};


/** @param {!Array.<!proto.dlkit.proto.commenting.BookNode>} value */
proto.dlkit.proto.commenting.BookNodeList.prototype.setBookNodesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.proto.commenting.BookNode=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.proto.commenting.BookNode}
 */
proto.dlkit.proto.commenting.BookNodeList.prototype.addBookNodes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.proto.commenting.BookNode, opt_index);
};


proto.dlkit.proto.commenting.BookNodeList.prototype.clearBookNodesList = function() {
  this.setBookNodesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBookIdReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookIdReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookIdReply.displayName = 'proto.dlkit.proto.commenting.GetBookIdReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookIdReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookIdReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookIdReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookIdReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.GetBookIdReply}
 */
proto.dlkit.proto.commenting.GetBookIdReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookIdReply;
  return proto.dlkit.proto.commenting.GetBookIdReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookIdReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookIdReply}
 */
proto.dlkit.proto.commenting.GetBookIdReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.GetBookIdReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookIdReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookIdReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookIdReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.GetBookIdReply.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBookIdReply.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookIdReply.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookIdReply.prototype.hasId = function() {
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
proto.dlkit.proto.commenting.GetBookIdRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookIdRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookIdRequest.displayName = 'proto.dlkit.proto.commenting.GetBookIdRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookIdRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookIdRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookIdRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookIdRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookIdRequest}
 */
proto.dlkit.proto.commenting.GetBookIdRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookIdRequest;
  return proto.dlkit.proto.commenting.GetBookIdRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookIdRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookIdRequest}
 */
proto.dlkit.proto.commenting.GetBookIdRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookIdRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookIdRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookIdRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookIdRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookReply.displayName = 'proto.dlkit.proto.commenting.GetBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    book: (f = msg.getBook()) && proto.dlkit.proto.commenting.Book.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookReply}
 */
proto.dlkit.proto.commenting.GetBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookReply;
  return proto.dlkit.proto.commenting.GetBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookReply}
 */
proto.dlkit.proto.commenting.GetBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.Book;
      reader.readMessage(value,proto.dlkit.proto.commenting.Book.deserializeBinaryFromReader);
      msg.setBook(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBook();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.Book.serializeBinaryToWriter
    );
  }
};


/**
 * optional Book book = 1;
 * @return {?proto.dlkit.proto.commenting.Book}
 */
proto.dlkit.proto.commenting.GetBookReply.prototype.getBook = function() {
  return /** @type{?proto.dlkit.proto.commenting.Book} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.Book, 1));
};


/** @param {?proto.dlkit.proto.commenting.Book|undefined} value */
proto.dlkit.proto.commenting.GetBookReply.prototype.setBook = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookReply.prototype.clearBook = function() {
  this.setBook(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookReply.prototype.hasBook = function() {
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
proto.dlkit.proto.commenting.GetBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookRequest.displayName = 'proto.dlkit.proto.commenting.GetBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookRequest}
 */
proto.dlkit.proto.commenting.GetBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookRequest;
  return proto.dlkit.proto.commenting.GetBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookRequest}
 */
proto.dlkit.proto.commenting.GetBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanLookupCommentsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanLookupCommentsReply.displayName = 'proto.dlkit.proto.commenting.CanLookupCommentsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanLookupCommentsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupComments: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentsReply}
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanLookupCommentsReply;
  return proto.dlkit.proto.commenting.CanLookupCommentsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentsReply}
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupComments(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanLookupCommentsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupComments();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_comments = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanLookupCommentsReply.prototype.getCanLookupComments = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanLookupCommentsReply.prototype.setCanLookupComments = function(value) {
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
proto.dlkit.proto.commenting.CanLookupCommentsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanLookupCommentsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanLookupCommentsRequest.displayName = 'proto.dlkit.proto.commenting.CanLookupCommentsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanLookupCommentsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanLookupCommentsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentsRequest}
 */
proto.dlkit.proto.commenting.CanLookupCommentsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanLookupCommentsRequest;
  return proto.dlkit.proto.commenting.CanLookupCommentsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentsRequest}
 */
proto.dlkit.proto.commenting.CanLookupCommentsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanLookupCommentsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanLookupCommentsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseComparativeCommentViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseComparativeCommentViewReply.displayName = 'proto.dlkit.proto.commenting.UseComparativeCommentViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseComparativeCommentViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseComparativeCommentViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseComparativeCommentViewReply}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseComparativeCommentViewReply;
  return proto.dlkit.proto.commenting.UseComparativeCommentViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseComparativeCommentViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseComparativeCommentViewReply}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseComparativeCommentViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseComparativeCommentViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseComparativeCommentViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.displayName = 'proto.dlkit.proto.commenting.UseComparativeCommentViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseComparativeCommentViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseComparativeCommentViewRequest}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseComparativeCommentViewRequest;
  return proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseComparativeCommentViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseComparativeCommentViewRequest}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseComparativeCommentViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeCommentViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UsePlenaryCommentViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.displayName = 'proto.dlkit.proto.commenting.UsePlenaryCommentViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UsePlenaryCommentViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryCommentViewReply}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UsePlenaryCommentViewReply;
  return proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryCommentViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryCommentViewReply}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryCommentViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.displayName = 'proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest;
  return proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryCommentViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseFederatedBookViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseFederatedBookViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseFederatedBookViewReply.displayName = 'proto.dlkit.proto.commenting.UseFederatedBookViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseFederatedBookViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseFederatedBookViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseFederatedBookViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseFederatedBookViewReply}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseFederatedBookViewReply;
  return proto.dlkit.proto.commenting.UseFederatedBookViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseFederatedBookViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseFederatedBookViewReply}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseFederatedBookViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseFederatedBookViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseFederatedBookViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseFederatedBookViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseFederatedBookViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseFederatedBookViewRequest.displayName = 'proto.dlkit.proto.commenting.UseFederatedBookViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseFederatedBookViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseFederatedBookViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseFederatedBookViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseFederatedBookViewRequest}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseFederatedBookViewRequest;
  return proto.dlkit.proto.commenting.UseFederatedBookViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseFederatedBookViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseFederatedBookViewRequest}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseFederatedBookViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseFederatedBookViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseFederatedBookViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseFederatedBookViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseIsolatedBookViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseIsolatedBookViewReply.displayName = 'proto.dlkit.proto.commenting.UseIsolatedBookViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseIsolatedBookViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseIsolatedBookViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseIsolatedBookViewReply}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseIsolatedBookViewReply;
  return proto.dlkit.proto.commenting.UseIsolatedBookViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseIsolatedBookViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseIsolatedBookViewReply}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseIsolatedBookViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseIsolatedBookViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseIsolatedBookViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.displayName = 'proto.dlkit.proto.commenting.UseIsolatedBookViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseIsolatedBookViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseIsolatedBookViewRequest}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseIsolatedBookViewRequest;
  return proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseIsolatedBookViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseIsolatedBookViewRequest}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseIsolatedBookViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseIsolatedBookViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseEffectiveCommentViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.displayName = 'proto.dlkit.proto.commenting.UseEffectiveCommentViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseEffectiveCommentViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseEffectiveCommentViewReply}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseEffectiveCommentViewReply;
  return proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseEffectiveCommentViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseEffectiveCommentViewReply}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseEffectiveCommentViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.displayName = 'proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest;
  return proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseEffectiveCommentViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.displayName = 'proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply;
  return proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.displayName = 'proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest;
  return proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseAnyEffectiveCommentViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentReply.displayName = 'proto.dlkit.proto.commenting.GetCommentReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    comment: (f = msg.getComment()) && proto.dlkit.proto.commenting.Comment.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentReply}
 */
proto.dlkit.proto.commenting.GetCommentReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentReply;
  return proto.dlkit.proto.commenting.GetCommentReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentReply}
 */
proto.dlkit.proto.commenting.GetCommentReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.Comment;
      reader.readMessage(value,proto.dlkit.proto.commenting.Comment.deserializeBinaryFromReader);
      msg.setComment(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getComment();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.Comment.serializeBinaryToWriter
    );
  }
};


/**
 * optional Comment comment = 1;
 * @return {?proto.dlkit.proto.commenting.Comment}
 */
proto.dlkit.proto.commenting.GetCommentReply.prototype.getComment = function() {
  return /** @type{?proto.dlkit.proto.commenting.Comment} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.Comment, 1));
};


/** @param {?proto.dlkit.proto.commenting.Comment|undefined} value */
proto.dlkit.proto.commenting.GetCommentReply.prototype.setComment = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentReply.prototype.clearComment = function() {
  this.setComment(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentReply.prototype.hasComment = function() {
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
proto.dlkit.proto.commenting.GetCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentRequest}
 */
proto.dlkit.proto.commenting.GetCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentRequest;
  return proto.dlkit.proto.commenting.GetCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentRequest}
 */
proto.dlkit.proto.commenting.GetCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.GetCommentsByIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.GetCommentsByIdsRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByIdsRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByIdsRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentIdsList: jspb.Message.toObjectList(msg.getCommentIdsList(),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByIdsRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByIdsRequest;
  return proto.dlkit.proto.commenting.GetCommentsByIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByIdsRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addCommentIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id comment_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.prototype.getCommentIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.prototype.setCommentIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByIdsRequest.prototype.addCommentIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.commenting.GetCommentsByIdsRequest.prototype.clearCommentIdsList = function() {
  this.setCommentIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeRequest.prototype.hasCommentGenusType = function() {
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
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest;
  return proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByParentGenusTypeRequest.prototype.hasCommentGenusType = function() {
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
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentRecordType: (f = msg.getCommentRecordType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest;
  return proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentRecordType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentRecordType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type comment_record_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.prototype.getCommentRecordType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.prototype.setCommentRecordType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.prototype.clearCommentRecordType = function() {
  this.setCommentRecordType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByRecordTypeRequest.prototype.hasCommentRecordType = function() {
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
proto.dlkit.proto.commenting.GetCommentsOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp to = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
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
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.hasCommentGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp to = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsForCommentorRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsForCommentorRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsForCommentorRequest;
  return proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorRequest.prototype.hasResourceId = function() {
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
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setResourceId(value);
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
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFrom();
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
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp to = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    case 2:
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
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
};


/**
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.hasCommentGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorRequest.prototype.hasResourceId = function() {
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResourceId(value);
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
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
  f = message.getResourceId();
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
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.hasCommentGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp to = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsForReferenceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsForReferenceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsForReferenceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsForReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsForReferenceRequest;
  return proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForReferenceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsForReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReferenceId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForReferenceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getReferenceId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceRequest.prototype.hasReferenceId = function() {
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
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setReferenceId(value);
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
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getReferenceId();
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
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.hasReferenceId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional google.protobuf.Timestamp to = 3;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 3));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForReferenceOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReferenceId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getReferenceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.hasCommentGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceRequest.prototype.hasReferenceId = function() {
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReferenceId(value);
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
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
  f = message.getReferenceId();
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
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.hasCommentGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.hasReferenceId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp to = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForReferenceOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest;
  return proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReferenceId(value);
      break;
    case 2:
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
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getReferenceId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
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
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.hasReferenceId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceRequest.prototype.hasResourceId = function() {
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
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setReferenceId(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResourceId(value);
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
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFrom();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      google_protobuf_timestamp_pb.Timestamp.serializeBinaryToWriter
    );
  }
  f = message.getReferenceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
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
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 1));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.hasReferenceId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional google.protobuf.Timestamp to = 4;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 4));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsForCommentorAndReferenceOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReferenceId(value);
      break;
    case 3:
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getReferenceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
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
};


/**
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.hasCommentGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.hasReferenceId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceRequest.prototype.hasResourceId = function() {
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentGenusType: (f = msg.getCommentGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f),
    from: (f = msg.getFrom()) && google_protobuf_timestamp_pb.Timestamp.toObject(includeInstance, f),
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    resourceId: (f = msg.getResourceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest;
  return proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setCommentGenusType(value);
      break;
    case 2:
      var value = new google_protobuf_timestamp_pb.Timestamp;
      reader.readMessage(value,google_protobuf_timestamp_pb.Timestamp.deserializeBinaryFromReader);
      msg.setFrom(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReferenceId(value);
      break;
    case 4:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setResourceId(value);
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
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
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
  f = message.getReferenceId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getResourceId();
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
 * optional dlkit.primordium.type.primitives.Type comment_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.getCommentGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.setCommentGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.clearCommentGenusType = function() {
  this.setCommentGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.hasCommentGenusType = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional google.protobuf.Timestamp from_ = 2;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.getFrom = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 2));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.setFrom = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.clearFrom = function() {
  this.setFrom(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.hasFrom = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.hasReferenceId = function() {
  return jspb.Message.getField(this, 3) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id resource_id = 4;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 4));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 4, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.hasResourceId = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional google.protobuf.Timestamp to = 5;
 * @return {?proto.google.protobuf.Timestamp}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.getTo = function() {
  return /** @type{?proto.google.protobuf.Timestamp} */ (
    jspb.Message.getWrapperField(this, google_protobuf_timestamp_pb.Timestamp, 5));
};


/** @param {?proto.google.protobuf.Timestamp|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.setTo = function(value) {
  jspb.Message.setWrapperField(this, 5, value);
};


proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.clearTo = function() {
  this.setTo(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.prototype.hasTo = function() {
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
proto.dlkit.proto.commenting.GetCommentsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsRequest}
 */
proto.dlkit.proto.commenting.GetCommentsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsRequest;
  return proto.dlkit.proto.commenting.GetCommentsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsRequest}
 */
proto.dlkit.proto.commenting.GetCommentsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanSearchCommentsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanSearchCommentsReply.displayName = 'proto.dlkit.proto.commenting.CanSearchCommentsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanSearchCommentsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanSearchCommentsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canSearchComments: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanSearchCommentsReply}
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanSearchCommentsReply;
  return proto.dlkit.proto.commenting.CanSearchCommentsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanSearchCommentsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanSearchCommentsReply}
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanSearchComments(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanSearchCommentsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanSearchCommentsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanSearchComments();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_search_comments = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanSearchCommentsReply.prototype.getCanSearchComments = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanSearchCommentsReply.prototype.setCanSearchComments = function(value) {
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
proto.dlkit.proto.commenting.CanSearchCommentsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanSearchCommentsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanSearchCommentsRequest.displayName = 'proto.dlkit.proto.commenting.CanSearchCommentsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanSearchCommentsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanSearchCommentsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanSearchCommentsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanSearchCommentsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanSearchCommentsRequest}
 */
proto.dlkit.proto.commenting.CanSearchCommentsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanSearchCommentsRequest;
  return proto.dlkit.proto.commenting.CanSearchCommentsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanSearchCommentsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanSearchCommentsRequest}
 */
proto.dlkit.proto.commenting.CanSearchCommentsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanSearchCommentsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanSearchCommentsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanSearchCommentsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanSearchCommentsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentQueryReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentQueryReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentQueryReply.displayName = 'proto.dlkit.proto.commenting.GetCommentQueryReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentQueryReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentQueryReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentQuery: (f = msg.getCommentQuery()) && proto.dlkit.proto.commenting.CommentQuery.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentQueryReply}
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentQueryReply;
  return proto.dlkit.proto.commenting.GetCommentQueryReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentQueryReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentQueryReply}
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.CommentQuery;
      reader.readMessage(value,proto.dlkit.proto.commenting.CommentQuery.deserializeBinaryFromReader);
      msg.setCommentQuery(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentQueryReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentQueryReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.CommentQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional CommentQuery comment_query = 1;
 * @return {?proto.dlkit.proto.commenting.CommentQuery}
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.prototype.getCommentQuery = function() {
  return /** @type{?proto.dlkit.proto.commenting.CommentQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.CommentQuery, 1));
};


/** @param {?proto.dlkit.proto.commenting.CommentQuery|undefined} value */
proto.dlkit.proto.commenting.GetCommentQueryReply.prototype.setCommentQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentQueryReply.prototype.clearCommentQuery = function() {
  this.setCommentQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentQueryReply.prototype.hasCommentQuery = function() {
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
proto.dlkit.proto.commenting.GetCommentQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentQueryRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentQueryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentQueryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentQueryRequest}
 */
proto.dlkit.proto.commenting.GetCommentQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentQueryRequest;
  return proto.dlkit.proto.commenting.GetCommentQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentQueryRequest}
 */
proto.dlkit.proto.commenting.GetCommentQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentQueryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByQueryRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByQueryRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByQueryRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByQueryRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByQueryRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentQuery: (f = msg.getCommentQuery()) && proto.dlkit.proto.commenting.CommentQuery.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByQueryRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByQueryRequest;
  return proto.dlkit.proto.commenting.GetCommentsByQueryRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByQueryRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByQueryRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.CommentQuery;
      reader.readMessage(value,proto.dlkit.proto.commenting.CommentQuery.deserializeBinaryFromReader);
      msg.setCommentQuery(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByQueryRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByQueryRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentQuery();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.CommentQuery.serializeBinaryToWriter
    );
  }
};


/**
 * optional CommentQuery comment_query = 1;
 * @return {?proto.dlkit.proto.commenting.CommentQuery}
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.prototype.getCommentQuery = function() {
  return /** @type{?proto.dlkit.proto.commenting.CommentQuery} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.CommentQuery, 1));
};


/** @param {?proto.dlkit.proto.commenting.CommentQuery|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.prototype.setCommentQuery = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByQueryRequest.prototype.clearCommentQuery = function() {
  this.setCommentQuery(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByQueryRequest.prototype.hasCommentQuery = function() {
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
proto.dlkit.proto.commenting.CanCreateCommentsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateCommentsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateCommentsReply.displayName = 'proto.dlkit.proto.commenting.CanCreateCommentsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateCommentsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateCommentsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateComments: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentsReply}
 */
proto.dlkit.proto.commenting.CanCreateCommentsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateCommentsReply;
  return proto.dlkit.proto.commenting.CanCreateCommentsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentsReply}
 */
proto.dlkit.proto.commenting.CanCreateCommentsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateComments(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateCommentsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateCommentsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateComments();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_comments = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanCreateCommentsReply.prototype.getCanCreateComments = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanCreateCommentsReply.prototype.setCanCreateComments = function(value) {
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
proto.dlkit.proto.commenting.CanCreateCommentsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateCommentsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateCommentsRequest.displayName = 'proto.dlkit.proto.commenting.CanCreateCommentsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateCommentsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateCommentsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentsRequest}
 */
proto.dlkit.proto.commenting.CanCreateCommentsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateCommentsRequest;
  return proto.dlkit.proto.commenting.CanCreateCommentsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentsRequest}
 */
proto.dlkit.proto.commenting.CanCreateCommentsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateCommentsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateCommentsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.displayName = 'proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateCommentWithRecordTypes: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply;
  return proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateCommentWithRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateCommentWithRecordTypes();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_comment_with_record_types = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.prototype.getCanCreateCommentWithRecordTypes = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesReply.prototype.setCanCreateCommentWithRecordTypes = function(value) {
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
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.displayName = 'proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentRecordTypesList: jspb.Message.toObjectList(msg.getCommentRecordTypesList(),
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
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest;
  return proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addCommentRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type comment_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.prototype.getCommentRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.prototype.setCommentRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.prototype.addCommentRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.commenting.CanCreateCommentWithRecordTypesRequest.prototype.clearCommentRecordTypesList = function() {
  this.setCommentRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentFormForCreateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentFormForCreateReply.displayName = 'proto.dlkit.proto.commenting.GetCommentFormForCreateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentFormForCreateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForCreateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentForm: (f = msg.getCommentForm()) && proto.dlkit.proto.commenting.CommentForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForCreateReply}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentFormForCreateReply;
  return proto.dlkit.proto.commenting.GetCommentFormForCreateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForCreateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForCreateReply}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.CommentForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.CommentForm.deserializeBinaryFromReader);
      msg.setCommentForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentFormForCreateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForCreateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.CommentForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CommentForm comment_form = 1;
 * @return {?proto.dlkit.proto.commenting.CommentForm}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.prototype.getCommentForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.CommentForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.CommentForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.CommentForm|undefined} value */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.prototype.setCommentForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentFormForCreateReply.prototype.clearCommentForm = function() {
  this.setCommentForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateReply.prototype.hasCommentForm = function() {
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
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentFormForCreateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentFormForCreateRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForCreateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentRecordTypesList: jspb.Message.toObjectList(msg.getCommentRecordTypesList(),
    dlkit_primordium_type_primitives_pb.Type.toObject, includeInstance),
    referenceId: (f = msg.getReferenceId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForCreateRequest}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentFormForCreateRequest;
  return proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForCreateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForCreateRequest}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addCommentRecordTypes(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setReferenceId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForCreateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
  f = message.getReferenceId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type comment_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.getCommentRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.setCommentRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.addCommentRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.clearCommentRecordTypesList = function() {
  this.setCommentRecordTypesList([]);
};


/**
 * optional dlkit.primordium.id.primitives.Id reference_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.getReferenceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.setReferenceId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.clearReferenceId = function() {
  this.setReferenceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentFormForCreateRequest.prototype.hasReferenceId = function() {
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
proto.dlkit.proto.commenting.CreateCommentReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CreateCommentReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CreateCommentReply.displayName = 'proto.dlkit.proto.commenting.CreateCommentReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CreateCommentReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CreateCommentReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CreateCommentReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateCommentReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    comment: (f = msg.getComment()) && proto.dlkit.proto.commenting.Comment.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CreateCommentReply}
 */
proto.dlkit.proto.commenting.CreateCommentReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CreateCommentReply;
  return proto.dlkit.proto.commenting.CreateCommentReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CreateCommentReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CreateCommentReply}
 */
proto.dlkit.proto.commenting.CreateCommentReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.Comment;
      reader.readMessage(value,proto.dlkit.proto.commenting.Comment.deserializeBinaryFromReader);
      msg.setComment(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CreateCommentReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CreateCommentReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CreateCommentReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateCommentReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getComment();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.Comment.serializeBinaryToWriter
    );
  }
};


/**
 * optional Comment comment = 1;
 * @return {?proto.dlkit.proto.commenting.Comment}
 */
proto.dlkit.proto.commenting.CreateCommentReply.prototype.getComment = function() {
  return /** @type{?proto.dlkit.proto.commenting.Comment} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.Comment, 1));
};


/** @param {?proto.dlkit.proto.commenting.Comment|undefined} value */
proto.dlkit.proto.commenting.CreateCommentReply.prototype.setComment = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.CreateCommentReply.prototype.clearComment = function() {
  this.setComment(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.CreateCommentReply.prototype.hasComment = function() {
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
proto.dlkit.proto.commenting.CreateCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CreateCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CreateCommentRequest.displayName = 'proto.dlkit.proto.commenting.CreateCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CreateCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CreateCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CreateCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentForm: (f = msg.getCommentForm()) && proto.dlkit.proto.commenting.CommentForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CreateCommentRequest}
 */
proto.dlkit.proto.commenting.CreateCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CreateCommentRequest;
  return proto.dlkit.proto.commenting.CreateCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CreateCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CreateCommentRequest}
 */
proto.dlkit.proto.commenting.CreateCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.CommentForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.CommentForm.deserializeBinaryFromReader);
      msg.setCommentForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CreateCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CreateCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CreateCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.CommentForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CommentForm comment_form = 1;
 * @return {?proto.dlkit.proto.commenting.CommentForm}
 */
proto.dlkit.proto.commenting.CreateCommentRequest.prototype.getCommentForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.CommentForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.CommentForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.CommentForm|undefined} value */
proto.dlkit.proto.commenting.CreateCommentRequest.prototype.setCommentForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.CreateCommentRequest.prototype.clearCommentForm = function() {
  this.setCommentForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.CreateCommentRequest.prototype.hasCommentForm = function() {
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
proto.dlkit.proto.commenting.CanUpdateCommentsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanUpdateCommentsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanUpdateCommentsReply.displayName = 'proto.dlkit.proto.commenting.CanUpdateCommentsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanUpdateCommentsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanUpdateCommentsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canUpdateComments: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanUpdateCommentsReply}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanUpdateCommentsReply;
  return proto.dlkit.proto.commenting.CanUpdateCommentsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanUpdateCommentsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanUpdateCommentsReply}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanUpdateComments(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanUpdateCommentsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanUpdateCommentsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanUpdateComments();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_update_comments = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.prototype.getCanUpdateComments = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanUpdateCommentsReply.prototype.setCanUpdateComments = function(value) {
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
proto.dlkit.proto.commenting.CanUpdateCommentsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanUpdateCommentsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanUpdateCommentsRequest.displayName = 'proto.dlkit.proto.commenting.CanUpdateCommentsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanUpdateCommentsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanUpdateCommentsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateCommentsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanUpdateCommentsRequest}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanUpdateCommentsRequest;
  return proto.dlkit.proto.commenting.CanUpdateCommentsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanUpdateCommentsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanUpdateCommentsRequest}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanUpdateCommentsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanUpdateCommentsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanUpdateCommentsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateCommentsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentFormForUpdateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.displayName = 'proto.dlkit.proto.commenting.GetCommentFormForUpdateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForUpdateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentForm: (f = msg.getCommentForm()) && proto.dlkit.proto.commenting.CommentForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForUpdateReply}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentFormForUpdateReply;
  return proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForUpdateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForUpdateReply}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.CommentForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.CommentForm.deserializeBinaryFromReader);
      msg.setCommentForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForUpdateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.CommentForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CommentForm comment_form = 1;
 * @return {?proto.dlkit.proto.commenting.CommentForm}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.prototype.getCommentForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.CommentForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.CommentForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.CommentForm|undefined} value */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.prototype.setCommentForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.prototype.clearCommentForm = function() {
  this.setCommentForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateReply.prototype.hasCommentForm = function() {
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
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest;
  return proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentFormForUpdateRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.UpdateCommentReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UpdateCommentReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UpdateCommentReply.displayName = 'proto.dlkit.proto.commenting.UpdateCommentReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UpdateCommentReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UpdateCommentReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UpdateCommentReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateCommentReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UpdateCommentReply}
 */
proto.dlkit.proto.commenting.UpdateCommentReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UpdateCommentReply;
  return proto.dlkit.proto.commenting.UpdateCommentReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UpdateCommentReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UpdateCommentReply}
 */
proto.dlkit.proto.commenting.UpdateCommentReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UpdateCommentReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UpdateCommentReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UpdateCommentReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateCommentReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UpdateCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UpdateCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UpdateCommentRequest.displayName = 'proto.dlkit.proto.commenting.UpdateCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UpdateCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UpdateCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentForm: (f = msg.getCommentForm()) && proto.dlkit.proto.commenting.CommentForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UpdateCommentRequest}
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UpdateCommentRequest;
  return proto.dlkit.proto.commenting.UpdateCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UpdateCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UpdateCommentRequest}
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.CommentForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.CommentForm.deserializeBinaryFromReader);
      msg.setCommentForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UpdateCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UpdateCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.CommentForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional CommentForm comment_form = 1;
 * @return {?proto.dlkit.proto.commenting.CommentForm}
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.prototype.getCommentForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.CommentForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.CommentForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.CommentForm|undefined} value */
proto.dlkit.proto.commenting.UpdateCommentRequest.prototype.setCommentForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.UpdateCommentRequest.prototype.clearCommentForm = function() {
  this.setCommentForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.UpdateCommentRequest.prototype.hasCommentForm = function() {
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
proto.dlkit.proto.commenting.CanDeleteCommentsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanDeleteCommentsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanDeleteCommentsReply.displayName = 'proto.dlkit.proto.commenting.CanDeleteCommentsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanDeleteCommentsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanDeleteCommentsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canDeleteComments: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanDeleteCommentsReply}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanDeleteCommentsReply;
  return proto.dlkit.proto.commenting.CanDeleteCommentsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanDeleteCommentsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanDeleteCommentsReply}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanDeleteComments(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanDeleteCommentsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanDeleteCommentsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanDeleteComments();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_delete_comments = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.prototype.getCanDeleteComments = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanDeleteCommentsReply.prototype.setCanDeleteComments = function(value) {
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
proto.dlkit.proto.commenting.CanDeleteCommentsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanDeleteCommentsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanDeleteCommentsRequest.displayName = 'proto.dlkit.proto.commenting.CanDeleteCommentsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanDeleteCommentsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanDeleteCommentsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteCommentsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanDeleteCommentsRequest}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanDeleteCommentsRequest;
  return proto.dlkit.proto.commenting.CanDeleteCommentsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanDeleteCommentsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanDeleteCommentsRequest}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanDeleteCommentsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanDeleteCommentsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanDeleteCommentsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteCommentsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.DeleteCommentReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.DeleteCommentReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.DeleteCommentReply.displayName = 'proto.dlkit.proto.commenting.DeleteCommentReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.DeleteCommentReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.DeleteCommentReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.DeleteCommentReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteCommentReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.DeleteCommentReply}
 */
proto.dlkit.proto.commenting.DeleteCommentReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.DeleteCommentReply;
  return proto.dlkit.proto.commenting.DeleteCommentReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.DeleteCommentReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.DeleteCommentReply}
 */
proto.dlkit.proto.commenting.DeleteCommentReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.DeleteCommentReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.DeleteCommentReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.DeleteCommentReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteCommentReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.DeleteCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.DeleteCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.DeleteCommentRequest.displayName = 'proto.dlkit.proto.commenting.DeleteCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.DeleteCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.DeleteCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.DeleteCommentRequest}
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.DeleteCommentRequest;
  return proto.dlkit.proto.commenting.DeleteCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.DeleteCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.DeleteCommentRequest}
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.DeleteCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.DeleteCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.DeleteCommentRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.DeleteCommentRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.DeleteCommentRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.CanManageCommentAliasesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanManageCommentAliasesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanManageCommentAliasesReply.displayName = 'proto.dlkit.proto.commenting.CanManageCommentAliasesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanManageCommentAliasesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanManageCommentAliasesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canManageCommentAliases: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanManageCommentAliasesReply}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanManageCommentAliasesReply;
  return proto.dlkit.proto.commenting.CanManageCommentAliasesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanManageCommentAliasesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanManageCommentAliasesReply}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanManageCommentAliases(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanManageCommentAliasesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanManageCommentAliasesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanManageCommentAliases();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_manage_comment_aliases = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.prototype.getCanManageCommentAliases = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanManageCommentAliasesReply.prototype.setCanManageCommentAliases = function(value) {
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
proto.dlkit.proto.commenting.CanManageCommentAliasesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanManageCommentAliasesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.displayName = 'proto.dlkit.proto.commenting.CanManageCommentAliasesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanManageCommentAliasesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanManageCommentAliasesRequest}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanManageCommentAliasesRequest;
  return proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanManageCommentAliasesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanManageCommentAliasesRequest}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanManageCommentAliasesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageCommentAliasesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AliasCommentReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AliasCommentReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AliasCommentReply.displayName = 'proto.dlkit.proto.commenting.AliasCommentReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AliasCommentReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AliasCommentReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AliasCommentReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasCommentReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AliasCommentReply}
 */
proto.dlkit.proto.commenting.AliasCommentReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AliasCommentReply;
  return proto.dlkit.proto.commenting.AliasCommentReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AliasCommentReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AliasCommentReply}
 */
proto.dlkit.proto.commenting.AliasCommentReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AliasCommentReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AliasCommentReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AliasCommentReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasCommentReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AliasCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AliasCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AliasCommentRequest.displayName = 'proto.dlkit.proto.commenting.AliasCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AliasCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AliasCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    aliasId: (f = msg.getAliasId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AliasCommentRequest}
 */
proto.dlkit.proto.commenting.AliasCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AliasCommentRequest;
  return proto.dlkit.proto.commenting.AliasCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AliasCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AliasCommentRequest}
 */
proto.dlkit.proto.commenting.AliasCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AliasCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AliasCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAliasId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getCommentId();
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
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.getAliasId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.setAliasId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.AliasCommentRequest.prototype.clearAliasId = function() {
  this.setAliasId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.hasAliasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.AliasCommentRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AliasCommentRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.displayName = 'proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupCommentBookMappings: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply;
  return proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupCommentBookMappings(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupCommentBookMappings();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_comment_book_mappings = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.prototype.getCanLookupCommentBookMappings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsReply.prototype.setCanLookupCommentBookMappings = function(value) {
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
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.displayName = 'proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest;
  return proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupCommentBookMappingsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseComparativeBookViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseComparativeBookViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseComparativeBookViewReply.displayName = 'proto.dlkit.proto.commenting.UseComparativeBookViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseComparativeBookViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseComparativeBookViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeBookViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseComparativeBookViewReply}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseComparativeBookViewReply;
  return proto.dlkit.proto.commenting.UseComparativeBookViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseComparativeBookViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseComparativeBookViewReply}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseComparativeBookViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseComparativeBookViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeBookViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UseComparativeBookViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UseComparativeBookViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UseComparativeBookViewRequest.displayName = 'proto.dlkit.proto.commenting.UseComparativeBookViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UseComparativeBookViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UseComparativeBookViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeBookViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UseComparativeBookViewRequest}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UseComparativeBookViewRequest;
  return proto.dlkit.proto.commenting.UseComparativeBookViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UseComparativeBookViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UseComparativeBookViewRequest}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UseComparativeBookViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UseComparativeBookViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UseComparativeBookViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UseComparativeBookViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UsePlenaryBookViewReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UsePlenaryBookViewReply.displayName = 'proto.dlkit.proto.commenting.UsePlenaryBookViewReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UsePlenaryBookViewReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UsePlenaryBookViewReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryBookViewReply}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UsePlenaryBookViewReply;
  return proto.dlkit.proto.commenting.UsePlenaryBookViewReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryBookViewReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryBookViewReply}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UsePlenaryBookViewReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryBookViewReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UsePlenaryBookViewRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.displayName = 'proto.dlkit.proto.commenting.UsePlenaryBookViewRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UsePlenaryBookViewRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryBookViewRequest}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UsePlenaryBookViewRequest;
  return proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryBookViewRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UsePlenaryBookViewRequest}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UsePlenaryBookViewRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UsePlenaryBookViewRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentIdsByBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentIdsByBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentIdsByBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentIdsByBookRequest}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentIdsByBookRequest;
  return proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentIdsByBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentIdsByBookRequest}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentIdsByBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBookRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.GetCommentsByBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByBookRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByBookRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByBookRequest;
  return proto.dlkit.proto.commenting.GetCommentsByBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByBookRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetCommentsByBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetCommentsByBookRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookIdsList: jspb.Message.toObjectList(msg.getBookIdsList(),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest;
  return proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addBookIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id book_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.prototype.getBookIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.prototype.setBookIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.prototype.addBookIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.commenting.GetCommentIdsByBooksRequest.prototype.clearBookIdsList = function() {
  this.setBookIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.GetCommentsByBooksRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetCommentsByBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetCommentsByBooksRequest.displayName = 'proto.dlkit.proto.commenting.GetCommentsByBooksRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetCommentsByBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetCommentsByBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookIdsList: jspb.Message.toObjectList(msg.getBookIdsList(),
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
 * @return {!proto.dlkit.proto.commenting.GetCommentsByBooksRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetCommentsByBooksRequest;
  return proto.dlkit.proto.commenting.GetCommentsByBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetCommentsByBooksRequest}
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addBookIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetCommentsByBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetCommentsByBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id book_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.prototype.getBookIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.prototype.setBookIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetCommentsByBooksRequest.prototype.addBookIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.commenting.GetCommentsByBooksRequest.prototype.clearBookIdsList = function() {
  this.setBookIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookIdsByCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.displayName = 'proto.dlkit.proto.commenting.GetBookIdsByCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookIdsByCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookIdsByCommentRequest}
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookIdsByCommentRequest;
  return proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookIdsByCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookIdsByCommentRequest}
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookIdsByCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookIdsByCommentRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.GetBooksByCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBooksByCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBooksByCommentRequest.displayName = 'proto.dlkit.proto.commenting.GetBooksByCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBooksByCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBooksByCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBooksByCommentRequest}
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBooksByCommentRequest;
  return proto.dlkit.proto.commenting.GetBooksByCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBooksByCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBooksByCommentRequest}
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBooksByCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBooksByCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBooksByCommentRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBooksByCommentRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.CanAssignCommentsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanAssignCommentsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanAssignCommentsReply.displayName = 'proto.dlkit.proto.commenting.CanAssignCommentsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanAssignCommentsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanAssignCommentsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAssignComments: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsReply}
 */
proto.dlkit.proto.commenting.CanAssignCommentsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanAssignCommentsReply;
  return proto.dlkit.proto.commenting.CanAssignCommentsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsReply}
 */
proto.dlkit.proto.commenting.CanAssignCommentsReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAssignComments(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanAssignCommentsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanAssignCommentsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAssignComments();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_assign_comments = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanAssignCommentsReply.prototype.getCanAssignComments = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanAssignCommentsReply.prototype.setCanAssignComments = function(value) {
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
proto.dlkit.proto.commenting.CanAssignCommentsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanAssignCommentsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanAssignCommentsRequest.displayName = 'proto.dlkit.proto.commenting.CanAssignCommentsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanAssignCommentsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanAssignCommentsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsRequest}
 */
proto.dlkit.proto.commenting.CanAssignCommentsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanAssignCommentsRequest;
  return proto.dlkit.proto.commenting.CanAssignCommentsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsRequest}
 */
proto.dlkit.proto.commenting.CanAssignCommentsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanAssignCommentsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanAssignCommentsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanAssignCommentsToBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.displayName = 'proto.dlkit.proto.commenting.CanAssignCommentsToBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsToBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAssignCommentsToBook: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsToBookReply}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanAssignCommentsToBookReply;
  return proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsToBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsToBookReply}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAssignCommentsToBook(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsToBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAssignCommentsToBook();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_assign_comments_to_book = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.prototype.getCanAssignCommentsToBook = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanAssignCommentsToBookReply.prototype.setCanAssignCommentsToBook = function(value) {
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
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.displayName = 'proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest;
  return proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.CanAssignCommentsToBookRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetAssignableBookIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.displayName = 'proto.dlkit.proto.commenting.GetAssignableBookIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetAssignableBookIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetAssignableBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetAssignableBookIdsRequest;
  return proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetAssignableBookIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetAssignableBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetAssignableBookIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.displayName = 'proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest;
  return proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetAssignableBookIdsForCommentRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.AssignCommentToBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AssignCommentToBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AssignCommentToBookReply.displayName = 'proto.dlkit.proto.commenting.AssignCommentToBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AssignCommentToBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AssignCommentToBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AssignCommentToBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AssignCommentToBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AssignCommentToBookReply}
 */
proto.dlkit.proto.commenting.AssignCommentToBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AssignCommentToBookReply;
  return proto.dlkit.proto.commenting.AssignCommentToBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AssignCommentToBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AssignCommentToBookReply}
 */
proto.dlkit.proto.commenting.AssignCommentToBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AssignCommentToBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AssignCommentToBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AssignCommentToBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AssignCommentToBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AssignCommentToBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AssignCommentToBookRequest.displayName = 'proto.dlkit.proto.commenting.AssignCommentToBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AssignCommentToBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AssignCommentToBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AssignCommentToBookRequest}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AssignCommentToBookRequest;
  return proto.dlkit.proto.commenting.AssignCommentToBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AssignCommentToBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AssignCommentToBookRequest}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AssignCommentToBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AssignCommentToBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AssignCommentToBookRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.UnassignCommentFromBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UnassignCommentFromBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UnassignCommentFromBookReply.displayName = 'proto.dlkit.proto.commenting.UnassignCommentFromBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UnassignCommentFromBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UnassignCommentFromBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UnassignCommentFromBookReply}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UnassignCommentFromBookReply;
  return proto.dlkit.proto.commenting.UnassignCommentFromBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UnassignCommentFromBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UnassignCommentFromBookReply}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UnassignCommentFromBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UnassignCommentFromBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UnassignCommentFromBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.displayName = 'proto.dlkit.proto.commenting.UnassignCommentFromBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UnassignCommentFromBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UnassignCommentFromBookRequest}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UnassignCommentFromBookRequest;
  return proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UnassignCommentFromBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UnassignCommentFromBookRequest}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UnassignCommentFromBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.UnassignCommentFromBookRequest.prototype.hasCommentId = function() {
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
proto.dlkit.proto.commenting.ReassignCommentToBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.ReassignCommentToBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.ReassignCommentToBookReply.displayName = 'proto.dlkit.proto.commenting.ReassignCommentToBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.ReassignCommentToBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.ReassignCommentToBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.ReassignCommentToBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.ReassignCommentToBookReply}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.ReassignCommentToBookReply;
  return proto.dlkit.proto.commenting.ReassignCommentToBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.ReassignCommentToBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.ReassignCommentToBookReply}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.ReassignCommentToBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.ReassignCommentToBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.ReassignCommentToBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.ReassignCommentToBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.ReassignCommentToBookRequest.displayName = 'proto.dlkit.proto.commenting.ReassignCommentToBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.ReassignCommentToBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.ReassignCommentToBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    commentId: (f = msg.getCommentId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    fromBookId: (f = msg.getFromBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    toBookId: (f = msg.getToBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.ReassignCommentToBookRequest}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.ReassignCommentToBookRequest;
  return proto.dlkit.proto.commenting.ReassignCommentToBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.ReassignCommentToBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.ReassignCommentToBookRequest}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setCommentId(value);
      break;
    case 2:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setFromBookId(value);
      break;
    case 3:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setToBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.ReassignCommentToBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.ReassignCommentToBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCommentId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getFromBookId();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getToBookId();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id comment_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.getCommentId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.setCommentId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.clearCommentId = function() {
  this.setCommentId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.hasCommentId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id from_book_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.getFromBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.setFromBookId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.clearFromBookId = function() {
  this.setFromBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.hasFromBookId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id to_book_id = 3;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.getToBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 3));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.setToBookId = function(value) {
  jspb.Message.setWrapperField(this, 3, value);
};


proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.clearToBookId = function() {
  this.setToBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.ReassignCommentToBookRequest.prototype.hasToBookId = function() {
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
proto.dlkit.proto.commenting.CanLookupBooksReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanLookupBooksReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanLookupBooksReply.displayName = 'proto.dlkit.proto.commenting.CanLookupBooksReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanLookupBooksReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanLookupBooksReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanLookupBooksReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupBooksReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canLookupBooks: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanLookupBooksReply}
 */
proto.dlkit.proto.commenting.CanLookupBooksReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanLookupBooksReply;
  return proto.dlkit.proto.commenting.CanLookupBooksReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanLookupBooksReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanLookupBooksReply}
 */
proto.dlkit.proto.commenting.CanLookupBooksReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanLookupBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanLookupBooksReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanLookupBooksReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanLookupBooksReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupBooksReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanLookupBooks();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_lookup_books = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanLookupBooksReply.prototype.getCanLookupBooks = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanLookupBooksReply.prototype.setCanLookupBooks = function(value) {
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
proto.dlkit.proto.commenting.CanLookupBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanLookupBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanLookupBooksRequest.displayName = 'proto.dlkit.proto.commenting.CanLookupBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanLookupBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanLookupBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanLookupBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanLookupBooksRequest}
 */
proto.dlkit.proto.commenting.CanLookupBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanLookupBooksRequest;
  return proto.dlkit.proto.commenting.CanLookupBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanLookupBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanLookupBooksRequest}
 */
proto.dlkit.proto.commenting.CanLookupBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanLookupBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanLookupBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanLookupBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanLookupBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.GetBooksByIdsRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBooksByIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBooksByIdsRequest.displayName = 'proto.dlkit.proto.commenting.GetBooksByIdsRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBooksByIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBooksByIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookIdsList: jspb.Message.toObjectList(msg.getBookIdsList(),
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
 * @return {!proto.dlkit.proto.commenting.GetBooksByIdsRequest}
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBooksByIdsRequest;
  return proto.dlkit.proto.commenting.GetBooksByIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBooksByIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBooksByIdsRequest}
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.addBookIds(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBooksByIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBooksByIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookIdsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.id.primitives.Id book_ids = 1;
 * @return {!Array.<!proto.dlkit.primordium.id.primitives.Id>}
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.prototype.getBookIdsList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.id.primitives.Id>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.id.primitives.Id>} value */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.prototype.setBookIdsList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.id.primitives.Id=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetBooksByIdsRequest.prototype.addBookIds = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.id.primitives.Id, opt_index);
};


proto.dlkit.proto.commenting.GetBooksByIdsRequest.prototype.clearBookIdsList = function() {
  this.setBookIdsList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.displayName = 'proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookGenusType: (f = msg.getBookGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest;
  return proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setBookGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type book_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.prototype.getBookGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.prototype.setBookGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.prototype.clearBookGenusType = function() {
  this.setBookGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBooksByGenusTypeRequest.prototype.hasBookGenusType = function() {
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
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.displayName = 'proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookGenusType: (f = msg.getBookGenusType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest;
  return proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest}
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setBookGenusType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookGenusType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type book_genus_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.prototype.getBookGenusType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.prototype.setBookGenusType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.prototype.clearBookGenusType = function() {
  this.setBookGenusType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBooksByParentGenusTypeRequest.prototype.hasBookGenusType = function() {
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
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.displayName = 'proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookRecordType: (f = msg.getBookRecordType()) && dlkit_primordium_type_primitives_pb.Type.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest}
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest;
  return proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest}
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.setBookRecordType(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookRecordType();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.type.primitives.Type book_record_type = 1;
 * @return {?proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.prototype.getBookRecordType = function() {
  return /** @type{?proto.dlkit.primordium.type.primitives.Type} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {?proto.dlkit.primordium.type.primitives.Type|undefined} value */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.prototype.setBookRecordType = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.prototype.clearBookRecordType = function() {
  this.setBookRecordType(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBooksByRecordTypeRequest.prototype.hasBookRecordType = function() {
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
proto.dlkit.proto.commenting.GetBooksByProviderRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBooksByProviderRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBooksByProviderRequest.displayName = 'proto.dlkit.proto.commenting.GetBooksByProviderRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBooksByProviderRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBooksByProviderRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBooksByProviderRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByProviderRequest.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.GetBooksByProviderRequest}
 */
proto.dlkit.proto.commenting.GetBooksByProviderRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBooksByProviderRequest;
  return proto.dlkit.proto.commenting.GetBooksByProviderRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBooksByProviderRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBooksByProviderRequest}
 */
proto.dlkit.proto.commenting.GetBooksByProviderRequest.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.GetBooksByProviderRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBooksByProviderRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBooksByProviderRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksByProviderRequest.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.GetBooksByProviderRequest.prototype.getResourceId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBooksByProviderRequest.prototype.setResourceId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBooksByProviderRequest.prototype.clearResourceId = function() {
  this.setResourceId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBooksByProviderRequest.prototype.hasResourceId = function() {
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
proto.dlkit.proto.commenting.GetBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBooksRequest.displayName = 'proto.dlkit.proto.commenting.GetBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBooksRequest}
 */
proto.dlkit.proto.commenting.GetBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBooksRequest;
  return proto.dlkit.proto.commenting.GetBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBooksRequest}
 */
proto.dlkit.proto.commenting.GetBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CanCreateBooksReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateBooksReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateBooksReply.displayName = 'proto.dlkit.proto.commenting.CanCreateBooksReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateBooksReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateBooksReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateBooksReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBooksReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateBooks: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanCreateBooksReply}
 */
proto.dlkit.proto.commenting.CanCreateBooksReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateBooksReply;
  return proto.dlkit.proto.commenting.CanCreateBooksReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateBooksReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateBooksReply}
 */
proto.dlkit.proto.commenting.CanCreateBooksReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateBooksReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateBooksReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateBooksReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBooksReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateBooks();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_books = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanCreateBooksReply.prototype.getCanCreateBooks = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanCreateBooksReply.prototype.setCanCreateBooks = function(value) {
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
proto.dlkit.proto.commenting.CanCreateBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateBooksRequest.displayName = 'proto.dlkit.proto.commenting.CanCreateBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanCreateBooksRequest}
 */
proto.dlkit.proto.commenting.CanCreateBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateBooksRequest;
  return proto.dlkit.proto.commenting.CanCreateBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateBooksRequest}
 */
proto.dlkit.proto.commenting.CanCreateBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.displayName = 'proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canCreateBookWithRecordTypes: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply;
  return proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanCreateBookWithRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanCreateBookWithRecordTypes();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_create_book_with_record_types = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.prototype.getCanCreateBookWithRecordTypes = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesReply.prototype.setCanCreateBookWithRecordTypes = function(value) {
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
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.displayName = 'proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookRecordTypesList: jspb.Message.toObjectList(msg.getBookRecordTypesList(),
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
 * @return {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest;
  return proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addBookRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type book_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.prototype.getBookRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.prototype.setBookRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.prototype.addBookRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.commenting.CanCreateBookWithRecordTypesRequest.prototype.clearBookRecordTypesList = function() {
  this.setBookRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookFormForCreateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookFormForCreateReply.displayName = 'proto.dlkit.proto.commenting.GetBookFormForCreateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookFormForCreateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookFormForCreateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookForm: (f = msg.getBookForm()) && proto.dlkit.proto.commenting.BookForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookFormForCreateReply}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookFormForCreateReply;
  return proto.dlkit.proto.commenting.GetBookFormForCreateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForCreateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookFormForCreateReply}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.BookForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.BookForm.deserializeBinaryFromReader);
      msg.setBookForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookFormForCreateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForCreateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.BookForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional BookForm book_form = 1;
 * @return {?proto.dlkit.proto.commenting.BookForm}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.prototype.getBookForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.BookForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.BookForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.BookForm|undefined} value */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.prototype.setBookForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookFormForCreateReply.prototype.clearBookForm = function() {
  this.setBookForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateReply.prototype.hasBookForm = function() {
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
proto.dlkit.proto.commenting.GetBookFormForCreateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.dlkit.proto.commenting.GetBookFormForCreateRequest.repeatedFields_, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookFormForCreateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookFormForCreateRequest.displayName = 'proto.dlkit.proto.commenting.GetBookFormForCreateRequest';
}
/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookFormForCreateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookFormForCreateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookRecordTypesList: jspb.Message.toObjectList(msg.getBookRecordTypesList(),
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
 * @return {!proto.dlkit.proto.commenting.GetBookFormForCreateRequest}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookFormForCreateRequest;
  return proto.dlkit.proto.commenting.GetBookFormForCreateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForCreateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookFormForCreateRequest}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_type_primitives_pb.Type;
      reader.readMessage(value,dlkit_primordium_type_primitives_pb.Type.deserializeBinaryFromReader);
      msg.addBookRecordTypes(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookFormForCreateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForCreateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookRecordTypesList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      dlkit_primordium_type_primitives_pb.Type.serializeBinaryToWriter
    );
  }
};


/**
 * repeated dlkit.primordium.type.primitives.Type book_record_types = 1;
 * @return {!Array.<!proto.dlkit.primordium.type.primitives.Type>}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.prototype.getBookRecordTypesList = function() {
  return /** @type{!Array.<!proto.dlkit.primordium.type.primitives.Type>} */ (
    jspb.Message.getRepeatedWrapperField(this, dlkit_primordium_type_primitives_pb.Type, 1));
};


/** @param {!Array.<!proto.dlkit.primordium.type.primitives.Type>} value */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.prototype.setBookRecordTypesList = function(value) {
  jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.dlkit.primordium.type.primitives.Type=} opt_value
 * @param {number=} opt_index
 * @return {!proto.dlkit.primordium.type.primitives.Type}
 */
proto.dlkit.proto.commenting.GetBookFormForCreateRequest.prototype.addBookRecordTypes = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.dlkit.primordium.type.primitives.Type, opt_index);
};


proto.dlkit.proto.commenting.GetBookFormForCreateRequest.prototype.clearBookRecordTypesList = function() {
  this.setBookRecordTypesList([]);
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CreateBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CreateBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CreateBookReply.displayName = 'proto.dlkit.proto.commenting.CreateBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CreateBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CreateBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CreateBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    book: (f = msg.getBook()) && proto.dlkit.proto.commenting.Book.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CreateBookReply}
 */
proto.dlkit.proto.commenting.CreateBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CreateBookReply;
  return proto.dlkit.proto.commenting.CreateBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CreateBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CreateBookReply}
 */
proto.dlkit.proto.commenting.CreateBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.Book;
      reader.readMessage(value,proto.dlkit.proto.commenting.Book.deserializeBinaryFromReader);
      msg.setBook(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CreateBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CreateBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CreateBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBook();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.Book.serializeBinaryToWriter
    );
  }
};


/**
 * optional Book book = 1;
 * @return {?proto.dlkit.proto.commenting.Book}
 */
proto.dlkit.proto.commenting.CreateBookReply.prototype.getBook = function() {
  return /** @type{?proto.dlkit.proto.commenting.Book} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.Book, 1));
};


/** @param {?proto.dlkit.proto.commenting.Book|undefined} value */
proto.dlkit.proto.commenting.CreateBookReply.prototype.setBook = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.CreateBookReply.prototype.clearBook = function() {
  this.setBook(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.CreateBookReply.prototype.hasBook = function() {
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
proto.dlkit.proto.commenting.CreateBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CreateBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CreateBookRequest.displayName = 'proto.dlkit.proto.commenting.CreateBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CreateBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CreateBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CreateBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookForm: (f = msg.getBookForm()) && proto.dlkit.proto.commenting.BookForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CreateBookRequest}
 */
proto.dlkit.proto.commenting.CreateBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CreateBookRequest;
  return proto.dlkit.proto.commenting.CreateBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CreateBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CreateBookRequest}
 */
proto.dlkit.proto.commenting.CreateBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.BookForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.BookForm.deserializeBinaryFromReader);
      msg.setBookForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CreateBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CreateBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CreateBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CreateBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.BookForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional BookForm book_form = 1;
 * @return {?proto.dlkit.proto.commenting.BookForm}
 */
proto.dlkit.proto.commenting.CreateBookRequest.prototype.getBookForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.BookForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.BookForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.BookForm|undefined} value */
proto.dlkit.proto.commenting.CreateBookRequest.prototype.setBookForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.CreateBookRequest.prototype.clearBookForm = function() {
  this.setBookForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.CreateBookRequest.prototype.hasBookForm = function() {
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
proto.dlkit.proto.commenting.CanUpdateBooksReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanUpdateBooksReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanUpdateBooksReply.displayName = 'proto.dlkit.proto.commenting.CanUpdateBooksReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanUpdateBooksReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanUpdateBooksReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanUpdateBooksReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateBooksReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canUpdateBooks: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanUpdateBooksReply}
 */
proto.dlkit.proto.commenting.CanUpdateBooksReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanUpdateBooksReply;
  return proto.dlkit.proto.commenting.CanUpdateBooksReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanUpdateBooksReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanUpdateBooksReply}
 */
proto.dlkit.proto.commenting.CanUpdateBooksReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanUpdateBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanUpdateBooksReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanUpdateBooksReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanUpdateBooksReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateBooksReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanUpdateBooks();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_update_books = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanUpdateBooksReply.prototype.getCanUpdateBooks = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanUpdateBooksReply.prototype.setCanUpdateBooks = function(value) {
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
proto.dlkit.proto.commenting.CanUpdateBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanUpdateBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanUpdateBooksRequest.displayName = 'proto.dlkit.proto.commenting.CanUpdateBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanUpdateBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanUpdateBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanUpdateBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanUpdateBooksRequest}
 */
proto.dlkit.proto.commenting.CanUpdateBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanUpdateBooksRequest;
  return proto.dlkit.proto.commenting.CanUpdateBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanUpdateBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanUpdateBooksRequest}
 */
proto.dlkit.proto.commenting.CanUpdateBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanUpdateBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanUpdateBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanUpdateBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanUpdateBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookFormForUpdateReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookFormForUpdateReply.displayName = 'proto.dlkit.proto.commenting.GetBookFormForUpdateReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookFormForUpdateReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookFormForUpdateReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookForm: (f = msg.getBookForm()) && proto.dlkit.proto.commenting.BookForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookFormForUpdateReply}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookFormForUpdateReply;
  return proto.dlkit.proto.commenting.GetBookFormForUpdateReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForUpdateReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookFormForUpdateReply}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.BookForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.BookForm.deserializeBinaryFromReader);
      msg.setBookForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookFormForUpdateReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForUpdateReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.BookForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional BookForm book_form = 1;
 * @return {?proto.dlkit.proto.commenting.BookForm}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.prototype.getBookForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.BookForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.BookForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.BookForm|undefined} value */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.prototype.setBookForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookFormForUpdateReply.prototype.clearBookForm = function() {
  this.setBookForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateReply.prototype.hasBookForm = function() {
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
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookFormForUpdateRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.displayName = 'proto.dlkit.proto.commenting.GetBookFormForUpdateRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookFormForUpdateRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookFormForUpdateRequest}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookFormForUpdateRequest;
  return proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForUpdateRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookFormForUpdateRequest}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookFormForUpdateRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookFormForUpdateRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.UpdateBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UpdateBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UpdateBookReply.displayName = 'proto.dlkit.proto.commenting.UpdateBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UpdateBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UpdateBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UpdateBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UpdateBookReply}
 */
proto.dlkit.proto.commenting.UpdateBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UpdateBookReply;
  return proto.dlkit.proto.commenting.UpdateBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UpdateBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UpdateBookReply}
 */
proto.dlkit.proto.commenting.UpdateBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UpdateBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UpdateBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UpdateBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.UpdateBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.UpdateBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.UpdateBookRequest.displayName = 'proto.dlkit.proto.commenting.UpdateBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.UpdateBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.UpdateBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.UpdateBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookForm: (f = msg.getBookForm()) && proto.dlkit.proto.commenting.BookForm.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.UpdateBookRequest}
 */
proto.dlkit.proto.commenting.UpdateBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.UpdateBookRequest;
  return proto.dlkit.proto.commenting.UpdateBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.UpdateBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.UpdateBookRequest}
 */
proto.dlkit.proto.commenting.UpdateBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.BookForm;
      reader.readMessage(value,proto.dlkit.proto.commenting.BookForm.deserializeBinaryFromReader);
      msg.setBookForm(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.UpdateBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.UpdateBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.UpdateBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.UpdateBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookForm();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.BookForm.serializeBinaryToWriter
    );
  }
};


/**
 * optional BookForm book_form = 1;
 * @return {?proto.dlkit.proto.commenting.BookForm}
 */
proto.dlkit.proto.commenting.UpdateBookRequest.prototype.getBookForm = function() {
  return /** @type{?proto.dlkit.proto.commenting.BookForm} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.BookForm, 1));
};


/** @param {?proto.dlkit.proto.commenting.BookForm|undefined} value */
proto.dlkit.proto.commenting.UpdateBookRequest.prototype.setBookForm = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.UpdateBookRequest.prototype.clearBookForm = function() {
  this.setBookForm(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.UpdateBookRequest.prototype.hasBookForm = function() {
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
proto.dlkit.proto.commenting.CanDeleteBooksReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanDeleteBooksReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanDeleteBooksReply.displayName = 'proto.dlkit.proto.commenting.CanDeleteBooksReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanDeleteBooksReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanDeleteBooksReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanDeleteBooksReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteBooksReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canDeleteBooks: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanDeleteBooksReply}
 */
proto.dlkit.proto.commenting.CanDeleteBooksReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanDeleteBooksReply;
  return proto.dlkit.proto.commenting.CanDeleteBooksReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanDeleteBooksReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanDeleteBooksReply}
 */
proto.dlkit.proto.commenting.CanDeleteBooksReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanDeleteBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanDeleteBooksReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanDeleteBooksReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanDeleteBooksReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteBooksReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanDeleteBooks();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_delete_books = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanDeleteBooksReply.prototype.getCanDeleteBooks = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanDeleteBooksReply.prototype.setCanDeleteBooks = function(value) {
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
proto.dlkit.proto.commenting.CanDeleteBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanDeleteBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanDeleteBooksRequest.displayName = 'proto.dlkit.proto.commenting.CanDeleteBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanDeleteBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanDeleteBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanDeleteBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanDeleteBooksRequest}
 */
proto.dlkit.proto.commenting.CanDeleteBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanDeleteBooksRequest;
  return proto.dlkit.proto.commenting.CanDeleteBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanDeleteBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanDeleteBooksRequest}
 */
proto.dlkit.proto.commenting.CanDeleteBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanDeleteBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanDeleteBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanDeleteBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanDeleteBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.DeleteBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.DeleteBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.DeleteBookReply.displayName = 'proto.dlkit.proto.commenting.DeleteBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.DeleteBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.DeleteBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.DeleteBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.DeleteBookReply}
 */
proto.dlkit.proto.commenting.DeleteBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.DeleteBookReply;
  return proto.dlkit.proto.commenting.DeleteBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.DeleteBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.DeleteBookReply}
 */
proto.dlkit.proto.commenting.DeleteBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.DeleteBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.DeleteBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.DeleteBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.DeleteBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.DeleteBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.DeleteBookRequest.displayName = 'proto.dlkit.proto.commenting.DeleteBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.DeleteBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.DeleteBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.DeleteBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.DeleteBookRequest}
 */
proto.dlkit.proto.commenting.DeleteBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.DeleteBookRequest;
  return proto.dlkit.proto.commenting.DeleteBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.DeleteBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.DeleteBookRequest}
 */
proto.dlkit.proto.commenting.DeleteBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.DeleteBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.DeleteBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.DeleteBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.DeleteBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.DeleteBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.DeleteBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.DeleteBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.DeleteBookRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.CanManageBookAliasesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanManageBookAliasesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanManageBookAliasesReply.displayName = 'proto.dlkit.proto.commenting.CanManageBookAliasesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanManageBookAliasesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanManageBookAliasesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canManageBookAliases: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanManageBookAliasesReply}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanManageBookAliasesReply;
  return proto.dlkit.proto.commenting.CanManageBookAliasesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanManageBookAliasesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanManageBookAliasesReply}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanManageBookAliases(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanManageBookAliasesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanManageBookAliasesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanManageBookAliases();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_manage_book_aliases = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.prototype.getCanManageBookAliases = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanManageBookAliasesReply.prototype.setCanManageBookAliases = function(value) {
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
proto.dlkit.proto.commenting.CanManageBookAliasesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanManageBookAliasesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanManageBookAliasesRequest.displayName = 'proto.dlkit.proto.commenting.CanManageBookAliasesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanManageBookAliasesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanManageBookAliasesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageBookAliasesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanManageBookAliasesRequest}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanManageBookAliasesRequest;
  return proto.dlkit.proto.commenting.CanManageBookAliasesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanManageBookAliasesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanManageBookAliasesRequest}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanManageBookAliasesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanManageBookAliasesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanManageBookAliasesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanManageBookAliasesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AliasBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AliasBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AliasBookReply.displayName = 'proto.dlkit.proto.commenting.AliasBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AliasBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AliasBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AliasBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AliasBookReply}
 */
proto.dlkit.proto.commenting.AliasBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AliasBookReply;
  return proto.dlkit.proto.commenting.AliasBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AliasBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AliasBookReply}
 */
proto.dlkit.proto.commenting.AliasBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AliasBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AliasBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AliasBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AliasBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AliasBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AliasBookRequest.displayName = 'proto.dlkit.proto.commenting.AliasBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AliasBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AliasBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AliasBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    aliasId: (f = msg.getAliasId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AliasBookRequest}
 */
proto.dlkit.proto.commenting.AliasBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AliasBookRequest;
  return proto.dlkit.proto.commenting.AliasBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AliasBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AliasBookRequest}
 */
proto.dlkit.proto.commenting.AliasBookRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AliasBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AliasBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AliasBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AliasBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAliasId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
  f = message.getBookId();
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
proto.dlkit.proto.commenting.AliasBookRequest.prototype.getAliasId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AliasBookRequest.prototype.setAliasId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.AliasBookRequest.prototype.clearAliasId = function() {
  this.setAliasId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AliasBookRequest.prototype.hasAliasId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.AliasBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AliasBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.AliasBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AliasBookRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.GetBookHierarchyIdReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookHierarchyIdReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookHierarchyIdReply.displayName = 'proto.dlkit.proto.commenting.GetBookHierarchyIdReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookHierarchyIdReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyIdReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyIdReply}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookHierarchyIdReply;
  return proto.dlkit.proto.commenting.GetBookHierarchyIdReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyIdReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyIdReply}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookHierarchyIdReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyIdReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookHierarchyIdReply.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdReply.prototype.hasId = function() {
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
proto.dlkit.proto.commenting.GetBookHierarchyIdRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookHierarchyIdRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.displayName = 'proto.dlkit.proto.commenting.GetBookHierarchyIdRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyIdRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyIdRequest}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookHierarchyIdRequest;
  return proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyIdRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyIdRequest}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyIdRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyIdRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetBookHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookHierarchyReply.displayName = 'proto.dlkit.proto.commenting.GetBookHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyReply}
 */
proto.dlkit.proto.commenting.GetBookHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookHierarchyReply;
  return proto.dlkit.proto.commenting.GetBookHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyReply}
 */
proto.dlkit.proto.commenting.GetBookHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.GetBookHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.GetBookHierarchyReply.prototype.getHierarchy = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Hierarchy} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Hierarchy, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Hierarchy|undefined} value */
proto.dlkit.proto.commenting.GetBookHierarchyReply.prototype.setHierarchy = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookHierarchyReply.prototype.clearHierarchy = function() {
  this.setHierarchy(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookHierarchyReply.prototype.hasHierarchy = function() {
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
proto.dlkit.proto.commenting.GetBookHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookHierarchyRequest.displayName = 'proto.dlkit.proto.commenting.GetBookHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyRequest}
 */
proto.dlkit.proto.commenting.GetBookHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookHierarchyRequest;
  return proto.dlkit.proto.commenting.GetBookHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookHierarchyRequest}
 */
proto.dlkit.proto.commenting.GetBookHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanAccessBookHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.displayName = 'proto.dlkit.proto.commenting.CanAccessBookHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanAccessBookHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canAccessBookHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanAccessBookHierarchyReply}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanAccessBookHierarchyReply;
  return proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanAccessBookHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanAccessBookHierarchyReply}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanAccessBookHierarchy(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanAccessBookHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanAccessBookHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_access_book_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.prototype.getCanAccessBookHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanAccessBookHierarchyReply.prototype.setCanAccessBookHierarchy = function(value) {
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
proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.displayName = 'proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest;
  return proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanAccessBookHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetRootBookIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetRootBookIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetRootBookIdsRequest.displayName = 'proto.dlkit.proto.commenting.GetRootBookIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetRootBookIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetRootBookIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetRootBookIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetRootBookIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetRootBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetRootBookIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetRootBookIdsRequest;
  return proto.dlkit.proto.commenting.GetRootBookIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetRootBookIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetRootBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetRootBookIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetRootBookIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetRootBookIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetRootBookIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetRootBookIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.GetRootBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetRootBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetRootBooksRequest.displayName = 'proto.dlkit.proto.commenting.GetRootBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetRootBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetRootBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetRootBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetRootBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetRootBooksRequest}
 */
proto.dlkit.proto.commenting.GetRootBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetRootBooksRequest;
  return proto.dlkit.proto.commenting.GetRootBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetRootBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetRootBooksRequest}
 */
proto.dlkit.proto.commenting.GetRootBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetRootBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetRootBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetRootBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetRootBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.HasParentBooksReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.HasParentBooksReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.HasParentBooksReply.displayName = 'proto.dlkit.proto.commenting.HasParentBooksReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.HasParentBooksReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.HasParentBooksReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.HasParentBooksReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasParentBooksReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasParentBooks: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.HasParentBooksReply}
 */
proto.dlkit.proto.commenting.HasParentBooksReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.HasParentBooksReply;
  return proto.dlkit.proto.commenting.HasParentBooksReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.HasParentBooksReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.HasParentBooksReply}
 */
proto.dlkit.proto.commenting.HasParentBooksReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasParentBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.HasParentBooksReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.HasParentBooksReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.HasParentBooksReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasParentBooksReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasParentBooks();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_parent_books = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.HasParentBooksReply.prototype.getHasParentBooks = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.HasParentBooksReply.prototype.setHasParentBooks = function(value) {
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
proto.dlkit.proto.commenting.HasParentBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.HasParentBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.HasParentBooksRequest.displayName = 'proto.dlkit.proto.commenting.HasParentBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.HasParentBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.HasParentBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.HasParentBooksRequest}
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.HasParentBooksRequest;
  return proto.dlkit.proto.commenting.HasParentBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.HasParentBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.HasParentBooksRequest}
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.HasParentBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.HasParentBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.HasParentBooksRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.HasParentBooksRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.HasParentBooksRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.IsParentOfBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsParentOfBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsParentOfBookReply.displayName = 'proto.dlkit.proto.commenting.IsParentOfBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsParentOfBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsParentOfBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsParentOfBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsParentOfBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isParentOfBook: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.IsParentOfBookReply}
 */
proto.dlkit.proto.commenting.IsParentOfBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsParentOfBookReply;
  return proto.dlkit.proto.commenting.IsParentOfBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsParentOfBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsParentOfBookReply}
 */
proto.dlkit.proto.commenting.IsParentOfBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsParentOfBook(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.IsParentOfBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsParentOfBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsParentOfBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsParentOfBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsParentOfBook();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_parent_of_book = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.IsParentOfBookReply.prototype.getIsParentOfBook = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.IsParentOfBookReply.prototype.setIsParentOfBook = function(value) {
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
proto.dlkit.proto.commenting.IsParentOfBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsParentOfBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsParentOfBookRequest.displayName = 'proto.dlkit.proto.commenting.IsParentOfBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsParentOfBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsParentOfBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.IsParentOfBookRequest}
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsParentOfBookRequest;
  return proto.dlkit.proto.commenting.IsParentOfBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsParentOfBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsParentOfBookRequest}
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsParentOfBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsParentOfBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
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
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsParentOfBookRequest.prototype.hasId = function() {
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
proto.dlkit.proto.commenting.GetParentBookIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetParentBookIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetParentBookIdsRequest.displayName = 'proto.dlkit.proto.commenting.GetParentBookIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetParentBookIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetParentBookIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetParentBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetParentBookIdsRequest;
  return proto.dlkit.proto.commenting.GetParentBookIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetParentBookIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetParentBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetParentBookIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetParentBookIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetParentBookIdsRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetParentBookIdsRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.GetParentBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetParentBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetParentBooksRequest.displayName = 'proto.dlkit.proto.commenting.GetParentBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetParentBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetParentBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetParentBooksRequest}
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetParentBooksRequest;
  return proto.dlkit.proto.commenting.GetParentBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetParentBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetParentBooksRequest}
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetParentBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetParentBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetParentBooksRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetParentBooksRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetParentBooksRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.IsAncestorOfBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsAncestorOfBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsAncestorOfBookReply.displayName = 'proto.dlkit.proto.commenting.IsAncestorOfBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsAncestorOfBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsAncestorOfBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isAncestorOfBook: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.IsAncestorOfBookReply}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsAncestorOfBookReply;
  return proto.dlkit.proto.commenting.IsAncestorOfBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsAncestorOfBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsAncestorOfBookReply}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsAncestorOfBook(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsAncestorOfBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsAncestorOfBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsAncestorOfBook();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_ancestor_of_book = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.prototype.getIsAncestorOfBook = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.IsAncestorOfBookReply.prototype.setIsAncestorOfBook = function(value) {
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
proto.dlkit.proto.commenting.IsAncestorOfBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsAncestorOfBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsAncestorOfBookRequest.displayName = 'proto.dlkit.proto.commenting.IsAncestorOfBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsAncestorOfBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsAncestorOfBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.IsAncestorOfBookRequest}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsAncestorOfBookRequest;
  return proto.dlkit.proto.commenting.IsAncestorOfBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsAncestorOfBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsAncestorOfBookRequest}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsAncestorOfBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsAncestorOfBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
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
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsAncestorOfBookRequest.prototype.hasId = function() {
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
proto.dlkit.proto.commenting.HasChildBooksReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.HasChildBooksReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.HasChildBooksReply.displayName = 'proto.dlkit.proto.commenting.HasChildBooksReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.HasChildBooksReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.HasChildBooksReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.HasChildBooksReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasChildBooksReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    hasChildBooks: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.HasChildBooksReply}
 */
proto.dlkit.proto.commenting.HasChildBooksReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.HasChildBooksReply;
  return proto.dlkit.proto.commenting.HasChildBooksReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.HasChildBooksReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.HasChildBooksReply}
 */
proto.dlkit.proto.commenting.HasChildBooksReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setHasChildBooks(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.HasChildBooksReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.HasChildBooksReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.HasChildBooksReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasChildBooksReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getHasChildBooks();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool has_child_books = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.HasChildBooksReply.prototype.getHasChildBooks = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.HasChildBooksReply.prototype.setHasChildBooks = function(value) {
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
proto.dlkit.proto.commenting.HasChildBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.HasChildBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.HasChildBooksRequest.displayName = 'proto.dlkit.proto.commenting.HasChildBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.HasChildBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.HasChildBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.HasChildBooksRequest}
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.HasChildBooksRequest;
  return proto.dlkit.proto.commenting.HasChildBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.HasChildBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.HasChildBooksRequest}
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.HasChildBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.HasChildBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.HasChildBooksRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.HasChildBooksRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.HasChildBooksRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.IsChildOfBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsChildOfBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsChildOfBookReply.displayName = 'proto.dlkit.proto.commenting.IsChildOfBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsChildOfBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsChildOfBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsChildOfBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsChildOfBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isChildOfBook: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.IsChildOfBookReply}
 */
proto.dlkit.proto.commenting.IsChildOfBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsChildOfBookReply;
  return proto.dlkit.proto.commenting.IsChildOfBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsChildOfBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsChildOfBookReply}
 */
proto.dlkit.proto.commenting.IsChildOfBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsChildOfBook(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.IsChildOfBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsChildOfBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsChildOfBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsChildOfBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsChildOfBook();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_child_of_book = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.IsChildOfBookReply.prototype.getIsChildOfBook = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.IsChildOfBookReply.prototype.setIsChildOfBook = function(value) {
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
proto.dlkit.proto.commenting.IsChildOfBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsChildOfBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsChildOfBookRequest.displayName = 'proto.dlkit.proto.commenting.IsChildOfBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsChildOfBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsChildOfBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.IsChildOfBookRequest}
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsChildOfBookRequest;
  return proto.dlkit.proto.commenting.IsChildOfBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsChildOfBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsChildOfBookRequest}
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsChildOfBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsChildOfBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
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
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsChildOfBookRequest.prototype.hasId = function() {
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
proto.dlkit.proto.commenting.GetChildBookIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetChildBookIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetChildBookIdsRequest.displayName = 'proto.dlkit.proto.commenting.GetChildBookIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetChildBookIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetChildBookIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetChildBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetChildBookIdsRequest;
  return proto.dlkit.proto.commenting.GetChildBookIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetChildBookIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetChildBookIdsRequest}
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetChildBookIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetChildBookIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetChildBookIdsRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetChildBookIdsRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.GetChildBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetChildBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetChildBooksRequest.displayName = 'proto.dlkit.proto.commenting.GetChildBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetChildBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetChildBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetChildBooksRequest}
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetChildBooksRequest;
  return proto.dlkit.proto.commenting.GetChildBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetChildBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetChildBooksRequest}
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetChildBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetChildBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetChildBooksRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetChildBooksRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetChildBooksRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.IsDescendantOfBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsDescendantOfBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsDescendantOfBookReply.displayName = 'proto.dlkit.proto.commenting.IsDescendantOfBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsDescendantOfBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsDescendantOfBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    isDescendantOfBook: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.IsDescendantOfBookReply}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsDescendantOfBookReply;
  return proto.dlkit.proto.commenting.IsDescendantOfBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsDescendantOfBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsDescendantOfBookReply}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setIsDescendantOfBook(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsDescendantOfBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsDescendantOfBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getIsDescendantOfBook();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool is_descendant_of_book = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.prototype.getIsDescendantOfBook = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.IsDescendantOfBookReply.prototype.setIsDescendantOfBook = function(value) {
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
proto.dlkit.proto.commenting.IsDescendantOfBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.IsDescendantOfBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.IsDescendantOfBookRequest.displayName = 'proto.dlkit.proto.commenting.IsDescendantOfBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.IsDescendantOfBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.IsDescendantOfBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.IsDescendantOfBookRequest}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.IsDescendantOfBookRequest;
  return proto.dlkit.proto.commenting.IsDescendantOfBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.IsDescendantOfBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.IsDescendantOfBookRequest}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.IsDescendantOfBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.IsDescendantOfBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
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
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id id_ = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.getId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.setId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.clearId = function() {
  this.setId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.IsDescendantOfBookRequest.prototype.hasId = function() {
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
proto.dlkit.proto.commenting.GetBookNodeIdsReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookNodeIdsReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookNodeIdsReply.displayName = 'proto.dlkit.proto.commenting.GetBookNodeIdsReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookNodeIdsReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookNodeIdsReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodeIdsReply.toObject = function(includeInstance, msg) {
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
 * @return {!proto.dlkit.proto.commenting.GetBookNodeIdsReply}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookNodeIdsReply;
  return proto.dlkit.proto.commenting.GetBookNodeIdsReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookNodeIdsReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookNodeIdsReply}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsReply.deserializeBinaryFromReader = function(msg, reader) {
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
proto.dlkit.proto.commenting.GetBookNodeIdsReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookNodeIdsReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookNodeIdsReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodeIdsReply.serializeBinaryToWriter = function(message, writer) {
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
proto.dlkit.proto.commenting.GetBookNodeIdsReply.prototype.getNode = function() {
  return /** @type{?proto.dlkit.proto.hierarchy.Node} */ (
    jspb.Message.getWrapperField(this, dlkit_proto_hierarchy_pb.Node, 1));
};


/** @param {?proto.dlkit.proto.hierarchy.Node|undefined} value */
proto.dlkit.proto.commenting.GetBookNodeIdsReply.prototype.setNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookNodeIdsReply.prototype.clearNode = function() {
  this.setNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsReply.prototype.hasNode = function() {
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
proto.dlkit.proto.commenting.GetBookNodeIdsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookNodeIdsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookNodeIdsRequest.displayName = 'proto.dlkit.proto.commenting.GetBookNodeIdsRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookNodeIdsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookNodeIdsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetBookNodeIdsRequest}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookNodeIdsRequest;
  return proto.dlkit.proto.commenting.GetBookNodeIdsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookNodeIdsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookNodeIdsRequest}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookNodeIdsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookNodeIdsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAncestorLevels();
  if (f !== 0) {
    writer.writeSint32(
      1,
      f
    );
  }
  f = message.getBookId();
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
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional sint32 descendant_levels = 3;
 * @return {number}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/** @param {number} value */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 3, value);
};


/**
 * optional bool include_siblings = 4;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 4, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.GetBookNodeIdsRequest.prototype.setIncludeSiblings = function(value) {
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
proto.dlkit.proto.commenting.GetBookNodesReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookNodesReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookNodesReply.displayName = 'proto.dlkit.proto.commenting.GetBookNodesReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookNodesReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookNodesReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookNodesReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodesReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookNode: (f = msg.getBookNode()) && proto.dlkit.proto.commenting.BookNode.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.GetBookNodesReply}
 */
proto.dlkit.proto.commenting.GetBookNodesReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookNodesReply;
  return proto.dlkit.proto.commenting.GetBookNodesReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookNodesReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookNodesReply}
 */
proto.dlkit.proto.commenting.GetBookNodesReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.dlkit.proto.commenting.BookNode;
      reader.readMessage(value,proto.dlkit.proto.commenting.BookNode.deserializeBinaryFromReader);
      msg.setBookNode(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.GetBookNodesReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookNodesReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookNodesReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodesReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookNode();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      proto.dlkit.proto.commenting.BookNode.serializeBinaryToWriter
    );
  }
};


/**
 * optional BookNode book_node = 1;
 * @return {?proto.dlkit.proto.commenting.BookNode}
 */
proto.dlkit.proto.commenting.GetBookNodesReply.prototype.getBookNode = function() {
  return /** @type{?proto.dlkit.proto.commenting.BookNode} */ (
    jspb.Message.getWrapperField(this, proto.dlkit.proto.commenting.BookNode, 1));
};


/** @param {?proto.dlkit.proto.commenting.BookNode|undefined} value */
proto.dlkit.proto.commenting.GetBookNodesReply.prototype.setBookNode = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.GetBookNodesReply.prototype.clearBookNode = function() {
  this.setBookNode(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookNodesReply.prototype.hasBookNode = function() {
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
proto.dlkit.proto.commenting.GetBookNodesRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.GetBookNodesRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.GetBookNodesRequest.displayName = 'proto.dlkit.proto.commenting.GetBookNodesRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.GetBookNodesRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.GetBookNodesRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    ancestorLevels: jspb.Message.getFieldWithDefault(msg, 1, 0),
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.GetBookNodesRequest}
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.GetBookNodesRequest;
  return proto.dlkit.proto.commenting.GetBookNodesRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.GetBookNodesRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.GetBookNodesRequest}
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.deserializeBinaryFromReader = function(msg, reader) {
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
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.GetBookNodesRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.GetBookNodesRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAncestorLevels();
  if (f !== 0) {
    writer.writeSint32(
      1,
      f
    );
  }
  f = message.getBookId();
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
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.getAncestorLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/** @param {number} value */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.setAncestorLevels = function(value) {
  jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional sint32 descendant_levels = 3;
 * @return {number}
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.getDescendantLevels = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/** @param {number} value */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.setDescendantLevels = function(value) {
  jspb.Message.setProto3IntField(this, 3, value);
};


/**
 * optional bool include_siblings = 4;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.getIncludeSiblings = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 4, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.GetBookNodesRequest.prototype.setIncludeSiblings = function(value) {
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
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanModifyBookHierarchyReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.displayName = 'proto.dlkit.proto.commenting.CanModifyBookHierarchyReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanModifyBookHierarchyReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.toObject = function(includeInstance, msg) {
  var f, obj = {
    canModifyBookHierarchy: jspb.Message.getFieldWithDefault(msg, 1, false)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanModifyBookHierarchyReply}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanModifyBookHierarchyReply;
  return proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanModifyBookHierarchyReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanModifyBookHierarchyReply}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setCanModifyBookHierarchy(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanModifyBookHierarchyReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getCanModifyBookHierarchy();
  if (f) {
    writer.writeBool(
      1,
      f
    );
  }
};


/**
 * optional bool can_modify_book_hierarchy = 1;
 * Note that Boolean fields may be set to 0/1 when serialized from a Java server.
 * You should avoid comparisons like {@code val === true/false} in those cases.
 * @return {boolean}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.prototype.getCanModifyBookHierarchy = function() {
  return /** @type {boolean} */ (jspb.Message.getFieldWithDefault(this, 1, false));
};


/** @param {boolean} value */
proto.dlkit.proto.commenting.CanModifyBookHierarchyReply.prototype.setCanModifyBookHierarchy = function(value) {
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
proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.displayName = 'proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest;
  return proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.CanModifyBookHierarchyRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AddRootBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AddRootBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AddRootBookReply.displayName = 'proto.dlkit.proto.commenting.AddRootBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AddRootBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AddRootBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AddRootBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddRootBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AddRootBookReply}
 */
proto.dlkit.proto.commenting.AddRootBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AddRootBookReply;
  return proto.dlkit.proto.commenting.AddRootBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AddRootBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AddRootBookReply}
 */
proto.dlkit.proto.commenting.AddRootBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AddRootBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AddRootBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AddRootBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddRootBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AddRootBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AddRootBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AddRootBookRequest.displayName = 'proto.dlkit.proto.commenting.AddRootBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AddRootBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AddRootBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AddRootBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddRootBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AddRootBookRequest}
 */
proto.dlkit.proto.commenting.AddRootBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AddRootBookRequest;
  return proto.dlkit.proto.commenting.AddRootBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AddRootBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AddRootBookRequest}
 */
proto.dlkit.proto.commenting.AddRootBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AddRootBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AddRootBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AddRootBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddRootBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.AddRootBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AddRootBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.AddRootBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AddRootBookRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.RemoveRootBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.RemoveRootBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.RemoveRootBookReply.displayName = 'proto.dlkit.proto.commenting.RemoveRootBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.RemoveRootBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.RemoveRootBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.RemoveRootBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveRootBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.RemoveRootBookReply}
 */
proto.dlkit.proto.commenting.RemoveRootBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.RemoveRootBookReply;
  return proto.dlkit.proto.commenting.RemoveRootBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.RemoveRootBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.RemoveRootBookReply}
 */
proto.dlkit.proto.commenting.RemoveRootBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.RemoveRootBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.RemoveRootBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.RemoveRootBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveRootBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.RemoveRootBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.RemoveRootBookRequest.displayName = 'proto.dlkit.proto.commenting.RemoveRootBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.RemoveRootBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.RemoveRootBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.RemoveRootBookRequest}
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.RemoveRootBookRequest;
  return proto.dlkit.proto.commenting.RemoveRootBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.RemoveRootBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.RemoveRootBookRequest}
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.RemoveRootBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.RemoveRootBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.RemoveRootBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.RemoveRootBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.RemoveRootBookRequest.prototype.hasBookId = function() {
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
proto.dlkit.proto.commenting.AddChildBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AddChildBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AddChildBookReply.displayName = 'proto.dlkit.proto.commenting.AddChildBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AddChildBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AddChildBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AddChildBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddChildBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.AddChildBookReply}
 */
proto.dlkit.proto.commenting.AddChildBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AddChildBookReply;
  return proto.dlkit.proto.commenting.AddChildBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AddChildBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AddChildBookReply}
 */
proto.dlkit.proto.commenting.AddChildBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.AddChildBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AddChildBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AddChildBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddChildBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.AddChildBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.AddChildBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.AddChildBookRequest.displayName = 'proto.dlkit.proto.commenting.AddChildBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.AddChildBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.AddChildBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddChildBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.AddChildBookRequest}
 */
proto.dlkit.proto.commenting.AddChildBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.AddChildBookRequest;
  return proto.dlkit.proto.commenting.AddChildBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.AddChildBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.AddChildBookRequest}
 */
proto.dlkit.proto.commenting.AddChildBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.AddChildBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.AddChildBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.AddChildBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
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
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.AddChildBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id child_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.AddChildBookRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.AddChildBookRequest.prototype.hasChildId = function() {
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
proto.dlkit.proto.commenting.RemoveChildBookReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.RemoveChildBookReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.RemoveChildBookReply.displayName = 'proto.dlkit.proto.commenting.RemoveChildBookReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.RemoveChildBookReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.RemoveChildBookReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.RemoveChildBookReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBookReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.RemoveChildBookReply}
 */
proto.dlkit.proto.commenting.RemoveChildBookReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.RemoveChildBookReply;
  return proto.dlkit.proto.commenting.RemoveChildBookReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBookReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.RemoveChildBookReply}
 */
proto.dlkit.proto.commenting.RemoveChildBookReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.RemoveChildBookReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.RemoveChildBookReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBookReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBookReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.RemoveChildBookRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.RemoveChildBookRequest.displayName = 'proto.dlkit.proto.commenting.RemoveChildBookRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.RemoveChildBookRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.RemoveChildBookRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f),
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
 * @return {!proto.dlkit.proto.commenting.RemoveChildBookRequest}
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.RemoveChildBookRequest;
  return proto.dlkit.proto.commenting.RemoveChildBookRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBookRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.RemoveChildBookRequest}
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
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
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.RemoveChildBookRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBookRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
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
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


/**
 * optional dlkit.primordium.id.primitives.Id child_id = 2;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.getChildId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 2));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.setChildId = function(value) {
  jspb.Message.setWrapperField(this, 2, value);
};


proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.clearChildId = function() {
  this.setChildId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.RemoveChildBookRequest.prototype.hasChildId = function() {
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
proto.dlkit.proto.commenting.RemoveChildBooksReply = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.RemoveChildBooksReply, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.RemoveChildBooksReply.displayName = 'proto.dlkit.proto.commenting.RemoveChildBooksReply';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.RemoveChildBooksReply.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.RemoveChildBooksReply.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.RemoveChildBooksReply} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBooksReply.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.RemoveChildBooksReply}
 */
proto.dlkit.proto.commenting.RemoveChildBooksReply.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.RemoveChildBooksReply;
  return proto.dlkit.proto.commenting.RemoveChildBooksReply.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBooksReply} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.RemoveChildBooksReply}
 */
proto.dlkit.proto.commenting.RemoveChildBooksReply.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.RemoveChildBooksReply.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.RemoveChildBooksReply.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBooksReply} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBooksReply.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.dlkit.proto.commenting.RemoveChildBooksRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  proto.dlkit.proto.commenting.RemoveChildBooksRequest.displayName = 'proto.dlkit.proto.commenting.RemoveChildBooksRequest';
}


if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto suitable for use in Soy templates.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     com.google.apps.jspb.JsClassTemplate.JS_RESERVED_WORDS.
 * @param {boolean=} opt_includeInstance Whether to include the JSPB instance
 *     for transitional soy proto support: http://goto/soy-param-migration
 * @return {!Object}
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.dlkit.proto.commenting.RemoveChildBooksRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Whether to include the JSPB
 *     instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.dlkit.proto.commenting.RemoveChildBooksRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.toObject = function(includeInstance, msg) {
  var f, obj = {
    bookId: (f = msg.getBookId()) && dlkit_primordium_id_primitives_pb.Id.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.dlkit.proto.commenting.RemoveChildBooksRequest}
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.dlkit.proto.commenting.RemoveChildBooksRequest;
  return proto.dlkit.proto.commenting.RemoveChildBooksRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBooksRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.dlkit.proto.commenting.RemoveChildBooksRequest}
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new dlkit_primordium_id_primitives_pb.Id;
      reader.readMessage(value,dlkit_primordium_id_primitives_pb.Id.deserializeBinaryFromReader);
      msg.setBookId(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.dlkit.proto.commenting.RemoveChildBooksRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.dlkit.proto.commenting.RemoveChildBooksRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getBookId();
  if (f != null) {
    writer.writeMessage(
      1,
      f,
      dlkit_primordium_id_primitives_pb.Id.serializeBinaryToWriter
    );
  }
};


/**
 * optional dlkit.primordium.id.primitives.Id book_id = 1;
 * @return {?proto.dlkit.primordium.id.primitives.Id}
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.prototype.getBookId = function() {
  return /** @type{?proto.dlkit.primordium.id.primitives.Id} */ (
    jspb.Message.getWrapperField(this, dlkit_primordium_id_primitives_pb.Id, 1));
};


/** @param {?proto.dlkit.primordium.id.primitives.Id|undefined} value */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.prototype.setBookId = function(value) {
  jspb.Message.setWrapperField(this, 1, value);
};


proto.dlkit.proto.commenting.RemoveChildBooksRequest.prototype.clearBookId = function() {
  this.setBookId(undefined);
};


/**
 * Returns whether this field is set.
 * @return {!boolean}
 */
proto.dlkit.proto.commenting.RemoveChildBooksRequest.prototype.hasBookId = function() {
  return jspb.Message.getField(this, 1) != null;
};


goog.object.extend(exports, proto.dlkit.proto.commenting);
