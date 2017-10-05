// package: dlkit.proto.commenting
// file: dlkit/proto/commenting.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as dlkit_proto_resource_pb from "../../dlkit/proto/resource_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Comment extends jspb.Message {
  hasBook(): boolean;
  clearBook(): void;
  getBook(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setBook(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasCommentor(): boolean;
  clearCommentor(): void;
  getCommentor(): dlkit_proto_resource_pb.Resource | undefined;
  setCommentor(value?: dlkit_proto_resource_pb.Resource): void;

  hasRating(): boolean;
  clearRating(): void;
  getRating(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setRating(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasReference(): boolean;
  clearReference(): void;
  getReference(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReference(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getText(): string;
  setText(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Comment.AsObject;
  static toObject(includeInstance: boolean, msg: Comment): Comment.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Comment, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Comment;
  static deserializeBinaryFromReader(message: Comment, reader: jspb.BinaryReader): Comment;
}

export namespace Comment {
  export type AsObject = {
    book?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    commentor?: dlkit_proto_resource_pb.Resource.AsObject,
    rating?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    reference?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    text: string,
  }
}

export class CommentQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommentQuery.AsObject;
  static toObject(includeInstance: boolean, msg: CommentQuery): CommentQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommentQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommentQuery;
  static deserializeBinaryFromReader(message: CommentQuery, reader: jspb.BinaryReader): CommentQuery;
}

export namespace CommentQuery {
  export type AsObject = {
  }
}

export class CommentQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommentQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: CommentQueryInspector): CommentQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommentQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommentQueryInspector;
  static deserializeBinaryFromReader(message: CommentQueryInspector, reader: jspb.BinaryReader): CommentQueryInspector;
}

export namespace CommentQueryInspector {
  export type AsObject = {
  }
}

export class CommentForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommentForm.AsObject;
  static toObject(includeInstance: boolean, msg: CommentForm): CommentForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommentForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommentForm;
  static deserializeBinaryFromReader(message: CommentForm, reader: jspb.BinaryReader): CommentForm;
}

export namespace CommentForm {
  export type AsObject = {
  }
}

export class CommentSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommentSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: CommentSearchOrder): CommentSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommentSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommentSearchOrder;
  static deserializeBinaryFromReader(message: CommentSearchOrder, reader: jspb.BinaryReader): CommentSearchOrder;
}

export namespace CommentSearchOrder {
  export type AsObject = {
  }
}

export class CommentSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommentSearch.AsObject;
  static toObject(includeInstance: boolean, msg: CommentSearch): CommentSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommentSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommentSearch;
  static deserializeBinaryFromReader(message: CommentSearch, reader: jspb.BinaryReader): CommentSearch;
}

export namespace CommentSearch {
  export type AsObject = {
  }
}

export class CommentSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommentSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: CommentSearchResults): CommentSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommentSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommentSearchResults;
  static deserializeBinaryFromReader(message: CommentSearchResults, reader: jspb.BinaryReader): CommentSearchResults;
}

export namespace CommentSearchResults {
  export type AsObject = {
  }
}

export class CommentList extends jspb.Message {
  clearCommentsList(): void;
  getCommentsList(): Array<Comment>;
  setCommentsList(value: Array<Comment>): void;
  addComments(value?: Comment, index?: number): Comment;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommentList.AsObject;
  static toObject(includeInstance: boolean, msg: CommentList): CommentList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommentList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommentList;
  static deserializeBinaryFromReader(message: CommentList, reader: jspb.BinaryReader): CommentList;
}

export namespace CommentList {
  export type AsObject = {
    commentsList: Array<Comment.AsObject>,
  }
}

export class Book extends jspb.Message {
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
  toObject(includeInstance?: boolean): Book.AsObject;
  static toObject(includeInstance: boolean, msg: Book): Book.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Book, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Book;
  static deserializeBinaryFromReader(message: Book, reader: jspb.BinaryReader): Book;
}

export namespace Book {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class BookQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookQuery.AsObject;
  static toObject(includeInstance: boolean, msg: BookQuery): BookQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookQuery;
  static deserializeBinaryFromReader(message: BookQuery, reader: jspb.BinaryReader): BookQuery;
}

export namespace BookQuery {
  export type AsObject = {
  }
}

export class BookQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: BookQueryInspector): BookQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookQueryInspector;
  static deserializeBinaryFromReader(message: BookQueryInspector, reader: jspb.BinaryReader): BookQueryInspector;
}

export namespace BookQueryInspector {
  export type AsObject = {
  }
}

export class BookForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookForm.AsObject;
  static toObject(includeInstance: boolean, msg: BookForm): BookForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookForm;
  static deserializeBinaryFromReader(message: BookForm, reader: jspb.BinaryReader): BookForm;
}

export namespace BookForm {
  export type AsObject = {
  }
}

export class BookSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: BookSearchOrder): BookSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookSearchOrder;
  static deserializeBinaryFromReader(message: BookSearchOrder, reader: jspb.BinaryReader): BookSearchOrder;
}

export namespace BookSearchOrder {
  export type AsObject = {
  }
}

export class BookSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookSearch.AsObject;
  static toObject(includeInstance: boolean, msg: BookSearch): BookSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookSearch;
  static deserializeBinaryFromReader(message: BookSearch, reader: jspb.BinaryReader): BookSearch;
}

export namespace BookSearch {
  export type AsObject = {
  }
}

export class BookSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: BookSearchResults): BookSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookSearchResults;
  static deserializeBinaryFromReader(message: BookSearchResults, reader: jspb.BinaryReader): BookSearchResults;
}

export namespace BookSearchResults {
  export type AsObject = {
  }
}

export class BookList extends jspb.Message {
  clearBooksList(): void;
  getBooksList(): Array<Book>;
  setBooksList(value: Array<Book>): void;
  addBooks(value?: Book, index?: number): Book;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookList.AsObject;
  static toObject(includeInstance: boolean, msg: BookList): BookList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookList;
  static deserializeBinaryFromReader(message: BookList, reader: jspb.BinaryReader): BookList;
}

export namespace BookList {
  export type AsObject = {
    booksList: Array<Book.AsObject>,
  }
}

export class BookNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookNode.AsObject;
  static toObject(includeInstance: boolean, msg: BookNode): BookNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookNode;
  static deserializeBinaryFromReader(message: BookNode, reader: jspb.BinaryReader): BookNode;
}

export namespace BookNode {
  export type AsObject = {
  }
}

export class BookNodeList extends jspb.Message {
  clearBookNodesList(): void;
  getBookNodesList(): Array<BookNode>;
  setBookNodesList(value: Array<BookNode>): void;
  addBookNodes(value?: BookNode, index?: number): BookNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BookNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: BookNodeList): BookNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BookNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BookNodeList;
  static deserializeBinaryFromReader(message: BookNodeList, reader: jspb.BinaryReader): BookNodeList;
}

export namespace BookNodeList {
  export type AsObject = {
    bookNodesList: Array<BookNode.AsObject>,
  }
}

export class GetBookIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookIdReply): GetBookIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookIdReply;
  static deserializeBinaryFromReader(message: GetBookIdReply, reader: jspb.BinaryReader): GetBookIdReply;
}

export namespace GetBookIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBookIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookIdRequest): GetBookIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookIdRequest;
  static deserializeBinaryFromReader(message: GetBookIdRequest, reader: jspb.BinaryReader): GetBookIdRequest;
}

export namespace GetBookIdRequest {
  export type AsObject = {
  }
}

export class GetBookReply extends jspb.Message {
  hasBook(): boolean;
  clearBook(): void;
  getBook(): Book | undefined;
  setBook(value?: Book): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookReply): GetBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookReply;
  static deserializeBinaryFromReader(message: GetBookReply, reader: jspb.BinaryReader): GetBookReply;
}

export namespace GetBookReply {
  export type AsObject = {
    book?: Book.AsObject,
  }
}

export class GetBookRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookRequest): GetBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookRequest;
  static deserializeBinaryFromReader(message: GetBookRequest, reader: jspb.BinaryReader): GetBookRequest;
}

export namespace GetBookRequest {
  export type AsObject = {
  }
}

export class CanLookupCommentsReply extends jspb.Message {
  getCanLookupComments(): boolean;
  setCanLookupComments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCommentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCommentsReply): CanLookupCommentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCommentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCommentsReply;
  static deserializeBinaryFromReader(message: CanLookupCommentsReply, reader: jspb.BinaryReader): CanLookupCommentsReply;
}

export namespace CanLookupCommentsReply {
  export type AsObject = {
    canLookupComments: boolean,
  }
}

export class CanLookupCommentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCommentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCommentsRequest): CanLookupCommentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCommentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCommentsRequest;
  static deserializeBinaryFromReader(message: CanLookupCommentsRequest, reader: jspb.BinaryReader): CanLookupCommentsRequest;
}

export namespace CanLookupCommentsRequest {
  export type AsObject = {
  }
}

