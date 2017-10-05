// package: dlkit.proto.commenting
// file: dlkit/proto/commenting.proto

import * as dlkit_proto_commenting_pb from "../../dlkit/proto/commenting_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as dlkit_proto_resource_pb from "../../dlkit/proto/resource_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class CommentLookupSession {
  static serviceName = "dlkit.proto.commenting.CommentLookupSession";
}
export namespace CommentLookupSession {
  export class GetBookId {
    static readonly methodName = "GetBookId";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookIdRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookIdReply;
  }
  export class GetBook {
    static readonly methodName = "GetBook";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookReply;
  }
  export class CanLookupComments {
    static readonly methodName = "CanLookupComments";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanLookupCommentsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanLookupCommentsReply;
  }
  export class UseComparativeCommentView {
    static readonly methodName = "UseComparativeCommentView";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseComparativeCommentViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseComparativeCommentViewReply;
  }
  export class UsePlenaryCommentView {
    static readonly methodName = "UsePlenaryCommentView";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UsePlenaryCommentViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UsePlenaryCommentViewReply;
  }
  export class UseFederatedBookView {
    static readonly methodName = "UseFederatedBookView";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseFederatedBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseFederatedBookViewReply;
  }
  export class UseIsolatedBookView {
    static readonly methodName = "UseIsolatedBookView";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseIsolatedBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseIsolatedBookViewReply;
  }
  export class UseEffectiveCommentView {
    static readonly methodName = "UseEffectiveCommentView";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseEffectiveCommentViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseEffectiveCommentViewReply;
  }
  export class UseAnyEffectiveCommentView {
    static readonly methodName = "UseAnyEffectiveCommentView";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseAnyEffectiveCommentViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseAnyEffectiveCommentViewReply;
  }
  export class GetComment {
    static readonly methodName = "GetComment";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetCommentReply;
  }
  export class GetCommentsByIds {
    static readonly methodName = "GetCommentsByIds";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByIdsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusType {
    static readonly methodName = "GetCommentsByGenusType";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByParentGenusType {
    static readonly methodName = "GetCommentsByParentGenusType";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByRecordType {
    static readonly methodName = "GetCommentsByRecordType";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsOnDate {
    static readonly methodName = "GetCommentsOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusTypeOnDate {
    static readonly methodName = "GetCommentsByGenusTypeOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsForCommentor {
    static readonly methodName = "GetCommentsForCommentor";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsForCommentorRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsForCommentorOnDate {
    static readonly methodName = "GetCommentsForCommentorOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsForCommentorOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusTypeForCommentor {
    static readonly methodName = "GetCommentsByGenusTypeForCommentor";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusTypeForCommentorOnDate {
    static readonly methodName = "GetCommentsByGenusTypeForCommentorOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsForReference {
    static readonly methodName = "GetCommentsForReference";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsForReferenceRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsForReferenceOnDate {
    static readonly methodName = "GetCommentsForReferenceOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsForReferenceOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusTypeForReference {
    static readonly methodName = "GetCommentsByGenusTypeForReference";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeForReferenceRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusTypeForReferenceOnDate {
    static readonly methodName = "GetCommentsByGenusTypeForReferenceOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeForReferenceOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsForCommentorAndReference {
    static readonly methodName = "GetCommentsForCommentorAndReference";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsForCommentorAndReferenceRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsForCommentorAndReferenceOnDate {
    static readonly methodName = "GetCommentsForCommentorAndReferenceOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsForCommentorAndReferenceOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusTypeForCommentorAndReference {
    static readonly methodName = "GetCommentsByGenusTypeForCommentorAndReference";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorAndReferenceRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentsByGenusTypeForCommentorAndReferenceOnDate {
    static readonly methodName = "GetCommentsByGenusTypeForCommentorAndReferenceOnDate";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetComments {
    static readonly methodName = "GetComments";
    static readonly service = CommentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
}
export class CommentQuerySession {
  static serviceName = "dlkit.proto.commenting.CommentQuerySession";
}
export namespace CommentQuerySession {
  export class GetBookId {
    static readonly methodName = "GetBookId";
    static readonly service = CommentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookIdRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookIdReply;
  }
  export class GetBook {
    static readonly methodName = "GetBook";
    static readonly service = CommentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookReply;
  }
  export class CanSearchComments {
    static readonly methodName = "CanSearchComments";
    static readonly service = CommentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanSearchCommentsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanSearchCommentsReply;
  }
  export class UseFederatedBookView {
    static readonly methodName = "UseFederatedBookView";
    static readonly service = CommentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseFederatedBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseFederatedBookViewReply;
  }
  export class UseIsolatedBookView {
    static readonly methodName = "UseIsolatedBookView";
    static readonly service = CommentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseIsolatedBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseIsolatedBookViewReply;
  }
  export class GetCommentQuery {
    static readonly methodName = "GetCommentQuery";
    static readonly service = CommentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentQueryRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetCommentQueryReply;
  }
  export class GetCommentsByQuery {
    static readonly methodName = "GetCommentsByQuery";
    static readonly service = CommentQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByQueryRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
}
export class CommentAdminSession {
  static serviceName = "dlkit.proto.commenting.CommentAdminSession";
}
export namespace CommentAdminSession {
  export class GetBookId {
    static readonly methodName = "GetBookId";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookIdRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookIdReply;
  }
  export class GetBook {
    static readonly methodName = "GetBook";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookReply;
  }
  export class CanCreateComments {
    static readonly methodName = "CanCreateComments";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanCreateCommentsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanCreateCommentsReply;
  }
  export class CanCreateCommentWithRecordTypes {
    static readonly methodName = "CanCreateCommentWithRecordTypes";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanCreateCommentWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanCreateCommentWithRecordTypesReply;
  }
  export class GetCommentFormForCreate {
    static readonly methodName = "GetCommentFormForCreate";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentFormForCreateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetCommentFormForCreateReply;
  }
  export class CreateComment {
    static readonly methodName = "CreateComment";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CreateCommentRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CreateCommentReply;
  }
  export class CanUpdateComments {
    static readonly methodName = "CanUpdateComments";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanUpdateCommentsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanUpdateCommentsReply;
  }
  export class GetCommentFormForUpdate {
    static readonly methodName = "GetCommentFormForUpdate";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentFormForUpdateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetCommentFormForUpdateReply;
  }
  export class UpdateComment {
    static readonly methodName = "UpdateComment";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UpdateCommentRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UpdateCommentReply;
  }
  export class CanDeleteComments {
    static readonly methodName = "CanDeleteComments";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanDeleteCommentsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanDeleteCommentsReply;
  }
  export class DeleteComment {
    static readonly methodName = "DeleteComment";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.DeleteCommentRequest;
    static readonly responseType = dlkit_proto_commenting_pb.DeleteCommentReply;
  }
  export class CanManageCommentAliases {
    static readonly methodName = "CanManageCommentAliases";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanManageCommentAliasesRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanManageCommentAliasesReply;
  }
  export class AliasComment {
    static readonly methodName = "AliasComment";
    static readonly service = CommentAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.AliasCommentRequest;
    static readonly responseType = dlkit_proto_commenting_pb.AliasCommentReply;
  }
}
export class CommentBookSession {
  static serviceName = "dlkit.proto.commenting.CommentBookSession";
}
export namespace CommentBookSession {
  export class CanLookupCommentBookMappings {
    static readonly methodName = "CanLookupCommentBookMappings";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanLookupCommentBookMappingsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanLookupCommentBookMappingsReply;
  }
  export class UseComparativeBookView {
    static readonly methodName = "UseComparativeBookView";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseComparativeBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseComparativeBookViewReply;
  }
  export class UsePlenaryBookView {
    static readonly methodName = "UsePlenaryBookView";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UsePlenaryBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UsePlenaryBookViewReply;
  }
  export class GetCommentIdsByBook {
    static readonly methodName = "GetCommentIdsByBook";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentIdsByBookRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetCommentsByBook {
    static readonly methodName = "GetCommentsByBook";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetCommentIdsByBooks {
    static readonly methodName = "GetCommentIdsByBooks";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentIdsByBooksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetCommentsByBooks {
    static readonly methodName = "GetCommentsByBooks";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetCommentsByBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Comment;
  }
  export class GetBookIdsByComment {
    static readonly methodName = "GetBookIdsByComment";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookIdsByCommentRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetBooksByComment {
    static readonly methodName = "GetBooksByComment";
    static readonly service = CommentBookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBooksByCommentRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
}
export class CommentBookAssignmentSession {
  static serviceName = "dlkit.proto.commenting.CommentBookAssignmentSession";
}
export namespace CommentBookAssignmentSession {
  export class CanAssignComments {
    static readonly methodName = "CanAssignComments";
    static readonly service = CommentBookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanAssignCommentsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanAssignCommentsReply;
  }
  export class CanAssignCommentsToBook {
    static readonly methodName = "CanAssignCommentsToBook";
    static readonly service = CommentBookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanAssignCommentsToBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanAssignCommentsToBookReply;
  }
  export class GetAssignableBookIds {
    static readonly methodName = "GetAssignableBookIds";
    static readonly service = CommentBookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetAssignableBookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableBookIdsForComment {
    static readonly methodName = "GetAssignableBookIdsForComment";
    static readonly service = CommentBookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetAssignableBookIdsForCommentRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignCommentToBook {
    static readonly methodName = "AssignCommentToBook";
    static readonly service = CommentBookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.AssignCommentToBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.AssignCommentToBookReply;
  }
  export class UnassignCommentFromBook {
    static readonly methodName = "UnassignCommentFromBook";
    static readonly service = CommentBookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UnassignCommentFromBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UnassignCommentFromBookReply;
  }
  export class ReassignCommentToBook {
    static readonly methodName = "ReassignCommentToBook";
    static readonly service = CommentBookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.ReassignCommentToBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.ReassignCommentToBookReply;
  }
}
export class BookLookupSession {
  static serviceName = "dlkit.proto.commenting.BookLookupSession";
}
export namespace BookLookupSession {
  export class CanLookupBooks {
    static readonly methodName = "CanLookupBooks";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanLookupBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanLookupBooksReply;
  }
  export class UseComparativeBookView {
    static readonly methodName = "UseComparativeBookView";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseComparativeBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseComparativeBookViewReply;
  }
  export class UsePlenaryBookView {
    static readonly methodName = "UsePlenaryBookView";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UsePlenaryBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UsePlenaryBookViewReply;
  }
  export class GetBook {
    static readonly methodName = "GetBook";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookReply;
  }
  export class GetBooksByIds {
    static readonly methodName = "GetBooksByIds";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBooksByIdsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class GetBooksByGenusType {
    static readonly methodName = "GetBooksByGenusType";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBooksByGenusTypeRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class GetBooksByParentGenusType {
    static readonly methodName = "GetBooksByParentGenusType";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBooksByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class GetBooksByRecordType {
    static readonly methodName = "GetBooksByRecordType";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBooksByRecordTypeRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class GetBooksByProvider {
    static readonly methodName = "GetBooksByProvider";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBooksByProviderRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class GetBooks {
    static readonly methodName = "GetBooks";
    static readonly service = BookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
}
export class BookAdminSession {
  static serviceName = "dlkit.proto.commenting.BookAdminSession";
}
export namespace BookAdminSession {
  export class CanCreateBooks {
    static readonly methodName = "CanCreateBooks";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanCreateBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanCreateBooksReply;
  }
  export class CanCreateBookWithRecordTypes {
    static readonly methodName = "CanCreateBookWithRecordTypes";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanCreateBookWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanCreateBookWithRecordTypesReply;
  }
  export class GetBookFormForCreate {
    static readonly methodName = "GetBookFormForCreate";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookFormForCreateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookFormForCreateReply;
  }
  export class CreateBook {
    static readonly methodName = "CreateBook";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CreateBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CreateBookReply;
  }
  export class CanUpdateBooks {
    static readonly methodName = "CanUpdateBooks";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanUpdateBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanUpdateBooksReply;
  }
  export class GetBookFormForUpdate {
    static readonly methodName = "GetBookFormForUpdate";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookFormForUpdateRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookFormForUpdateReply;
  }
  export class UpdateBook {
    static readonly methodName = "UpdateBook";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UpdateBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UpdateBookReply;
  }
  export class CanDeleteBooks {
    static readonly methodName = "CanDeleteBooks";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanDeleteBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanDeleteBooksReply;
  }
  export class DeleteBook {
    static readonly methodName = "DeleteBook";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.DeleteBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.DeleteBookReply;
  }
  export class CanManageBookAliases {
    static readonly methodName = "CanManageBookAliases";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanManageBookAliasesRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanManageBookAliasesReply;
  }
  export class AliasBook {
    static readonly methodName = "AliasBook";
    static readonly service = BookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.AliasBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.AliasBookReply;
  }
}
export class BookHierarchySession {
  static serviceName = "dlkit.proto.commenting.BookHierarchySession";
}
export namespace BookHierarchySession {
  export class GetBookHierarchyId {
    static readonly methodName = "GetBookHierarchyId";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookHierarchyIdRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookHierarchyIdReply;
  }
  export class GetBookHierarchy {
    static readonly methodName = "GetBookHierarchy";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookHierarchyRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookHierarchyReply;
  }
  export class CanAccessBookHierarchy {
    static readonly methodName = "CanAccessBookHierarchy";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanAccessBookHierarchyRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanAccessBookHierarchyReply;
  }
  export class UseComparativeBookView {
    static readonly methodName = "UseComparativeBookView";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UseComparativeBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UseComparativeBookViewReply;
  }
  export class UsePlenaryBookView {
    static readonly methodName = "UsePlenaryBookView";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.UsePlenaryBookViewRequest;
    static readonly responseType = dlkit_proto_commenting_pb.UsePlenaryBookViewReply;
  }
  export class GetRootBookIds {
    static readonly methodName = "GetRootBookIds";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetRootBookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootBooks {
    static readonly methodName = "GetRootBooks";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetRootBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class HasParentBooks {
    static readonly methodName = "HasParentBooks";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.HasParentBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.HasParentBooksReply;
  }
  export class IsParentOfBook {
    static readonly methodName = "IsParentOfBook";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.IsParentOfBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.IsParentOfBookReply;
  }
  export class GetParentBookIds {
    static readonly methodName = "GetParentBookIds";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetParentBookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentBooks {
    static readonly methodName = "GetParentBooks";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetParentBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class IsAncestorOfBook {
    static readonly methodName = "IsAncestorOfBook";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.IsAncestorOfBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.IsAncestorOfBookReply;
  }
  export class HasChildBooks {
    static readonly methodName = "HasChildBooks";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.HasChildBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.HasChildBooksReply;
  }
  export class IsChildOfBook {
    static readonly methodName = "IsChildOfBook";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.IsChildOfBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.IsChildOfBookReply;
  }
  export class GetChildBookIds {
    static readonly methodName = "GetChildBookIds";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetChildBookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildBooks {
    static readonly methodName = "GetChildBooks";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_commenting_pb.GetChildBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.Book;
  }
  export class IsDescendantOfBook {
    static readonly methodName = "IsDescendantOfBook";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.IsDescendantOfBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.IsDescendantOfBookReply;
  }
  export class GetBookNodeIds {
    static readonly methodName = "GetBookNodeIds";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookNodeIdsRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookNodeIdsReply;
  }
  export class GetBookNodes {
    static readonly methodName = "GetBookNodes";
    static readonly service = BookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookNodesRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookNodesReply;
  }
}
export class BookHierarchyDesignSession {
  static serviceName = "dlkit.proto.commenting.BookHierarchyDesignSession";
}
export namespace BookHierarchyDesignSession {
  export class GetBookHierarchyId {
    static readonly methodName = "GetBookHierarchyId";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookHierarchyIdRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookHierarchyIdReply;
  }
  export class GetBookHierarchy {
    static readonly methodName = "GetBookHierarchy";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.GetBookHierarchyRequest;
    static readonly responseType = dlkit_proto_commenting_pb.GetBookHierarchyReply;
  }
  export class CanModifyBookHierarchy {
    static readonly methodName = "CanModifyBookHierarchy";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.CanModifyBookHierarchyRequest;
    static readonly responseType = dlkit_proto_commenting_pb.CanModifyBookHierarchyReply;
  }
  export class AddRootBook {
    static readonly methodName = "AddRootBook";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.AddRootBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.AddRootBookReply;
  }
  export class RemoveRootBook {
    static readonly methodName = "RemoveRootBook";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.RemoveRootBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.RemoveRootBookReply;
  }
  export class AddChildBook {
    static readonly methodName = "AddChildBook";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.AddChildBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.AddChildBookReply;
  }
  export class RemoveChildBook {
    static readonly methodName = "RemoveChildBook";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.RemoveChildBookRequest;
    static readonly responseType = dlkit_proto_commenting_pb.RemoveChildBookReply;
  }
  export class RemoveChildBooks {
    static readonly methodName = "RemoveChildBooks";
    static readonly service = BookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_commenting_pb.RemoveChildBooksRequest;
    static readonly responseType = dlkit_proto_commenting_pb.RemoveChildBooksReply;
  }
}
