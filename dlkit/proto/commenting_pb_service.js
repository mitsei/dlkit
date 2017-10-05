// package: dlkit.proto.commenting
// file: dlkit/proto/commenting.proto

var jspb = require("google-protobuf");
var dlkit_proto_commenting_pb = require("../../dlkit/proto/commenting_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var dlkit_proto_resource_pb = require("../../dlkit/proto/resource_pb");
var google_protobuf_timestamp_pb = require("google-protobuf/google/protobuf/timestamp_pb");
var CommentLookupSession = {
  serviceName: "dlkit.proto.commenting.CommentLookupSession"
};
CommentLookupSession.GetBookId = {
  methodName: "GetBookId",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookIdRequest,
  responseType: dlkit_proto_commenting_pb.GetBookIdReply
};
CommentLookupSession.GetBook = {
  methodName: "GetBook",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookRequest,
  responseType: dlkit_proto_commenting_pb.GetBookReply
};
CommentLookupSession.CanLookupComments = {
  methodName: "CanLookupComments",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanLookupCommentsRequest,
  responseType: dlkit_proto_commenting_pb.CanLookupCommentsReply
};
CommentLookupSession.UseComparativeCommentView = {
  methodName: "UseComparativeCommentView",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseComparativeCommentViewRequest,
  responseType: dlkit_proto_commenting_pb.UseComparativeCommentViewReply
};
CommentLookupSession.UsePlenaryCommentView = {
  methodName: "UsePlenaryCommentView",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UsePlenaryCommentViewRequest,
  responseType: dlkit_proto_commenting_pb.UsePlenaryCommentViewReply
};
CommentLookupSession.UseFederatedBookView = {
  methodName: "UseFederatedBookView",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseFederatedBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UseFederatedBookViewReply
};
CommentLookupSession.UseIsolatedBookView = {
  methodName: "UseIsolatedBookView",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseIsolatedBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UseIsolatedBookViewReply
};
CommentLookupSession.UseEffectiveCommentView = {
  methodName: "UseEffectiveCommentView",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseEffectiveCommentViewRequest,
  responseType: dlkit_proto_commenting_pb.UseEffectiveCommentViewReply
};
CommentLookupSession.UseAnyEffectiveCommentView = {
  methodName: "UseAnyEffectiveCommentView",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseAnyEffectiveCommentViewRequest,
  responseType: dlkit_proto_commenting_pb.UseAnyEffectiveCommentViewReply
};
CommentLookupSession.GetComment = {
  methodName: "GetComment",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetCommentRequest,
  responseType: dlkit_proto_commenting_pb.GetCommentReply
};
CommentLookupSession.GetCommentsByIds = {
  methodName: "GetCommentsByIds",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByIdsRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusType = {
  methodName: "GetCommentsByGenusType",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByParentGenusType = {
  methodName: "GetCommentsByParentGenusType",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByParentGenusTypeRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByRecordType = {
  methodName: "GetCommentsByRecordType",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByRecordTypeRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsOnDate = {
  methodName: "GetCommentsOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusTypeOnDate = {
  methodName: "GetCommentsByGenusTypeOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsForCommentor = {
  methodName: "GetCommentsForCommentor",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsForCommentorRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsForCommentorOnDate = {
  methodName: "GetCommentsForCommentorOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsForCommentorOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusTypeForCommentor = {
  methodName: "GetCommentsByGenusTypeForCommentor",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusTypeForCommentorOnDate = {
  methodName: "GetCommentsByGenusTypeForCommentorOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsForReference = {
  methodName: "GetCommentsForReference",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsForReferenceRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsForReferenceOnDate = {
  methodName: "GetCommentsForReferenceOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsForReferenceOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusTypeForReference = {
  methodName: "GetCommentsByGenusTypeForReference",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeForReferenceRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusTypeForReferenceOnDate = {
  methodName: "GetCommentsByGenusTypeForReferenceOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeForReferenceOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsForCommentorAndReference = {
  methodName: "GetCommentsForCommentorAndReference",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsForCommentorAndReferenceRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsForCommentorAndReferenceOnDate = {
  methodName: "GetCommentsForCommentorAndReferenceOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsForCommentorAndReferenceOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusTypeForCommentorAndReference = {
  methodName: "GetCommentsByGenusTypeForCommentorAndReference",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorAndReferenceRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetCommentsByGenusTypeForCommentorAndReferenceOnDate = {
  methodName: "GetCommentsByGenusTypeForCommentorAndReferenceOnDate",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByGenusTypeForCommentorAndReferenceOnDateRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentLookupSession.GetComments = {
  methodName: "GetComments",
  service: CommentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
var CommentQuerySession = {
  serviceName: "dlkit.proto.commenting.CommentQuerySession"
};
CommentQuerySession.GetBookId = {
  methodName: "GetBookId",
  service: CommentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookIdRequest,
  responseType: dlkit_proto_commenting_pb.GetBookIdReply
};
CommentQuerySession.GetBook = {
  methodName: "GetBook",
  service: CommentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookRequest,
  responseType: dlkit_proto_commenting_pb.GetBookReply
};
CommentQuerySession.CanSearchComments = {
  methodName: "CanSearchComments",
  service: CommentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanSearchCommentsRequest,
  responseType: dlkit_proto_commenting_pb.CanSearchCommentsReply
};
CommentQuerySession.UseFederatedBookView = {
  methodName: "UseFederatedBookView",
  service: CommentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseFederatedBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UseFederatedBookViewReply
};
CommentQuerySession.UseIsolatedBookView = {
  methodName: "UseIsolatedBookView",
  service: CommentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseIsolatedBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UseIsolatedBookViewReply
};
CommentQuerySession.GetCommentQuery = {
  methodName: "GetCommentQuery",
  service: CommentQuerySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetCommentQueryRequest,
  responseType: dlkit_proto_commenting_pb.GetCommentQueryReply
};
CommentQuerySession.GetCommentsByQuery = {
  methodName: "GetCommentsByQuery",
  service: CommentQuerySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByQueryRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
var CommentAdminSession = {
  serviceName: "dlkit.proto.commenting.CommentAdminSession"
};
CommentAdminSession.GetBookId = {
  methodName: "GetBookId",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookIdRequest,
  responseType: dlkit_proto_commenting_pb.GetBookIdReply
};
CommentAdminSession.GetBook = {
  methodName: "GetBook",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookRequest,
  responseType: dlkit_proto_commenting_pb.GetBookReply
};
CommentAdminSession.CanCreateComments = {
  methodName: "CanCreateComments",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanCreateCommentsRequest,
  responseType: dlkit_proto_commenting_pb.CanCreateCommentsReply
};
CommentAdminSession.CanCreateCommentWithRecordTypes = {
  methodName: "CanCreateCommentWithRecordTypes",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanCreateCommentWithRecordTypesRequest,
  responseType: dlkit_proto_commenting_pb.CanCreateCommentWithRecordTypesReply
};
CommentAdminSession.GetCommentFormForCreate = {
  methodName: "GetCommentFormForCreate",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetCommentFormForCreateRequest,
  responseType: dlkit_proto_commenting_pb.GetCommentFormForCreateReply
};
CommentAdminSession.CreateComment = {
  methodName: "CreateComment",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CreateCommentRequest,
  responseType: dlkit_proto_commenting_pb.CreateCommentReply
};
CommentAdminSession.CanUpdateComments = {
  methodName: "CanUpdateComments",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanUpdateCommentsRequest,
  responseType: dlkit_proto_commenting_pb.CanUpdateCommentsReply
};
CommentAdminSession.GetCommentFormForUpdate = {
  methodName: "GetCommentFormForUpdate",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetCommentFormForUpdateRequest,
  responseType: dlkit_proto_commenting_pb.GetCommentFormForUpdateReply
};
CommentAdminSession.UpdateComment = {
  methodName: "UpdateComment",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UpdateCommentRequest,
  responseType: dlkit_proto_commenting_pb.UpdateCommentReply
};
CommentAdminSession.CanDeleteComments = {
  methodName: "CanDeleteComments",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanDeleteCommentsRequest,
  responseType: dlkit_proto_commenting_pb.CanDeleteCommentsReply
};
CommentAdminSession.DeleteComment = {
  methodName: "DeleteComment",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.DeleteCommentRequest,
  responseType: dlkit_proto_commenting_pb.DeleteCommentReply
};
CommentAdminSession.CanManageCommentAliases = {
  methodName: "CanManageCommentAliases",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanManageCommentAliasesRequest,
  responseType: dlkit_proto_commenting_pb.CanManageCommentAliasesReply
};
CommentAdminSession.AliasComment = {
  methodName: "AliasComment",
  service: CommentAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.AliasCommentRequest,
  responseType: dlkit_proto_commenting_pb.AliasCommentReply
};
var CommentBookSession = {
  serviceName: "dlkit.proto.commenting.CommentBookSession"
};
CommentBookSession.CanLookupCommentBookMappings = {
  methodName: "CanLookupCommentBookMappings",
  service: CommentBookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanLookupCommentBookMappingsRequest,
  responseType: dlkit_proto_commenting_pb.CanLookupCommentBookMappingsReply
};
CommentBookSession.UseComparativeBookView = {
  methodName: "UseComparativeBookView",
  service: CommentBookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseComparativeBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UseComparativeBookViewReply
};
CommentBookSession.UsePlenaryBookView = {
  methodName: "UsePlenaryBookView",
  service: CommentBookSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UsePlenaryBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UsePlenaryBookViewReply
};
CommentBookSession.GetCommentIdsByBook = {
  methodName: "GetCommentIdsByBook",
  service: CommentBookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentIdsByBookRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CommentBookSession.GetCommentsByBook = {
  methodName: "GetCommentsByBook",
  service: CommentBookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByBookRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentBookSession.GetCommentIdsByBooks = {
  methodName: "GetCommentIdsByBooks",
  service: CommentBookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentIdsByBooksRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CommentBookSession.GetCommentsByBooks = {
  methodName: "GetCommentsByBooks",
  service: CommentBookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetCommentsByBooksRequest,
  responseType: dlkit_proto_commenting_pb.Comment
};
CommentBookSession.GetBookIdsByComment = {
  methodName: "GetBookIdsByComment",
  service: CommentBookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBookIdsByCommentRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CommentBookSession.GetBooksByComment = {
  methodName: "GetBooksByComment",
  service: CommentBookSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBooksByCommentRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
var CommentBookAssignmentSession = {
  serviceName: "dlkit.proto.commenting.CommentBookAssignmentSession"
};
CommentBookAssignmentSession.CanAssignComments = {
  methodName: "CanAssignComments",
  service: CommentBookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanAssignCommentsRequest,
  responseType: dlkit_proto_commenting_pb.CanAssignCommentsReply
};
CommentBookAssignmentSession.CanAssignCommentsToBook = {
  methodName: "CanAssignCommentsToBook",
  service: CommentBookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanAssignCommentsToBookRequest,
  responseType: dlkit_proto_commenting_pb.CanAssignCommentsToBookReply
};
CommentBookAssignmentSession.GetAssignableBookIds = {
  methodName: "GetAssignableBookIds",
  service: CommentBookAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetAssignableBookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CommentBookAssignmentSession.GetAssignableBookIdsForComment = {
  methodName: "GetAssignableBookIdsForComment",
  service: CommentBookAssignmentSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetAssignableBookIdsForCommentRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
CommentBookAssignmentSession.AssignCommentToBook = {
  methodName: "AssignCommentToBook",
  service: CommentBookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.AssignCommentToBookRequest,
  responseType: dlkit_proto_commenting_pb.AssignCommentToBookReply
};
CommentBookAssignmentSession.UnassignCommentFromBook = {
  methodName: "UnassignCommentFromBook",
  service: CommentBookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UnassignCommentFromBookRequest,
  responseType: dlkit_proto_commenting_pb.UnassignCommentFromBookReply
};
CommentBookAssignmentSession.ReassignCommentToBook = {
  methodName: "ReassignCommentToBook",
  service: CommentBookAssignmentSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.ReassignCommentToBookRequest,
  responseType: dlkit_proto_commenting_pb.ReassignCommentToBookReply
};
var BookLookupSession = {
  serviceName: "dlkit.proto.commenting.BookLookupSession"
};
BookLookupSession.CanLookupBooks = {
  methodName: "CanLookupBooks",
  service: BookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanLookupBooksRequest,
  responseType: dlkit_proto_commenting_pb.CanLookupBooksReply
};
BookLookupSession.UseComparativeBookView = {
  methodName: "UseComparativeBookView",
  service: BookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseComparativeBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UseComparativeBookViewReply
};
BookLookupSession.UsePlenaryBookView = {
  methodName: "UsePlenaryBookView",
  service: BookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UsePlenaryBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UsePlenaryBookViewReply
};
BookLookupSession.GetBook = {
  methodName: "GetBook",
  service: BookLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookRequest,
  responseType: dlkit_proto_commenting_pb.GetBookReply
};
BookLookupSession.GetBooksByIds = {
  methodName: "GetBooksByIds",
  service: BookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBooksByIdsRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookLookupSession.GetBooksByGenusType = {
  methodName: "GetBooksByGenusType",
  service: BookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBooksByGenusTypeRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookLookupSession.GetBooksByParentGenusType = {
  methodName: "GetBooksByParentGenusType",
  service: BookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBooksByParentGenusTypeRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookLookupSession.GetBooksByRecordType = {
  methodName: "GetBooksByRecordType",
  service: BookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBooksByRecordTypeRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookLookupSession.GetBooksByProvider = {
  methodName: "GetBooksByProvider",
  service: BookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBooksByProviderRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookLookupSession.GetBooks = {
  methodName: "GetBooks",
  service: BookLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetBooksRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
var BookAdminSession = {
  serviceName: "dlkit.proto.commenting.BookAdminSession"
};
BookAdminSession.CanCreateBooks = {
  methodName: "CanCreateBooks",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanCreateBooksRequest,
  responseType: dlkit_proto_commenting_pb.CanCreateBooksReply
};
BookAdminSession.CanCreateBookWithRecordTypes = {
  methodName: "CanCreateBookWithRecordTypes",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanCreateBookWithRecordTypesRequest,
  responseType: dlkit_proto_commenting_pb.CanCreateBookWithRecordTypesReply
};
BookAdminSession.GetBookFormForCreate = {
  methodName: "GetBookFormForCreate",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookFormForCreateRequest,
  responseType: dlkit_proto_commenting_pb.GetBookFormForCreateReply
};
BookAdminSession.CreateBook = {
  methodName: "CreateBook",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CreateBookRequest,
  responseType: dlkit_proto_commenting_pb.CreateBookReply
};
BookAdminSession.CanUpdateBooks = {
  methodName: "CanUpdateBooks",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanUpdateBooksRequest,
  responseType: dlkit_proto_commenting_pb.CanUpdateBooksReply
};
BookAdminSession.GetBookFormForUpdate = {
  methodName: "GetBookFormForUpdate",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookFormForUpdateRequest,
  responseType: dlkit_proto_commenting_pb.GetBookFormForUpdateReply
};
BookAdminSession.UpdateBook = {
  methodName: "UpdateBook",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UpdateBookRequest,
  responseType: dlkit_proto_commenting_pb.UpdateBookReply
};
BookAdminSession.CanDeleteBooks = {
  methodName: "CanDeleteBooks",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanDeleteBooksRequest,
  responseType: dlkit_proto_commenting_pb.CanDeleteBooksReply
};
BookAdminSession.DeleteBook = {
  methodName: "DeleteBook",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.DeleteBookRequest,
  responseType: dlkit_proto_commenting_pb.DeleteBookReply
};
BookAdminSession.CanManageBookAliases = {
  methodName: "CanManageBookAliases",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanManageBookAliasesRequest,
  responseType: dlkit_proto_commenting_pb.CanManageBookAliasesReply
};
BookAdminSession.AliasBook = {
  methodName: "AliasBook",
  service: BookAdminSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.AliasBookRequest,
  responseType: dlkit_proto_commenting_pb.AliasBookReply
};
var BookHierarchySession = {
  serviceName: "dlkit.proto.commenting.BookHierarchySession"
};
BookHierarchySession.GetBookHierarchyId = {
  methodName: "GetBookHierarchyId",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookHierarchyIdRequest,
  responseType: dlkit_proto_commenting_pb.GetBookHierarchyIdReply
};
BookHierarchySession.GetBookHierarchy = {
  methodName: "GetBookHierarchy",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookHierarchyRequest,
  responseType: dlkit_proto_commenting_pb.GetBookHierarchyReply
};
BookHierarchySession.CanAccessBookHierarchy = {
  methodName: "CanAccessBookHierarchy",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanAccessBookHierarchyRequest,
  responseType: dlkit_proto_commenting_pb.CanAccessBookHierarchyReply
};
BookHierarchySession.UseComparativeBookView = {
  methodName: "UseComparativeBookView",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UseComparativeBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UseComparativeBookViewReply
};
BookHierarchySession.UsePlenaryBookView = {
  methodName: "UsePlenaryBookView",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.UsePlenaryBookViewRequest,
  responseType: dlkit_proto_commenting_pb.UsePlenaryBookViewReply
};
BookHierarchySession.GetRootBookIds = {
  methodName: "GetRootBookIds",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetRootBookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BookHierarchySession.GetRootBooks = {
  methodName: "GetRootBooks",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetRootBooksRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookHierarchySession.HasParentBooks = {
  methodName: "HasParentBooks",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.HasParentBooksRequest,
  responseType: dlkit_proto_commenting_pb.HasParentBooksReply
};
BookHierarchySession.IsParentOfBook = {
  methodName: "IsParentOfBook",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.IsParentOfBookRequest,
  responseType: dlkit_proto_commenting_pb.IsParentOfBookReply
};
BookHierarchySession.GetParentBookIds = {
  methodName: "GetParentBookIds",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetParentBookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BookHierarchySession.GetParentBooks = {
  methodName: "GetParentBooks",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetParentBooksRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookHierarchySession.IsAncestorOfBook = {
  methodName: "IsAncestorOfBook",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.IsAncestorOfBookRequest,
  responseType: dlkit_proto_commenting_pb.IsAncestorOfBookReply
};
BookHierarchySession.HasChildBooks = {
  methodName: "HasChildBooks",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.HasChildBooksRequest,
  responseType: dlkit_proto_commenting_pb.HasChildBooksReply
};
BookHierarchySession.IsChildOfBook = {
  methodName: "IsChildOfBook",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.IsChildOfBookRequest,
  responseType: dlkit_proto_commenting_pb.IsChildOfBookReply
};
BookHierarchySession.GetChildBookIds = {
  methodName: "GetChildBookIds",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetChildBookIdsRequest,
  responseType: dlkit_primordium_id_primitives_pb.Id
};
BookHierarchySession.GetChildBooks = {
  methodName: "GetChildBooks",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_commenting_pb.GetChildBooksRequest,
  responseType: dlkit_proto_commenting_pb.Book
};
BookHierarchySession.IsDescendantOfBook = {
  methodName: "IsDescendantOfBook",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.IsDescendantOfBookRequest,
  responseType: dlkit_proto_commenting_pb.IsDescendantOfBookReply
};
BookHierarchySession.GetBookNodeIds = {
  methodName: "GetBookNodeIds",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookNodeIdsRequest,
  responseType: dlkit_proto_commenting_pb.GetBookNodeIdsReply
};
BookHierarchySession.GetBookNodes = {
  methodName: "GetBookNodes",
  service: BookHierarchySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookNodesRequest,
  responseType: dlkit_proto_commenting_pb.GetBookNodesReply
};
var BookHierarchyDesignSession = {
  serviceName: "dlkit.proto.commenting.BookHierarchyDesignSession"
};
BookHierarchyDesignSession.GetBookHierarchyId = {
  methodName: "GetBookHierarchyId",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookHierarchyIdRequest,
  responseType: dlkit_proto_commenting_pb.GetBookHierarchyIdReply
};
BookHierarchyDesignSession.GetBookHierarchy = {
  methodName: "GetBookHierarchy",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.GetBookHierarchyRequest,
  responseType: dlkit_proto_commenting_pb.GetBookHierarchyReply
};
BookHierarchyDesignSession.CanModifyBookHierarchy = {
  methodName: "CanModifyBookHierarchy",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.CanModifyBookHierarchyRequest,
  responseType: dlkit_proto_commenting_pb.CanModifyBookHierarchyReply
};
BookHierarchyDesignSession.AddRootBook = {
  methodName: "AddRootBook",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.AddRootBookRequest,
  responseType: dlkit_proto_commenting_pb.AddRootBookReply
};
BookHierarchyDesignSession.RemoveRootBook = {
  methodName: "RemoveRootBook",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.RemoveRootBookRequest,
  responseType: dlkit_proto_commenting_pb.RemoveRootBookReply
};
BookHierarchyDesignSession.AddChildBook = {
  methodName: "AddChildBook",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.AddChildBookRequest,
  responseType: dlkit_proto_commenting_pb.AddChildBookReply
};
BookHierarchyDesignSession.RemoveChildBook = {
  methodName: "RemoveChildBook",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.RemoveChildBookRequest,
  responseType: dlkit_proto_commenting_pb.RemoveChildBookReply
};
BookHierarchyDesignSession.RemoveChildBooks = {
  methodName: "RemoveChildBooks",
  service: BookHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_commenting_pb.RemoveChildBooksRequest,
  responseType: dlkit_proto_commenting_pb.RemoveChildBooksReply
};
module.exports = {
  CommentLookupSession: CommentLookupSession,
  CommentQuerySession: CommentQuerySession,
  CommentAdminSession: CommentAdminSession,
  CommentBookSession: CommentBookSession,
  CommentBookAssignmentSession: CommentBookAssignmentSession,
  BookLookupSession: BookLookupSession,
  BookAdminSession: BookAdminSession,
  BookHierarchySession: BookHierarchySession,
  BookHierarchyDesignSession: BookHierarchyDesignSession,
};