export class UseComparativeCommentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCommentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCommentViewReply): UseComparativeCommentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCommentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCommentViewReply;
  static deserializeBinaryFromReader(message: UseComparativeCommentViewReply, reader: jspb.BinaryReader): UseComparativeCommentViewReply;
}

export namespace UseComparativeCommentViewReply {
  export type AsObject = {
  }
}

export class UseComparativeCommentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeCommentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeCommentViewRequest): UseComparativeCommentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeCommentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeCommentViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeCommentViewRequest, reader: jspb.BinaryReader): UseComparativeCommentViewRequest;
}

export namespace UseComparativeCommentViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryCommentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCommentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCommentViewReply): UsePlenaryCommentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCommentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCommentViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryCommentViewReply, reader: jspb.BinaryReader): UsePlenaryCommentViewReply;
}

export namespace UsePlenaryCommentViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryCommentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryCommentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryCommentViewRequest): UsePlenaryCommentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryCommentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryCommentViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryCommentViewRequest, reader: jspb.BinaryReader): UsePlenaryCommentViewRequest;
}

export namespace UsePlenaryCommentViewRequest {
  export type AsObject = {
  }
}

export class UseFederatedBookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedBookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedBookViewReply): UseFederatedBookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedBookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedBookViewReply;
  static deserializeBinaryFromReader(message: UseFederatedBookViewReply, reader: jspb.BinaryReader): UseFederatedBookViewReply;
}

export namespace UseFederatedBookViewReply {
  export type AsObject = {
  }
}

export class UseFederatedBookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseFederatedBookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseFederatedBookViewRequest): UseFederatedBookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseFederatedBookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseFederatedBookViewRequest;
  static deserializeBinaryFromReader(message: UseFederatedBookViewRequest, reader: jspb.BinaryReader): UseFederatedBookViewRequest;
}

export namespace UseFederatedBookViewRequest {
  export type AsObject = {
  }
}

export class UseIsolatedBookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedBookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedBookViewReply): UseIsolatedBookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedBookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedBookViewReply;
  static deserializeBinaryFromReader(message: UseIsolatedBookViewReply, reader: jspb.BinaryReader): UseIsolatedBookViewReply;
}

export namespace UseIsolatedBookViewReply {
  export type AsObject = {
  }
}

export class UseIsolatedBookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseIsolatedBookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseIsolatedBookViewRequest): UseIsolatedBookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseIsolatedBookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseIsolatedBookViewRequest;
  static deserializeBinaryFromReader(message: UseIsolatedBookViewRequest, reader: jspb.BinaryReader): UseIsolatedBookViewRequest;
}

export namespace UseIsolatedBookViewRequest {
  export type AsObject = {
  }
}

export class UseEffectiveCommentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveCommentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveCommentViewReply): UseEffectiveCommentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveCommentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveCommentViewReply;
  static deserializeBinaryFromReader(message: UseEffectiveCommentViewReply, reader: jspb.BinaryReader): UseEffectiveCommentViewReply;
}

export namespace UseEffectiveCommentViewReply {
  export type AsObject = {
  }
}

export class UseEffectiveCommentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseEffectiveCommentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseEffectiveCommentViewRequest): UseEffectiveCommentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseEffectiveCommentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseEffectiveCommentViewRequest;
  static deserializeBinaryFromReader(message: UseEffectiveCommentViewRequest, reader: jspb.BinaryReader): UseEffectiveCommentViewRequest;
}

export namespace UseEffectiveCommentViewRequest {
  export type AsObject = {
  }
}

export class UseAnyEffectiveCommentViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveCommentViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveCommentViewReply): UseAnyEffectiveCommentViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveCommentViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveCommentViewReply;
  static deserializeBinaryFromReader(message: UseAnyEffectiveCommentViewReply, reader: jspb.BinaryReader): UseAnyEffectiveCommentViewReply;
}

export namespace UseAnyEffectiveCommentViewReply {
  export type AsObject = {
  }
}

export class UseAnyEffectiveCommentViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseAnyEffectiveCommentViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseAnyEffectiveCommentViewRequest): UseAnyEffectiveCommentViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseAnyEffectiveCommentViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseAnyEffectiveCommentViewRequest;
  static deserializeBinaryFromReader(message: UseAnyEffectiveCommentViewRequest, reader: jspb.BinaryReader): UseAnyEffectiveCommentViewRequest;
}

export namespace UseAnyEffectiveCommentViewRequest {
  export type AsObject = {
  }
}

export class GetCommentReply extends jspb.Message {
  hasComment(): boolean;
  clearComment(): void;
  getComment(): Comment | undefined;
  setComment(value?: Comment): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentReply): GetCommentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentReply;
  static deserializeBinaryFromReader(message: GetCommentReply, reader: jspb.BinaryReader): GetCommentReply;
}

export namespace GetCommentReply {
  export type AsObject = {
    comment?: Comment.AsObject,
  }
}

export class GetCommentRequest extends jspb.Message {
  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentRequest): GetCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentRequest;
  static deserializeBinaryFromReader(message: GetCommentRequest, reader: jspb.BinaryReader): GetCommentRequest;
}

export namespace GetCommentRequest {
  export type AsObject = {
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsByIdsRequest extends jspb.Message {
  clearCommentIdsList(): void;
  getCommentIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setCommentIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addCommentIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByIdsRequest): GetCommentsByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByIdsRequest;
  static deserializeBinaryFromReader(message: GetCommentsByIdsRequest, reader: jspb.BinaryReader): GetCommentsByIdsRequest;
}

export namespace GetCommentsByIdsRequest {
  export type AsObject = {
    commentIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetCommentsByGenusTypeRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeRequest): GetCommentsByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeRequest;
}

export namespace GetCommentsByGenusTypeRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCommentsByParentGenusTypeRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByParentGenusTypeRequest): GetCommentsByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetCommentsByParentGenusTypeRequest, reader: jspb.BinaryReader): GetCommentsByParentGenusTypeRequest;
}

export namespace GetCommentsByParentGenusTypeRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCommentsByRecordTypeRequest extends jspb.Message {
  hasCommentRecordType(): boolean;
  clearCommentRecordType(): void;
  getCommentRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByRecordTypeRequest): GetCommentsByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetCommentsByRecordTypeRequest, reader: jspb.BinaryReader): GetCommentsByRecordTypeRequest;
}

export namespace GetCommentsByRecordTypeRequest {
  export type AsObject = {
    commentRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetCommentsOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsOnDateRequest): GetCommentsOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsOnDateRequest, reader: jspb.BinaryReader): GetCommentsOnDateRequest;
}

export namespace GetCommentsOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsByGenusTypeOnDateRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeOnDateRequest): GetCommentsByGenusTypeOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeOnDateRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeOnDateRequest;
}

export namespace GetCommentsByGenusTypeOnDateRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsForCommentorRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsForCommentorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsForCommentorRequest): GetCommentsForCommentorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsForCommentorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsForCommentorRequest;
  static deserializeBinaryFromReader(message: GetCommentsForCommentorRequest, reader: jspb.BinaryReader): GetCommentsForCommentorRequest;
}

export namespace GetCommentsForCommentorRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsForCommentorOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsForCommentorOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsForCommentorOnDateRequest): GetCommentsForCommentorOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsForCommentorOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsForCommentorOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsForCommentorOnDateRequest, reader: jspb.BinaryReader): GetCommentsForCommentorOnDateRequest;
}

export namespace GetCommentsForCommentorOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsByGenusTypeForCommentorRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeForCommentorRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeForCommentorRequest): GetCommentsByGenusTypeForCommentorRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeForCommentorRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeForCommentorRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeForCommentorRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeForCommentorRequest;
}

export namespace GetCommentsByGenusTypeForCommentorRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsByGenusTypeForCommentorOnDateRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeForCommentorOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeForCommentorOnDateRequest): GetCommentsByGenusTypeForCommentorOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeForCommentorOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeForCommentorOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeForCommentorOnDateRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeForCommentorOnDateRequest;
}

export namespace GetCommentsByGenusTypeForCommentorOnDateRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsForReferenceRequest extends jspb.Message {
  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsForReferenceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsForReferenceRequest): GetCommentsForReferenceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsForReferenceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsForReferenceRequest;
  static deserializeBinaryFromReader(message: GetCommentsForReferenceRequest, reader: jspb.BinaryReader): GetCommentsForReferenceRequest;
}

export namespace GetCommentsForReferenceRequest {
  export type AsObject = {
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsForReferenceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsForReferenceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsForReferenceOnDateRequest): GetCommentsForReferenceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsForReferenceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsForReferenceOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsForReferenceOnDateRequest, reader: jspb.BinaryReader): GetCommentsForReferenceOnDateRequest;
}

export namespace GetCommentsForReferenceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsByGenusTypeForReferenceRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeForReferenceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeForReferenceRequest): GetCommentsByGenusTypeForReferenceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeForReferenceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeForReferenceRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeForReferenceRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeForReferenceRequest;
}

export namespace GetCommentsByGenusTypeForReferenceRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsByGenusTypeForReferenceOnDateRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeForReferenceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeForReferenceOnDateRequest): GetCommentsByGenusTypeForReferenceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeForReferenceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeForReferenceOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeForReferenceOnDateRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeForReferenceOnDateRequest;
}

export namespace GetCommentsByGenusTypeForReferenceOnDateRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsForCommentorAndReferenceRequest extends jspb.Message {
  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsForCommentorAndReferenceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsForCommentorAndReferenceRequest): GetCommentsForCommentorAndReferenceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsForCommentorAndReferenceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsForCommentorAndReferenceRequest;
  static deserializeBinaryFromReader(message: GetCommentsForCommentorAndReferenceRequest, reader: jspb.BinaryReader): GetCommentsForCommentorAndReferenceRequest;
}

export namespace GetCommentsForCommentorAndReferenceRequest {
  export type AsObject = {
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsForCommentorAndReferenceOnDateRequest extends jspb.Message {
  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsForCommentorAndReferenceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsForCommentorAndReferenceOnDateRequest): GetCommentsForCommentorAndReferenceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsForCommentorAndReferenceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsForCommentorAndReferenceOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsForCommentorAndReferenceOnDateRequest, reader: jspb.BinaryReader): GetCommentsForCommentorAndReferenceOnDateRequest;
}

export namespace GetCommentsForCommentorAndReferenceOnDateRequest {
  export type AsObject = {
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsByGenusTypeForCommentorAndReferenceRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeForCommentorAndReferenceRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeForCommentorAndReferenceRequest): GetCommentsByGenusTypeForCommentorAndReferenceRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeForCommentorAndReferenceRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeForCommentorAndReferenceRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeForCommentorAndReferenceRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeForCommentorAndReferenceRequest;
}

export namespace GetCommentsByGenusTypeForCommentorAndReferenceRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest extends jspb.Message {
  hasCommentGenusType(): boolean;
  clearCommentGenusType(): void;
  getCommentGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setCommentGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasFrom_(): boolean;
  clearFrom_(): void;
  getFrom_(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFrom_(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasTo(): boolean;
  clearTo(): void;
  getTo(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setTo(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest): GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest;
  static deserializeBinaryFromReader(message: GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest, reader: jspb.BinaryReader): GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest;
}

export namespace GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest {
  export type AsObject = {
    commentGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    from_?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    to?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class GetCommentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsRequest): GetCommentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsRequest;
  static deserializeBinaryFromReader(message: GetCommentsRequest, reader: jspb.BinaryReader): GetCommentsRequest;
}

export namespace GetCommentsRequest {
  export type AsObject = {
  }
}

export class CanSearchCommentsReply extends jspb.Message {
  getCanSearchComments(): boolean;
  setCanSearchComments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchCommentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchCommentsReply): CanSearchCommentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchCommentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchCommentsReply;
  static deserializeBinaryFromReader(message: CanSearchCommentsReply, reader: jspb.BinaryReader): CanSearchCommentsReply;
}

export namespace CanSearchCommentsReply {
  export type AsObject = {
    canSearchComments: boolean,
  }
}

export class CanSearchCommentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanSearchCommentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanSearchCommentsRequest): CanSearchCommentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanSearchCommentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanSearchCommentsRequest;
  static deserializeBinaryFromReader(message: CanSearchCommentsRequest, reader: jspb.BinaryReader): CanSearchCommentsRequest;
}

export namespace CanSearchCommentsRequest {
  export type AsObject = {
  }
}

export class GetCommentQueryReply extends jspb.Message {
  hasCommentQuery(): boolean;
  clearCommentQuery(): void;
  getCommentQuery(): CommentQuery | undefined;
  setCommentQuery(value?: CommentQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentQueryReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentQueryReply): GetCommentQueryReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentQueryReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentQueryReply;
  static deserializeBinaryFromReader(message: GetCommentQueryReply, reader: jspb.BinaryReader): GetCommentQueryReply;
}

export namespace GetCommentQueryReply {
  export type AsObject = {
    commentQuery?: CommentQuery.AsObject,
  }
}

export class GetCommentQueryRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentQueryRequest): GetCommentQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentQueryRequest;
  static deserializeBinaryFromReader(message: GetCommentQueryRequest, reader: jspb.BinaryReader): GetCommentQueryRequest;
}

export namespace GetCommentQueryRequest {
  export type AsObject = {
  }
}

export class GetCommentsByQueryRequest extends jspb.Message {
  hasCommentQuery(): boolean;
  clearCommentQuery(): void;
  getCommentQuery(): CommentQuery | undefined;
  setCommentQuery(value?: CommentQuery): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByQueryRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByQueryRequest): GetCommentsByQueryRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByQueryRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByQueryRequest;
  static deserializeBinaryFromReader(message: GetCommentsByQueryRequest, reader: jspb.BinaryReader): GetCommentsByQueryRequest;
}

export namespace GetCommentsByQueryRequest {
  export type AsObject = {
    commentQuery?: CommentQuery.AsObject,
  }
}

export class CanCreateCommentsReply extends jspb.Message {
  getCanCreateComments(): boolean;
  setCanCreateComments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCommentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCommentsReply): CanCreateCommentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCommentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCommentsReply;
  static deserializeBinaryFromReader(message: CanCreateCommentsReply, reader: jspb.BinaryReader): CanCreateCommentsReply;
}

export namespace CanCreateCommentsReply {
  export type AsObject = {
    canCreateComments: boolean,
  }
}

export class CanCreateCommentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCommentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCommentsRequest): CanCreateCommentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCommentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCommentsRequest;
  static deserializeBinaryFromReader(message: CanCreateCommentsRequest, reader: jspb.BinaryReader): CanCreateCommentsRequest;
}

export namespace CanCreateCommentsRequest {
  export type AsObject = {
  }
}

export class CanCreateCommentWithRecordTypesReply extends jspb.Message {
  getCanCreateCommentWithRecordTypes(): boolean;
  setCanCreateCommentWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCommentWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCommentWithRecordTypesReply): CanCreateCommentWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCommentWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCommentWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateCommentWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateCommentWithRecordTypesReply;
}

export namespace CanCreateCommentWithRecordTypesReply {
  export type AsObject = {
    canCreateCommentWithRecordTypes: boolean,
  }
}

export class CanCreateCommentWithRecordTypesRequest extends jspb.Message {
  clearCommentRecordTypesList(): void;
  getCommentRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setCommentRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addCommentRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateCommentWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateCommentWithRecordTypesRequest): CanCreateCommentWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateCommentWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateCommentWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateCommentWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateCommentWithRecordTypesRequest;
}

export namespace CanCreateCommentWithRecordTypesRequest {
  export type AsObject = {
    commentRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetCommentFormForCreateReply extends jspb.Message {
  hasCommentForm(): boolean;
  clearCommentForm(): void;
  getCommentForm(): CommentForm | undefined;
  setCommentForm(value?: CommentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentFormForCreateReply): GetCommentFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentFormForCreateReply;
  static deserializeBinaryFromReader(message: GetCommentFormForCreateReply, reader: jspb.BinaryReader): GetCommentFormForCreateReply;
}

export namespace GetCommentFormForCreateReply {
  export type AsObject = {
    commentForm?: CommentForm.AsObject,
  }
}

export class GetCommentFormForCreateRequest extends jspb.Message {
  clearCommentRecordTypesList(): void;
  getCommentRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setCommentRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addCommentRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasReferenceId(): boolean;
  clearReferenceId(): void;
  getReferenceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setReferenceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentFormForCreateRequest): GetCommentFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetCommentFormForCreateRequest, reader: jspb.BinaryReader): GetCommentFormForCreateRequest;
}

export namespace GetCommentFormForCreateRequest {
  export type AsObject = {
    commentRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    referenceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CreateCommentReply extends jspb.Message {
  hasComment(): boolean;
  clearComment(): void;
  getComment(): Comment | undefined;
  setComment(value?: Comment): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateCommentReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateCommentReply): CreateCommentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateCommentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateCommentReply;
  static deserializeBinaryFromReader(message: CreateCommentReply, reader: jspb.BinaryReader): CreateCommentReply;
}

export namespace CreateCommentReply {
  export type AsObject = {
    comment?: Comment.AsObject,
  }
}

export class CreateCommentRequest extends jspb.Message {
  hasCommentForm(): boolean;
  clearCommentForm(): void;
  getCommentForm(): CommentForm | undefined;
  setCommentForm(value?: CommentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateCommentRequest): CreateCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateCommentRequest;
  static deserializeBinaryFromReader(message: CreateCommentRequest, reader: jspb.BinaryReader): CreateCommentRequest;
}

export namespace CreateCommentRequest {
  export type AsObject = {
    commentForm?: CommentForm.AsObject,
  }
}

export class CanUpdateCommentsReply extends jspb.Message {
  getCanUpdateComments(): boolean;
  setCanUpdateComments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateCommentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateCommentsReply): CanUpdateCommentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateCommentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateCommentsReply;
  static deserializeBinaryFromReader(message: CanUpdateCommentsReply, reader: jspb.BinaryReader): CanUpdateCommentsReply;
}

export namespace CanUpdateCommentsReply {
  export type AsObject = {
    canUpdateComments: boolean,
  }
}

export class CanUpdateCommentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateCommentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateCommentsRequest): CanUpdateCommentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateCommentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateCommentsRequest;
  static deserializeBinaryFromReader(message: CanUpdateCommentsRequest, reader: jspb.BinaryReader): CanUpdateCommentsRequest;
}

export namespace CanUpdateCommentsRequest {
  export type AsObject = {
  }
}

export class GetCommentFormForUpdateReply extends jspb.Message {
  hasCommentForm(): boolean;
  clearCommentForm(): void;
  getCommentForm(): CommentForm | undefined;
  setCommentForm(value?: CommentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentFormForUpdateReply): GetCommentFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetCommentFormForUpdateReply, reader: jspb.BinaryReader): GetCommentFormForUpdateReply;
}

export namespace GetCommentFormForUpdateReply {
  export type AsObject = {
    commentForm?: CommentForm.AsObject,
  }
}

export class GetCommentFormForUpdateRequest extends jspb.Message {
  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentFormForUpdateRequest): GetCommentFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetCommentFormForUpdateRequest, reader: jspb.BinaryReader): GetCommentFormForUpdateRequest;
}

export namespace GetCommentFormForUpdateRequest {
  export type AsObject = {
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateCommentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateCommentReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateCommentReply): UpdateCommentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateCommentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateCommentReply;
  static deserializeBinaryFromReader(message: UpdateCommentReply, reader: jspb.BinaryReader): UpdateCommentReply;
}

export namespace UpdateCommentReply {
  export type AsObject = {
  }
}

export class UpdateCommentRequest extends jspb.Message {
  hasCommentForm(): boolean;
  clearCommentForm(): void;
  getCommentForm(): CommentForm | undefined;
  setCommentForm(value?: CommentForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateCommentRequest): UpdateCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateCommentRequest;
  static deserializeBinaryFromReader(message: UpdateCommentRequest, reader: jspb.BinaryReader): UpdateCommentRequest;
}

export namespace UpdateCommentRequest {
  export type AsObject = {
    commentForm?: CommentForm.AsObject,
  }
}

export class CanDeleteCommentsReply extends jspb.Message {
  getCanDeleteComments(): boolean;
  setCanDeleteComments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteCommentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteCommentsReply): CanDeleteCommentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteCommentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteCommentsReply;
  static deserializeBinaryFromReader(message: CanDeleteCommentsReply, reader: jspb.BinaryReader): CanDeleteCommentsReply;
}

export namespace CanDeleteCommentsReply {
  export type AsObject = {
    canDeleteComments: boolean,
  }
}

export class CanDeleteCommentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteCommentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteCommentsRequest): CanDeleteCommentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteCommentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteCommentsRequest;
  static deserializeBinaryFromReader(message: CanDeleteCommentsRequest, reader: jspb.BinaryReader): CanDeleteCommentsRequest;
}

export namespace CanDeleteCommentsRequest {
  export type AsObject = {
  }
}

export class DeleteCommentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCommentReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCommentReply): DeleteCommentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCommentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCommentReply;
  static deserializeBinaryFromReader(message: DeleteCommentReply, reader: jspb.BinaryReader): DeleteCommentReply;
}

export namespace DeleteCommentReply {
  export type AsObject = {
  }
}

export class DeleteCommentRequest extends jspb.Message {
  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteCommentRequest): DeleteCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteCommentRequest;
  static deserializeBinaryFromReader(message: DeleteCommentRequest, reader: jspb.BinaryReader): DeleteCommentRequest;
}

export namespace DeleteCommentRequest {
  export type AsObject = {
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageCommentAliasesReply extends jspb.Message {
  getCanManageCommentAliases(): boolean;
  setCanManageCommentAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageCommentAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageCommentAliasesReply): CanManageCommentAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageCommentAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageCommentAliasesReply;
  static deserializeBinaryFromReader(message: CanManageCommentAliasesReply, reader: jspb.BinaryReader): CanManageCommentAliasesReply;
}

export namespace CanManageCommentAliasesReply {
  export type AsObject = {
    canManageCommentAliases: boolean,
  }
}

export class CanManageCommentAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageCommentAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageCommentAliasesRequest): CanManageCommentAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageCommentAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageCommentAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageCommentAliasesRequest, reader: jspb.BinaryReader): CanManageCommentAliasesRequest;
}

export namespace CanManageCommentAliasesRequest {
  export type AsObject = {
  }
}

export class AliasCommentReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasCommentReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasCommentReply): AliasCommentReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasCommentReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasCommentReply;
  static deserializeBinaryFromReader(message: AliasCommentReply, reader: jspb.BinaryReader): AliasCommentReply;
}

export namespace AliasCommentReply {
  export type AsObject = {
  }
}

export class AliasCommentRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasCommentRequest): AliasCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasCommentRequest;
  static deserializeBinaryFromReader(message: AliasCommentRequest, reader: jspb.BinaryReader): AliasCommentRequest;
}

export namespace AliasCommentRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupCommentBookMappingsReply extends jspb.Message {
  getCanLookupCommentBookMappings(): boolean;
  setCanLookupCommentBookMappings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCommentBookMappingsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCommentBookMappingsReply): CanLookupCommentBookMappingsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCommentBookMappingsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCommentBookMappingsReply;
  static deserializeBinaryFromReader(message: CanLookupCommentBookMappingsReply, reader: jspb.BinaryReader): CanLookupCommentBookMappingsReply;
}

export namespace CanLookupCommentBookMappingsReply {
  export type AsObject = {
    canLookupCommentBookMappings: boolean,
  }
}

export class CanLookupCommentBookMappingsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupCommentBookMappingsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupCommentBookMappingsRequest): CanLookupCommentBookMappingsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupCommentBookMappingsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupCommentBookMappingsRequest;
  static deserializeBinaryFromReader(message: CanLookupCommentBookMappingsRequest, reader: jspb.BinaryReader): CanLookupCommentBookMappingsRequest;
}

export namespace CanLookupCommentBookMappingsRequest {
  export type AsObject = {
  }
}

export class UseComparativeBookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeBookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeBookViewReply): UseComparativeBookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeBookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeBookViewReply;
  static deserializeBinaryFromReader(message: UseComparativeBookViewReply, reader: jspb.BinaryReader): UseComparativeBookViewReply;
}

export namespace UseComparativeBookViewReply {
  export type AsObject = {
  }
}

export class UseComparativeBookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UseComparativeBookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UseComparativeBookViewRequest): UseComparativeBookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UseComparativeBookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UseComparativeBookViewRequest;
  static deserializeBinaryFromReader(message: UseComparativeBookViewRequest, reader: jspb.BinaryReader): UseComparativeBookViewRequest;
}

export namespace UseComparativeBookViewRequest {
  export type AsObject = {
  }
}

export class UsePlenaryBookViewReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryBookViewReply.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryBookViewReply): UsePlenaryBookViewReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryBookViewReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryBookViewReply;
  static deserializeBinaryFromReader(message: UsePlenaryBookViewReply, reader: jspb.BinaryReader): UsePlenaryBookViewReply;
}

export namespace UsePlenaryBookViewReply {
  export type AsObject = {
  }
}

export class UsePlenaryBookViewRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UsePlenaryBookViewRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UsePlenaryBookViewRequest): UsePlenaryBookViewRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UsePlenaryBookViewRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UsePlenaryBookViewRequest;
  static deserializeBinaryFromReader(message: UsePlenaryBookViewRequest, reader: jspb.BinaryReader): UsePlenaryBookViewRequest;
}

export namespace UsePlenaryBookViewRequest {
  export type AsObject = {
  }
}

export class GetCommentIdsByBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentIdsByBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentIdsByBookRequest): GetCommentIdsByBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentIdsByBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentIdsByBookRequest;
  static deserializeBinaryFromReader(message: GetCommentIdsByBookRequest, reader: jspb.BinaryReader): GetCommentIdsByBookRequest;
}

export namespace GetCommentIdsByBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentsByBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByBookRequest): GetCommentsByBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByBookRequest;
  static deserializeBinaryFromReader(message: GetCommentsByBookRequest, reader: jspb.BinaryReader): GetCommentsByBookRequest;
}

export namespace GetCommentsByBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetCommentIdsByBooksRequest extends jspb.Message {
  clearBookIdsList(): void;
  getBookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentIdsByBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentIdsByBooksRequest): GetCommentIdsByBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentIdsByBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentIdsByBooksRequest;
  static deserializeBinaryFromReader(message: GetCommentIdsByBooksRequest, reader: jspb.BinaryReader): GetCommentIdsByBooksRequest;
}

export namespace GetCommentIdsByBooksRequest {
  export type AsObject = {
    bookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetCommentsByBooksRequest extends jspb.Message {
  clearBookIdsList(): void;
  getBookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetCommentsByBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetCommentsByBooksRequest): GetCommentsByBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetCommentsByBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetCommentsByBooksRequest;
  static deserializeBinaryFromReader(message: GetCommentsByBooksRequest, reader: jspb.BinaryReader): GetCommentsByBooksRequest;
}

export namespace GetCommentsByBooksRequest {
  export type AsObject = {
    bookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBookIdsByCommentRequest extends jspb.Message {
  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookIdsByCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookIdsByCommentRequest): GetBookIdsByCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookIdsByCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookIdsByCommentRequest;
  static deserializeBinaryFromReader(message: GetBookIdsByCommentRequest, reader: jspb.BinaryReader): GetBookIdsByCommentRequest;
}

export namespace GetBookIdsByCommentRequest {
  export type AsObject = {
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBooksByCommentRequest extends jspb.Message {
  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBooksByCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBooksByCommentRequest): GetBooksByCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBooksByCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBooksByCommentRequest;
  static deserializeBinaryFromReader(message: GetBooksByCommentRequest, reader: jspb.BinaryReader): GetBooksByCommentRequest;
}

export namespace GetBooksByCommentRequest {
  export type AsObject = {
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanAssignCommentsReply extends jspb.Message {
  getCanAssignComments(): boolean;
  setCanAssignComments(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCommentsReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCommentsReply): CanAssignCommentsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCommentsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCommentsReply;
  static deserializeBinaryFromReader(message: CanAssignCommentsReply, reader: jspb.BinaryReader): CanAssignCommentsReply;
}

export namespace CanAssignCommentsReply {
  export type AsObject = {
    canAssignComments: boolean,
  }
}

export class CanAssignCommentsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCommentsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCommentsRequest): CanAssignCommentsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCommentsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCommentsRequest;
  static deserializeBinaryFromReader(message: CanAssignCommentsRequest, reader: jspb.BinaryReader): CanAssignCommentsRequest;
}

export namespace CanAssignCommentsRequest {
  export type AsObject = {
  }
}

export class CanAssignCommentsToBookReply extends jspb.Message {
  getCanAssignCommentsToBook(): boolean;
  setCanAssignCommentsToBook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCommentsToBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCommentsToBookReply): CanAssignCommentsToBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCommentsToBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCommentsToBookReply;
  static deserializeBinaryFromReader(message: CanAssignCommentsToBookReply, reader: jspb.BinaryReader): CanAssignCommentsToBookReply;
}

export namespace CanAssignCommentsToBookReply {
  export type AsObject = {
    canAssignCommentsToBook: boolean,
  }
}

export class CanAssignCommentsToBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAssignCommentsToBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAssignCommentsToBookRequest): CanAssignCommentsToBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAssignCommentsToBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAssignCommentsToBookRequest;
  static deserializeBinaryFromReader(message: CanAssignCommentsToBookRequest, reader: jspb.BinaryReader): CanAssignCommentsToBookRequest;
}

export namespace CanAssignCommentsToBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBookIdsRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBookIdsRequest): GetAssignableBookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBookIdsRequest;
  static deserializeBinaryFromReader(message: GetAssignableBookIdsRequest, reader: jspb.BinaryReader): GetAssignableBookIdsRequest;
}

export namespace GetAssignableBookIdsRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetAssignableBookIdsForCommentRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetAssignableBookIdsForCommentRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetAssignableBookIdsForCommentRequest): GetAssignableBookIdsForCommentRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetAssignableBookIdsForCommentRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetAssignableBookIdsForCommentRequest;
  static deserializeBinaryFromReader(message: GetAssignableBookIdsForCommentRequest, reader: jspb.BinaryReader): GetAssignableBookIdsForCommentRequest;
}

export namespace GetAssignableBookIdsForCommentRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AssignCommentToBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignCommentToBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AssignCommentToBookReply): AssignCommentToBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignCommentToBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignCommentToBookReply;
  static deserializeBinaryFromReader(message: AssignCommentToBookReply, reader: jspb.BinaryReader): AssignCommentToBookReply;
}

export namespace AssignCommentToBookReply {
  export type AsObject = {
  }
}

export class AssignCommentToBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AssignCommentToBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AssignCommentToBookRequest): AssignCommentToBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AssignCommentToBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AssignCommentToBookRequest;
  static deserializeBinaryFromReader(message: AssignCommentToBookRequest, reader: jspb.BinaryReader): AssignCommentToBookRequest;
}

export namespace AssignCommentToBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UnassignCommentFromBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignCommentFromBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignCommentFromBookReply): UnassignCommentFromBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignCommentFromBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignCommentFromBookReply;
  static deserializeBinaryFromReader(message: UnassignCommentFromBookReply, reader: jspb.BinaryReader): UnassignCommentFromBookReply;
}

export namespace UnassignCommentFromBookReply {
  export type AsObject = {
  }
}

export class UnassignCommentFromBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UnassignCommentFromBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UnassignCommentFromBookRequest): UnassignCommentFromBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UnassignCommentFromBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UnassignCommentFromBookRequest;
  static deserializeBinaryFromReader(message: UnassignCommentFromBookRequest, reader: jspb.BinaryReader): UnassignCommentFromBookRequest;
}

export namespace UnassignCommentFromBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ReassignCommentToBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignCommentToBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignCommentToBookReply): ReassignCommentToBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignCommentToBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignCommentToBookReply;
  static deserializeBinaryFromReader(message: ReassignCommentToBookReply, reader: jspb.BinaryReader): ReassignCommentToBookReply;
}

export namespace ReassignCommentToBookReply {
  export type AsObject = {
  }
}

export class ReassignCommentToBookRequest extends jspb.Message {
  hasCommentId(): boolean;
  clearCommentId(): void;
  getCommentId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCommentId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFromBookId(): boolean;
  clearFromBookId(): void;
  getFromBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setFromBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasToBookId(): boolean;
  clearToBookId(): void;
  getToBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setToBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ReassignCommentToBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ReassignCommentToBookRequest): ReassignCommentToBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ReassignCommentToBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ReassignCommentToBookRequest;
  static deserializeBinaryFromReader(message: ReassignCommentToBookRequest, reader: jspb.BinaryReader): ReassignCommentToBookRequest;
}

export namespace ReassignCommentToBookRequest {
  export type AsObject = {
    commentId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fromBookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    toBookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanLookupBooksReply extends jspb.Message {
  getCanLookupBooks(): boolean;
  setCanLookupBooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupBooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupBooksReply): CanLookupBooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupBooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupBooksReply;
  static deserializeBinaryFromReader(message: CanLookupBooksReply, reader: jspb.BinaryReader): CanLookupBooksReply;
}

export namespace CanLookupBooksReply {
  export type AsObject = {
    canLookupBooks: boolean,
  }
}

export class CanLookupBooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanLookupBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanLookupBooksRequest): CanLookupBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanLookupBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanLookupBooksRequest;
  static deserializeBinaryFromReader(message: CanLookupBooksRequest, reader: jspb.BinaryReader): CanLookupBooksRequest;
}

export namespace CanLookupBooksRequest {
  export type AsObject = {
  }
}

export class GetBooksByIdsRequest extends jspb.Message {
  clearBookIdsList(): void;
  getBookIdsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setBookIdsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addBookIds(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBooksByIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBooksByIdsRequest): GetBooksByIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBooksByIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBooksByIdsRequest;
  static deserializeBinaryFromReader(message: GetBooksByIdsRequest, reader: jspb.BinaryReader): GetBooksByIdsRequest;
}

export namespace GetBooksByIdsRequest {
  export type AsObject = {
    bookIdsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class GetBooksByGenusTypeRequest extends jspb.Message {
  hasBookGenusType(): boolean;
  clearBookGenusType(): void;
  getBookGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBookGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBooksByGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBooksByGenusTypeRequest): GetBooksByGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBooksByGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBooksByGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetBooksByGenusTypeRequest, reader: jspb.BinaryReader): GetBooksByGenusTypeRequest;
}

export namespace GetBooksByGenusTypeRequest {
  export type AsObject = {
    bookGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBooksByParentGenusTypeRequest extends jspb.Message {
  hasBookGenusType(): boolean;
  clearBookGenusType(): void;
  getBookGenusType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBookGenusType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBooksByParentGenusTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBooksByParentGenusTypeRequest): GetBooksByParentGenusTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBooksByParentGenusTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBooksByParentGenusTypeRequest;
  static deserializeBinaryFromReader(message: GetBooksByParentGenusTypeRequest, reader: jspb.BinaryReader): GetBooksByParentGenusTypeRequest;
}

export namespace GetBooksByParentGenusTypeRequest {
  export type AsObject = {
    bookGenusType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBooksByRecordTypeRequest extends jspb.Message {
  hasBookRecordType(): boolean;
  clearBookRecordType(): void;
  getBookRecordType(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setBookRecordType(value?: dlkit_primordium_type_primitives_pb.Type): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBooksByRecordTypeRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBooksByRecordTypeRequest): GetBooksByRecordTypeRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBooksByRecordTypeRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBooksByRecordTypeRequest;
  static deserializeBinaryFromReader(message: GetBooksByRecordTypeRequest, reader: jspb.BinaryReader): GetBooksByRecordTypeRequest;
}

export namespace GetBooksByRecordTypeRequest {
  export type AsObject = {
    bookRecordType?: dlkit_primordium_type_primitives_pb.Type.AsObject,
  }
}

export class GetBooksByProviderRequest extends jspb.Message {
  hasResourceId(): boolean;
  clearResourceId(): void;
  getResourceId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResourceId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBooksByProviderRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBooksByProviderRequest): GetBooksByProviderRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBooksByProviderRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBooksByProviderRequest;
  static deserializeBinaryFromReader(message: GetBooksByProviderRequest, reader: jspb.BinaryReader): GetBooksByProviderRequest;
}

export namespace GetBooksByProviderRequest {
  export type AsObject = {
    resourceId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBooksRequest): GetBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBooksRequest;
  static deserializeBinaryFromReader(message: GetBooksRequest, reader: jspb.BinaryReader): GetBooksRequest;
}

export namespace GetBooksRequest {
  export type AsObject = {
  }
}

export class CanCreateBooksReply extends jspb.Message {
  getCanCreateBooks(): boolean;
  setCanCreateBooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBooksReply): CanCreateBooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBooksReply;
  static deserializeBinaryFromReader(message: CanCreateBooksReply, reader: jspb.BinaryReader): CanCreateBooksReply;
}

export namespace CanCreateBooksReply {
  export type AsObject = {
    canCreateBooks: boolean,
  }
}

export class CanCreateBooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBooksRequest): CanCreateBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBooksRequest;
  static deserializeBinaryFromReader(message: CanCreateBooksRequest, reader: jspb.BinaryReader): CanCreateBooksRequest;
}

export namespace CanCreateBooksRequest {
  export type AsObject = {
  }
}

export class CanCreateBookWithRecordTypesReply extends jspb.Message {
  getCanCreateBookWithRecordTypes(): boolean;
  setCanCreateBookWithRecordTypes(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBookWithRecordTypesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBookWithRecordTypesReply): CanCreateBookWithRecordTypesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBookWithRecordTypesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBookWithRecordTypesReply;
  static deserializeBinaryFromReader(message: CanCreateBookWithRecordTypesReply, reader: jspb.BinaryReader): CanCreateBookWithRecordTypesReply;
}

export namespace CanCreateBookWithRecordTypesReply {
  export type AsObject = {
    canCreateBookWithRecordTypes: boolean,
  }
}

export class CanCreateBookWithRecordTypesRequest extends jspb.Message {
  clearBookRecordTypesList(): void;
  getBookRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setBookRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addBookRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanCreateBookWithRecordTypesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanCreateBookWithRecordTypesRequest): CanCreateBookWithRecordTypesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanCreateBookWithRecordTypesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanCreateBookWithRecordTypesRequest;
  static deserializeBinaryFromReader(message: CanCreateBookWithRecordTypesRequest, reader: jspb.BinaryReader): CanCreateBookWithRecordTypesRequest;
}

export namespace CanCreateBookWithRecordTypesRequest {
  export type AsObject = {
    bookRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class GetBookFormForCreateReply extends jspb.Message {
  hasBookForm(): boolean;
  clearBookForm(): void;
  getBookForm(): BookForm | undefined;
  setBookForm(value?: BookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookFormForCreateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookFormForCreateReply): GetBookFormForCreateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookFormForCreateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookFormForCreateReply;
  static deserializeBinaryFromReader(message: GetBookFormForCreateReply, reader: jspb.BinaryReader): GetBookFormForCreateReply;
}

export namespace GetBookFormForCreateReply {
  export type AsObject = {
    bookForm?: BookForm.AsObject,
  }
}

export class GetBookFormForCreateRequest extends jspb.Message {
  clearBookRecordTypesList(): void;
  getBookRecordTypesList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setBookRecordTypesList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addBookRecordTypes(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookFormForCreateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookFormForCreateRequest): GetBookFormForCreateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookFormForCreateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookFormForCreateRequest;
  static deserializeBinaryFromReader(message: GetBookFormForCreateRequest, reader: jspb.BinaryReader): GetBookFormForCreateRequest;
}

export namespace GetBookFormForCreateRequest {
  export type AsObject = {
    bookRecordTypesList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CreateBookReply extends jspb.Message {
  hasBook(): boolean;
  clearBook(): void;
  getBook(): Book | undefined;
  setBook(value?: Book): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: CreateBookReply): CreateBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateBookReply;
  static deserializeBinaryFromReader(message: CreateBookReply, reader: jspb.BinaryReader): CreateBookReply;
}

export namespace CreateBookReply {
  export type AsObject = {
    book?: Book.AsObject,
  }
}

export class CreateBookRequest extends jspb.Message {
  hasBookForm(): boolean;
  clearBookForm(): void;
  getBookForm(): BookForm | undefined;
  setBookForm(value?: BookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CreateBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CreateBookRequest): CreateBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CreateBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CreateBookRequest;
  static deserializeBinaryFromReader(message: CreateBookRequest, reader: jspb.BinaryReader): CreateBookRequest;
}

export namespace CreateBookRequest {
  export type AsObject = {
    bookForm?: BookForm.AsObject,
  }
}

export class CanUpdateBooksReply extends jspb.Message {
  getCanUpdateBooks(): boolean;
  setCanUpdateBooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateBooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateBooksReply): CanUpdateBooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateBooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateBooksReply;
  static deserializeBinaryFromReader(message: CanUpdateBooksReply, reader: jspb.BinaryReader): CanUpdateBooksReply;
}

export namespace CanUpdateBooksReply {
  export type AsObject = {
    canUpdateBooks: boolean,
  }
}

export class CanUpdateBooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanUpdateBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanUpdateBooksRequest): CanUpdateBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanUpdateBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanUpdateBooksRequest;
  static deserializeBinaryFromReader(message: CanUpdateBooksRequest, reader: jspb.BinaryReader): CanUpdateBooksRequest;
}

export namespace CanUpdateBooksRequest {
  export type AsObject = {
  }
}

export class GetBookFormForUpdateReply extends jspb.Message {
  hasBookForm(): boolean;
  clearBookForm(): void;
  getBookForm(): BookForm | undefined;
  setBookForm(value?: BookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookFormForUpdateReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookFormForUpdateReply): GetBookFormForUpdateReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookFormForUpdateReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookFormForUpdateReply;
  static deserializeBinaryFromReader(message: GetBookFormForUpdateReply, reader: jspb.BinaryReader): GetBookFormForUpdateReply;
}

export namespace GetBookFormForUpdateReply {
  export type AsObject = {
    bookForm?: BookForm.AsObject,
  }
}

export class GetBookFormForUpdateRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookFormForUpdateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookFormForUpdateRequest): GetBookFormForUpdateRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookFormForUpdateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookFormForUpdateRequest;
  static deserializeBinaryFromReader(message: GetBookFormForUpdateRequest, reader: jspb.BinaryReader): GetBookFormForUpdateRequest;
}

export namespace GetBookFormForUpdateRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class UpdateBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateBookReply): UpdateBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateBookReply;
  static deserializeBinaryFromReader(message: UpdateBookReply, reader: jspb.BinaryReader): UpdateBookReply;
}

export namespace UpdateBookReply {
  export type AsObject = {
  }
}

export class UpdateBookRequest extends jspb.Message {
  hasBookForm(): boolean;
  clearBookForm(): void;
  getBookForm(): BookForm | undefined;
  setBookForm(value?: BookForm): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): UpdateBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: UpdateBookRequest): UpdateBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: UpdateBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): UpdateBookRequest;
  static deserializeBinaryFromReader(message: UpdateBookRequest, reader: jspb.BinaryReader): UpdateBookRequest;
}

export namespace UpdateBookRequest {
  export type AsObject = {
    bookForm?: BookForm.AsObject,
  }
}

export class CanDeleteBooksReply extends jspb.Message {
  getCanDeleteBooks(): boolean;
  setCanDeleteBooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteBooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteBooksReply): CanDeleteBooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteBooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteBooksReply;
  static deserializeBinaryFromReader(message: CanDeleteBooksReply, reader: jspb.BinaryReader): CanDeleteBooksReply;
}

export namespace CanDeleteBooksReply {
  export type AsObject = {
    canDeleteBooks: boolean,
  }
}

export class CanDeleteBooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanDeleteBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanDeleteBooksRequest): CanDeleteBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanDeleteBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanDeleteBooksRequest;
  static deserializeBinaryFromReader(message: CanDeleteBooksRequest, reader: jspb.BinaryReader): CanDeleteBooksRequest;
}

export namespace CanDeleteBooksRequest {
  export type AsObject = {
  }
}

export class DeleteBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteBookReply): DeleteBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteBookReply;
  static deserializeBinaryFromReader(message: DeleteBookReply, reader: jspb.BinaryReader): DeleteBookReply;
}

export namespace DeleteBookReply {
  export type AsObject = {
  }
}

export class DeleteBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DeleteBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DeleteBookRequest): DeleteBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DeleteBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DeleteBookRequest;
  static deserializeBinaryFromReader(message: DeleteBookRequest, reader: jspb.BinaryReader): DeleteBookRequest;
}

export namespace DeleteBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CanManageBookAliasesReply extends jspb.Message {
  getCanManageBookAliases(): boolean;
  setCanManageBookAliases(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageBookAliasesReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageBookAliasesReply): CanManageBookAliasesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageBookAliasesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageBookAliasesReply;
  static deserializeBinaryFromReader(message: CanManageBookAliasesReply, reader: jspb.BinaryReader): CanManageBookAliasesReply;
}

export namespace CanManageBookAliasesReply {
  export type AsObject = {
    canManageBookAliases: boolean,
  }
}

export class CanManageBookAliasesRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanManageBookAliasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanManageBookAliasesRequest): CanManageBookAliasesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanManageBookAliasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanManageBookAliasesRequest;
  static deserializeBinaryFromReader(message: CanManageBookAliasesRequest, reader: jspb.BinaryReader): CanManageBookAliasesRequest;
}

export namespace CanManageBookAliasesRequest {
  export type AsObject = {
  }
}

export class AliasBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AliasBookReply): AliasBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasBookReply;
  static deserializeBinaryFromReader(message: AliasBookReply, reader: jspb.BinaryReader): AliasBookReply;
}

export namespace AliasBookReply {
  export type AsObject = {
  }
}

export class AliasBookRequest extends jspb.Message {
  hasAliasId(): boolean;
  clearAliasId(): void;
  getAliasId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setAliasId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AliasBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AliasBookRequest): AliasBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AliasBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AliasBookRequest;
  static deserializeBinaryFromReader(message: AliasBookRequest, reader: jspb.BinaryReader): AliasBookRequest;
}

export namespace AliasBookRequest {
  export type AsObject = {
    aliasId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBookHierarchyIdReply extends jspb.Message {
  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookHierarchyIdReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookHierarchyIdReply): GetBookHierarchyIdReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookHierarchyIdReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookHierarchyIdReply;
  static deserializeBinaryFromReader(message: GetBookHierarchyIdReply, reader: jspb.BinaryReader): GetBookHierarchyIdReply;
}

export namespace GetBookHierarchyIdReply {
  export type AsObject = {
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBookHierarchyIdRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookHierarchyIdRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookHierarchyIdRequest): GetBookHierarchyIdRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookHierarchyIdRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookHierarchyIdRequest;
  static deserializeBinaryFromReader(message: GetBookHierarchyIdRequest, reader: jspb.BinaryReader): GetBookHierarchyIdRequest;
}

export namespace GetBookHierarchyIdRequest {
  export type AsObject = {
  }
}

export class GetBookHierarchyReply extends jspb.Message {
  hasHierarchy(): boolean;
  clearHierarchy(): void;
  getHierarchy(): dlkit_proto_hierarchy_pb.Hierarchy | undefined;
  setHierarchy(value?: dlkit_proto_hierarchy_pb.Hierarchy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookHierarchyReply): GetBookHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookHierarchyReply;
  static deserializeBinaryFromReader(message: GetBookHierarchyReply, reader: jspb.BinaryReader): GetBookHierarchyReply;
}

export namespace GetBookHierarchyReply {
  export type AsObject = {
    hierarchy?: dlkit_proto_hierarchy_pb.Hierarchy.AsObject,
  }
}

export class GetBookHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookHierarchyRequest): GetBookHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookHierarchyRequest;
  static deserializeBinaryFromReader(message: GetBookHierarchyRequest, reader: jspb.BinaryReader): GetBookHierarchyRequest;
}

export namespace GetBookHierarchyRequest {
  export type AsObject = {
  }
}

export class CanAccessBookHierarchyReply extends jspb.Message {
  getCanAccessBookHierarchy(): boolean;
  setCanAccessBookHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessBookHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessBookHierarchyReply): CanAccessBookHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessBookHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessBookHierarchyReply;
  static deserializeBinaryFromReader(message: CanAccessBookHierarchyReply, reader: jspb.BinaryReader): CanAccessBookHierarchyReply;
}

export namespace CanAccessBookHierarchyReply {
  export type AsObject = {
    canAccessBookHierarchy: boolean,
  }
}

export class CanAccessBookHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanAccessBookHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanAccessBookHierarchyRequest): CanAccessBookHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanAccessBookHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanAccessBookHierarchyRequest;
  static deserializeBinaryFromReader(message: CanAccessBookHierarchyRequest, reader: jspb.BinaryReader): CanAccessBookHierarchyRequest;
}

export namespace CanAccessBookHierarchyRequest {
  export type AsObject = {
  }
}

export class GetRootBookIdsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootBookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootBookIdsRequest): GetRootBookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootBookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootBookIdsRequest;
  static deserializeBinaryFromReader(message: GetRootBookIdsRequest, reader: jspb.BinaryReader): GetRootBookIdsRequest;
}

export namespace GetRootBookIdsRequest {
  export type AsObject = {
  }
}

export class GetRootBooksRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetRootBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetRootBooksRequest): GetRootBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetRootBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetRootBooksRequest;
  static deserializeBinaryFromReader(message: GetRootBooksRequest, reader: jspb.BinaryReader): GetRootBooksRequest;
}

export namespace GetRootBooksRequest {
  export type AsObject = {
  }
}

export class HasParentBooksReply extends jspb.Message {
  getHasParentBooks(): boolean;
  setHasParentBooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentBooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentBooksReply): HasParentBooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentBooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentBooksReply;
  static deserializeBinaryFromReader(message: HasParentBooksReply, reader: jspb.BinaryReader): HasParentBooksReply;
}

export namespace HasParentBooksReply {
  export type AsObject = {
    hasParentBooks: boolean,
  }
}

export class HasParentBooksRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasParentBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasParentBooksRequest): HasParentBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasParentBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasParentBooksRequest;
  static deserializeBinaryFromReader(message: HasParentBooksRequest, reader: jspb.BinaryReader): HasParentBooksRequest;
}

export namespace HasParentBooksRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsParentOfBookReply extends jspb.Message {
  getIsParentOfBook(): boolean;
  setIsParentOfBook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfBookReply): IsParentOfBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfBookReply;
  static deserializeBinaryFromReader(message: IsParentOfBookReply, reader: jspb.BinaryReader): IsParentOfBookReply;
}

export namespace IsParentOfBookReply {
  export type AsObject = {
    isParentOfBook: boolean,
  }
}

export class IsParentOfBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsParentOfBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsParentOfBookRequest): IsParentOfBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsParentOfBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsParentOfBookRequest;
  static deserializeBinaryFromReader(message: IsParentOfBookRequest, reader: jspb.BinaryReader): IsParentOfBookRequest;
}

export namespace IsParentOfBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentBookIdsRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentBookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentBookIdsRequest): GetParentBookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentBookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentBookIdsRequest;
  static deserializeBinaryFromReader(message: GetParentBookIdsRequest, reader: jspb.BinaryReader): GetParentBookIdsRequest;
}

export namespace GetParentBookIdsRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetParentBooksRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetParentBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetParentBooksRequest): GetParentBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetParentBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetParentBooksRequest;
  static deserializeBinaryFromReader(message: GetParentBooksRequest, reader: jspb.BinaryReader): GetParentBooksRequest;
}

export namespace GetParentBooksRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsAncestorOfBookReply extends jspb.Message {
  getIsAncestorOfBook(): boolean;
  setIsAncestorOfBook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfBookReply): IsAncestorOfBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfBookReply;
  static deserializeBinaryFromReader(message: IsAncestorOfBookReply, reader: jspb.BinaryReader): IsAncestorOfBookReply;
}

export namespace IsAncestorOfBookReply {
  export type AsObject = {
    isAncestorOfBook: boolean,
  }
}

export class IsAncestorOfBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsAncestorOfBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsAncestorOfBookRequest): IsAncestorOfBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsAncestorOfBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsAncestorOfBookRequest;
  static deserializeBinaryFromReader(message: IsAncestorOfBookRequest, reader: jspb.BinaryReader): IsAncestorOfBookRequest;
}

export namespace IsAncestorOfBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class HasChildBooksReply extends jspb.Message {
  getHasChildBooks(): boolean;
  setHasChildBooks(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildBooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildBooksReply): HasChildBooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildBooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildBooksReply;
  static deserializeBinaryFromReader(message: HasChildBooksReply, reader: jspb.BinaryReader): HasChildBooksReply;
}

export namespace HasChildBooksReply {
  export type AsObject = {
    hasChildBooks: boolean,
  }
}

export class HasChildBooksRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): HasChildBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: HasChildBooksRequest): HasChildBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: HasChildBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): HasChildBooksRequest;
  static deserializeBinaryFromReader(message: HasChildBooksRequest, reader: jspb.BinaryReader): HasChildBooksRequest;
}

export namespace HasChildBooksRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsChildOfBookReply extends jspb.Message {
  getIsChildOfBook(): boolean;
  setIsChildOfBook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfBookReply): IsChildOfBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfBookReply;
  static deserializeBinaryFromReader(message: IsChildOfBookReply, reader: jspb.BinaryReader): IsChildOfBookReply;
}

export namespace IsChildOfBookReply {
  export type AsObject = {
    isChildOfBook: boolean,
  }
}

export class IsChildOfBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsChildOfBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsChildOfBookRequest): IsChildOfBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsChildOfBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsChildOfBookRequest;
  static deserializeBinaryFromReader(message: IsChildOfBookRequest, reader: jspb.BinaryReader): IsChildOfBookRequest;
}

export namespace IsChildOfBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildBookIdsRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildBookIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildBookIdsRequest): GetChildBookIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildBookIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildBookIdsRequest;
  static deserializeBinaryFromReader(message: GetChildBookIdsRequest, reader: jspb.BinaryReader): GetChildBookIdsRequest;
}

export namespace GetChildBookIdsRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetChildBooksRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetChildBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetChildBooksRequest): GetChildBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetChildBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetChildBooksRequest;
  static deserializeBinaryFromReader(message: GetChildBooksRequest, reader: jspb.BinaryReader): GetChildBooksRequest;
}

export namespace GetChildBooksRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class IsDescendantOfBookReply extends jspb.Message {
  getIsDescendantOfBook(): boolean;
  setIsDescendantOfBook(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfBookReply): IsDescendantOfBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfBookReply;
  static deserializeBinaryFromReader(message: IsDescendantOfBookReply, reader: jspb.BinaryReader): IsDescendantOfBookReply;
}

export namespace IsDescendantOfBookReply {
  export type AsObject = {
    isDescendantOfBook: boolean,
  }
}

export class IsDescendantOfBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasId_(): boolean;
  clearId_(): void;
  getId_(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId_(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): IsDescendantOfBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: IsDescendantOfBookRequest): IsDescendantOfBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: IsDescendantOfBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): IsDescendantOfBookRequest;
  static deserializeBinaryFromReader(message: IsDescendantOfBookRequest, reader: jspb.BinaryReader): IsDescendantOfBookRequest;
}

export namespace IsDescendantOfBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    id_?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class GetBookNodeIdsReply extends jspb.Message {
  hasNode(): boolean;
  clearNode(): void;
  getNode(): dlkit_proto_hierarchy_pb.Node | undefined;
  setNode(value?: dlkit_proto_hierarchy_pb.Node): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookNodeIdsReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookNodeIdsReply): GetBookNodeIdsReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookNodeIdsReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookNodeIdsReply;
  static deserializeBinaryFromReader(message: GetBookNodeIdsReply, reader: jspb.BinaryReader): GetBookNodeIdsReply;
}

export namespace GetBookNodeIdsReply {
  export type AsObject = {
    node?: dlkit_proto_hierarchy_pb.Node.AsObject,
  }
}

export class GetBookNodeIdsRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookNodeIdsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookNodeIdsRequest): GetBookNodeIdsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookNodeIdsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookNodeIdsRequest;
  static deserializeBinaryFromReader(message: GetBookNodeIdsRequest, reader: jspb.BinaryReader): GetBookNodeIdsRequest;
}

export namespace GetBookNodeIdsRequest {
  export type AsObject = {
    ancestorLevels: number,
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class GetBookNodesReply extends jspb.Message {
  hasBookNode(): boolean;
  clearBookNode(): void;
  getBookNode(): BookNode | undefined;
  setBookNode(value?: BookNode): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookNodesReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookNodesReply): GetBookNodesReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookNodesReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookNodesReply;
  static deserializeBinaryFromReader(message: GetBookNodesReply, reader: jspb.BinaryReader): GetBookNodesReply;
}

export namespace GetBookNodesReply {
  export type AsObject = {
    bookNode?: BookNode.AsObject,
  }
}

export class GetBookNodesRequest extends jspb.Message {
  getAncestorLevels(): number;
  setAncestorLevels(value: number): void;

  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getDescendantLevels(): number;
  setDescendantLevels(value: number): void;

  getIncludeSiblings(): boolean;
  setIncludeSiblings(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetBookNodesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetBookNodesRequest): GetBookNodesRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetBookNodesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetBookNodesRequest;
  static deserializeBinaryFromReader(message: GetBookNodesRequest, reader: jspb.BinaryReader): GetBookNodesRequest;
}

export namespace GetBookNodesRequest {
  export type AsObject = {
    ancestorLevels: number,
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    descendantLevels: number,
    includeSiblings: boolean,
  }
}

export class CanModifyBookHierarchyReply extends jspb.Message {
  getCanModifyBookHierarchy(): boolean;
  setCanModifyBookHierarchy(value: boolean): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyBookHierarchyReply.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyBookHierarchyReply): CanModifyBookHierarchyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyBookHierarchyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyBookHierarchyReply;
  static deserializeBinaryFromReader(message: CanModifyBookHierarchyReply, reader: jspb.BinaryReader): CanModifyBookHierarchyReply;
}

export namespace CanModifyBookHierarchyReply {
  export type AsObject = {
    canModifyBookHierarchy: boolean,
  }
}

export class CanModifyBookHierarchyRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CanModifyBookHierarchyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: CanModifyBookHierarchyRequest): CanModifyBookHierarchyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CanModifyBookHierarchyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CanModifyBookHierarchyRequest;
  static deserializeBinaryFromReader(message: CanModifyBookHierarchyRequest, reader: jspb.BinaryReader): CanModifyBookHierarchyRequest;
}

export namespace CanModifyBookHierarchyRequest {
  export type AsObject = {
  }
}

export class AddRootBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootBookReply): AddRootBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootBookReply;
  static deserializeBinaryFromReader(message: AddRootBookReply, reader: jspb.BinaryReader): AddRootBookReply;
}

export namespace AddRootBookReply {
  export type AsObject = {
  }
}

export class AddRootBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddRootBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddRootBookRequest): AddRootBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddRootBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddRootBookRequest;
  static deserializeBinaryFromReader(message: AddRootBookRequest, reader: jspb.BinaryReader): AddRootBookRequest;
}

export namespace AddRootBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveRootBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootBookReply): RemoveRootBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootBookReply;
  static deserializeBinaryFromReader(message: RemoveRootBookReply, reader: jspb.BinaryReader): RemoveRootBookReply;
}

export namespace RemoveRootBookReply {
  export type AsObject = {
  }
}

export class RemoveRootBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveRootBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveRootBookRequest): RemoveRootBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveRootBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveRootBookRequest;
  static deserializeBinaryFromReader(message: RemoveRootBookRequest, reader: jspb.BinaryReader): RemoveRootBookRequest;
}

export namespace RemoveRootBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class AddChildBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildBookReply): AddChildBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildBookReply;
  static deserializeBinaryFromReader(message: AddChildBookReply, reader: jspb.BinaryReader): AddChildBookReply;
}

export namespace AddChildBookReply {
  export type AsObject = {
  }
}

export class AddChildBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): AddChildBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: AddChildBookRequest): AddChildBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: AddChildBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): AddChildBookRequest;
  static deserializeBinaryFromReader(message: AddChildBookRequest, reader: jspb.BinaryReader): AddChildBookRequest;
}

export namespace AddChildBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildBookReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBookReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBookReply): RemoveChildBookReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBookReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBookReply;
  static deserializeBinaryFromReader(message: RemoveChildBookReply, reader: jspb.BinaryReader): RemoveChildBookReply;
}

export namespace RemoveChildBookReply {
  export type AsObject = {
  }
}

export class RemoveChildBookRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasChildId(): boolean;
  clearChildId(): void;
  getChildId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setChildId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBookRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBookRequest): RemoveChildBookRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBookRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBookRequest;
  static deserializeBinaryFromReader(message: RemoveChildBookRequest, reader: jspb.BinaryReader): RemoveChildBookRequest;
}

export namespace RemoveChildBookRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    childId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class RemoveChildBooksReply extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBooksReply.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBooksReply): RemoveChildBooksReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBooksReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBooksReply;
  static deserializeBinaryFromReader(message: RemoveChildBooksReply, reader: jspb.BinaryReader): RemoveChildBooksReply;
}

export namespace RemoveChildBooksReply {
  export type AsObject = {
  }
}

export class RemoveChildBooksRequest extends jspb.Message {
  hasBookId(): boolean;
  clearBookId(): void;
  getBookId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setBookId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoveChildBooksRequest.AsObject;
  static toObject(includeInstance: boolean, msg: RemoveChildBooksRequest): RemoveChildBooksRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RemoveChildBooksRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoveChildBooksRequest;
  static deserializeBinaryFromReader(message: RemoveChildBooksRequest, reader: jspb.BinaryReader): RemoveChildBooksRequest;
}

export namespace RemoveChildBooksRequest {
  export type AsObject = {
    bookId?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

