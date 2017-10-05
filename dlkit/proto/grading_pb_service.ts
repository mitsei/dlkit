// package: dlkit.proto.grading
// file: dlkit/proto/grading.proto

import * as dlkit_proto_grading_pb from "../../dlkit/proto/grading_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";
export class GradeSystemLookupSession {
  static serviceName = "dlkit.proto.grading.GradeSystemLookupSession";
}
export namespace GradeSystemLookupSession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanLookupGradeSystems {
    static readonly methodName = "CanLookupGradeSystems";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanLookupGradeSystemsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanLookupGradeSystemsReply;
  }
  export class UseComparativeGradeSystemView {
    static readonly methodName = "UseComparativeGradeSystemView";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseComparativeGradeSystemViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseComparativeGradeSystemViewReply;
  }
  export class UsePlenaryGradeSystemView {
    static readonly methodName = "UsePlenaryGradeSystemView";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UsePlenaryGradeSystemViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UsePlenaryGradeSystemViewReply;
  }
  export class UseFederatedGradebookView {
    static readonly methodName = "UseFederatedGradebookView";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseFederatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseFederatedGradebookViewReply;
  }
  export class UseIsolatedGradebookView {
    static readonly methodName = "UseIsolatedGradebookView";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseIsolatedGradebookViewReply;
  }
  export class GetGradeSystem {
    static readonly methodName = "GetGradeSystem";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeSystemReply;
  }
  export class GetGradeSystemByGrade {
    static readonly methodName = "GetGradeSystemByGrade";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemByGradeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeSystemByGradeReply;
  }
  export class GetGradeSystemsByIds {
    static readonly methodName = "GetGradeSystemsByIds";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsByIdsRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
  export class GetGradeSystemsByGenusType {
    static readonly methodName = "GetGradeSystemsByGenusType";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
  export class GetGradeSystemsByParentGenusType {
    static readonly methodName = "GetGradeSystemsByParentGenusType";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
  export class GetGradeSystemsByRecordType {
    static readonly methodName = "GetGradeSystemsByRecordType";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
  export class GetGradeSystems {
    static readonly methodName = "GetGradeSystems";
    static readonly service = GradeSystemLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
}
export class GradeSystemQuerySession {
  static serviceName = "dlkit.proto.grading.GradeSystemQuerySession";
}
export namespace GradeSystemQuerySession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradeSystemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradeSystemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanSearchGradeSystems {
    static readonly methodName = "CanSearchGradeSystems";
    static readonly service = GradeSystemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanSearchGradeSystemsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanSearchGradeSystemsReply;
  }
  export class UseFederatedGradebookView {
    static readonly methodName = "UseFederatedGradebookView";
    static readonly service = GradeSystemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseFederatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseFederatedGradebookViewReply;
  }
  export class UseIsolatedGradebookView {
    static readonly methodName = "UseIsolatedGradebookView";
    static readonly service = GradeSystemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseIsolatedGradebookViewReply;
  }
  export class GetGradeSystemQuery {
    static readonly methodName = "GetGradeSystemQuery";
    static readonly service = GradeSystemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemQueryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeSystemQueryReply;
  }
  export class GetGradeSystemsByQuery {
    static readonly methodName = "GetGradeSystemsByQuery";
    static readonly service = GradeSystemQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsByQueryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
}
export class GradeSystemAdminSession {
  static serviceName = "dlkit.proto.grading.GradeSystemAdminSession";
}
export namespace GradeSystemAdminSession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanCreateGradeSystems {
    static readonly methodName = "CanCreateGradeSystems";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradeSystemsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradeSystemsReply;
  }
  export class CanCreateGradeSystemWithRecordTypes {
    static readonly methodName = "CanCreateGradeSystemWithRecordTypes";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradeSystemWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradeSystemWithRecordTypesReply;
  }
  export class GetGradeSystemFormForCreate {
    static readonly methodName = "GetGradeSystemFormForCreate";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemFormForCreateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeSystemFormForCreateReply;
  }
  export class CreateGradeSystem {
    static readonly methodName = "CreateGradeSystem";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CreateGradeSystemRequest;
    static readonly responseType = dlkit_proto_grading_pb.CreateGradeSystemReply;
  }
  export class CanUpdateGradeSystems {
    static readonly methodName = "CanUpdateGradeSystems";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanUpdateGradeSystemsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanUpdateGradeSystemsReply;
  }
  export class GetGradeSystemFormForUpdate {
    static readonly methodName = "GetGradeSystemFormForUpdate";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemFormForUpdateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeSystemFormForUpdateReply;
  }
  export class UpdateGradeSystem {
    static readonly methodName = "UpdateGradeSystem";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UpdateGradeSystemRequest;
    static readonly responseType = dlkit_proto_grading_pb.UpdateGradeSystemReply;
  }
  export class CanDeleteGradeSystems {
    static readonly methodName = "CanDeleteGradeSystems";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanDeleteGradeSystemsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanDeleteGradeSystemsReply;
  }
  export class DeleteGradeSystem {
    static readonly methodName = "DeleteGradeSystem";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.DeleteGradeSystemRequest;
    static readonly responseType = dlkit_proto_grading_pb.DeleteGradeSystemReply;
  }
  export class CanManageGradeSystemAliases {
    static readonly methodName = "CanManageGradeSystemAliases";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanManageGradeSystemAliasesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanManageGradeSystemAliasesReply;
  }
  export class AliasGradeSystem {
    static readonly methodName = "AliasGradeSystem";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AliasGradeSystemRequest;
    static readonly responseType = dlkit_proto_grading_pb.AliasGradeSystemReply;
  }
  export class CanCreateGrades {
    static readonly methodName = "CanCreateGrades";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradesReply;
  }
  export class CanCreateGradeWithRecordTypes {
    static readonly methodName = "CanCreateGradeWithRecordTypes";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradeWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradeWithRecordTypesReply;
  }
  export class GetGradeFormForCreate {
    static readonly methodName = "GetGradeFormForCreate";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeFormForCreateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeFormForCreateReply;
  }
  export class CreateGrade {
    static readonly methodName = "CreateGrade";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CreateGradeRequest;
    static readonly responseType = dlkit_proto_grading_pb.CreateGradeReply;
  }
  export class CanUpdateGrades {
    static readonly methodName = "CanUpdateGrades";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanUpdateGradesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanUpdateGradesReply;
  }
  export class GetGradeFormForUpdate {
    static readonly methodName = "GetGradeFormForUpdate";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeFormForUpdateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeFormForUpdateReply;
  }
  export class UpdateGrade {
    static readonly methodName = "UpdateGrade";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UpdateGradeRequest;
    static readonly responseType = dlkit_proto_grading_pb.UpdateGradeReply;
  }
  export class CanDeleteGrades {
    static readonly methodName = "CanDeleteGrades";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanDeleteGradesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanDeleteGradesReply;
  }
  export class DeleteGrade {
    static readonly methodName = "DeleteGrade";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.DeleteGradeRequest;
    static readonly responseType = dlkit_proto_grading_pb.DeleteGradeReply;
  }
  export class CanManageGradeAliases {
    static readonly methodName = "CanManageGradeAliases";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanManageGradeAliasesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanManageGradeAliasesReply;
  }
  export class AliasGrade {
    static readonly methodName = "AliasGrade";
    static readonly service = GradeSystemAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AliasGradeRequest;
    static readonly responseType = dlkit_proto_grading_pb.AliasGradeReply;
  }
}
export class GradeSystemGradebookSession {
  static serviceName = "dlkit.proto.grading.GradeSystemGradebookSession";
}
export namespace GradeSystemGradebookSession {
  export class UseComparativeGradebookView {
    static readonly methodName = "UseComparativeGradebookView";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseComparativeGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseComparativeGradebookViewReply;
  }
  export class UsePlenaryGradebookView {
    static readonly methodName = "UsePlenaryGradebookView";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UsePlenaryGradebookViewReply;
  }
  export class CanLookupGradeSystemGradebookMappings {
    static readonly methodName = "CanLookupGradeSystemGradebookMappings";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanLookupGradeSystemGradebookMappingsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanLookupGradeSystemGradebookMappingsReply;
  }
  export class GetGradeSystemIdsByGradebook {
    static readonly methodName = "GetGradeSystemIdsByGradebook";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemIdsByGradebookRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetGradeSystemsByGradebook {
    static readonly methodName = "GetGradeSystemsByGradebook";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsByGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
  export class GetGradeSystemIdsByGradebooks {
    static readonly methodName = "GetGradeSystemIdsByGradebooks";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemIdsByGradebooksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetGradeSystemsByGradebooks {
    static readonly methodName = "GetGradeSystemsByGradebooks";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeSystemsByGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeSystem;
  }
  export class GetGradebookIdsByGradeSystem {
    static readonly methodName = "GetGradebookIdsByGradeSystem";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdsByGradeSystemRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetGradebooksByGradeSystem {
    static readonly methodName = "GetGradebooksByGradeSystem";
    static readonly service = GradeSystemGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksByGradeSystemRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
}
export class GradeSystemGradebookAssignmentSession {
  static serviceName = "dlkit.proto.grading.GradeSystemGradebookAssignmentSession";
}
export namespace GradeSystemGradebookAssignmentSession {
  export class CanAssignGradeSystem {
    static readonly methodName = "CanAssignGradeSystem";
    static readonly service = GradeSystemGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanAssignGradeSystemRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanAssignGradeSystemReply;
  }
  export class CanAssignGradeSystemsToGradebook {
    static readonly methodName = "CanAssignGradeSystemsToGradebook";
    static readonly service = GradeSystemGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanAssignGradeSystemsToGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanAssignGradeSystemsToGradebookReply;
  }
  export class GetAssignableGradebookIds {
    static readonly methodName = "GetAssignableGradebookIds";
    static readonly service = GradeSystemGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetAssignableGradebookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableGradebookIdsForGradeSystem {
    static readonly methodName = "GetAssignableGradebookIdsForGradeSystem";
    static readonly service = GradeSystemGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetAssignableGradebookIdsForGradeSystemRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignGradeSystemToGradebook {
    static readonly methodName = "AssignGradeSystemToGradebook";
    static readonly service = GradeSystemGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AssignGradeSystemToGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.AssignGradeSystemToGradebookReply;
  }
  export class UnassignGradeSystemFromGradebook {
    static readonly methodName = "UnassignGradeSystemFromGradebook";
    static readonly service = GradeSystemGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UnassignGradeSystemFromGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.UnassignGradeSystemFromGradebookReply;
  }
}
export class GradeEntryLookupSession {
  static serviceName = "dlkit.proto.grading.GradeEntryLookupSession";
}
export namespace GradeEntryLookupSession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanLookupGradeEntries {
    static readonly methodName = "CanLookupGradeEntries";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanLookupGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanLookupGradeEntriesReply;
  }
  export class UseComparativeGradeEntryView {
    static readonly methodName = "UseComparativeGradeEntryView";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseComparativeGradeEntryViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseComparativeGradeEntryViewReply;
  }
  export class UsePlenaryGradeEntryView {
    static readonly methodName = "UsePlenaryGradeEntryView";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UsePlenaryGradeEntryViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UsePlenaryGradeEntryViewReply;
  }
  export class UseFederatedGradebookView {
    static readonly methodName = "UseFederatedGradebookView";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseFederatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseFederatedGradebookViewReply;
  }
  export class UseIsolatedGradebookView {
    static readonly methodName = "UseIsolatedGradebookView";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseIsolatedGradebookViewReply;
  }
  export class UseEffectiveGradeEntryView {
    static readonly methodName = "UseEffectiveGradeEntryView";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseEffectiveGradeEntryViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseEffectiveGradeEntryViewReply;
  }
  export class UseAnyEffectiveGradeEntryView {
    static readonly methodName = "UseAnyEffectiveGradeEntryView";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseAnyEffectiveGradeEntryViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseAnyEffectiveGradeEntryViewReply;
  }
  export class GetGradeEntry {
    static readonly methodName = "GetGradeEntry";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeEntryReply;
  }
  export class GetGradeEntriesByIds {
    static readonly methodName = "GetGradeEntriesByIds";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesByIdsRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesByGenusType {
    static readonly methodName = "GetGradeEntriesByGenusType";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesByParentGenusType {
    static readonly methodName = "GetGradeEntriesByParentGenusType";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesByRecordType {
    static readonly methodName = "GetGradeEntriesByRecordType";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesOnDate {
    static readonly methodName = "GetGradeEntriesOnDate";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesOnDateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesForGradebookColumn {
    static readonly methodName = "GetGradeEntriesForGradebookColumn";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesForGradebookColumnOnDate {
    static readonly methodName = "GetGradeEntriesForGradebookColumnOnDate";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnOnDateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesForResource {
    static readonly methodName = "GetGradeEntriesForResource";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesForResourceRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesForResourceOnDate {
    static readonly methodName = "GetGradeEntriesForResourceOnDate";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesForResourceOnDateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesForGradebookColumnAndResource {
    static readonly methodName = "GetGradeEntriesForGradebookColumnAndResource";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnAndResourceRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesForGradebookColumnAndResourceOnDate {
    static readonly methodName = "GetGradeEntriesForGradebookColumnAndResourceOnDate";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesForGradebookColumnAndResourceOnDateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntriesByGrader {
    static readonly methodName = "GetGradeEntriesByGrader";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesByGraderRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
  export class GetGradeEntries {
    static readonly methodName = "GetGradeEntries";
    static readonly service = GradeEntryLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
}
export class GradeEntryQuerySession {
  static serviceName = "dlkit.proto.grading.GradeEntryQuerySession";
}
export namespace GradeEntryQuerySession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradeEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradeEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanSearchGradeEntries {
    static readonly methodName = "CanSearchGradeEntries";
    static readonly service = GradeEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanSearchGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanSearchGradeEntriesReply;
  }
  export class UseFederatedGradebookView {
    static readonly methodName = "UseFederatedGradebookView";
    static readonly service = GradeEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseFederatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseFederatedGradebookViewReply;
  }
  export class UseIsolatedGradebookView {
    static readonly methodName = "UseIsolatedGradebookView";
    static readonly service = GradeEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseIsolatedGradebookViewReply;
  }
  export class GetGradeEntryQuery {
    static readonly methodName = "GetGradeEntryQuery";
    static readonly service = GradeEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntryQueryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeEntryQueryReply;
  }
  export class GetGradeEntriesByQuery {
    static readonly methodName = "GetGradeEntriesByQuery";
    static readonly service = GradeEntryQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntriesByQueryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradeEntry;
  }
}
export class GradeEntryAdminSession {
  static serviceName = "dlkit.proto.grading.GradeEntryAdminSession";
}
export namespace GradeEntryAdminSession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanCreateGradeEntries {
    static readonly methodName = "CanCreateGradeEntries";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradeEntriesReply;
  }
  export class CanCreateGradeEntryWithRecordTypes {
    static readonly methodName = "CanCreateGradeEntryWithRecordTypes";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradeEntryWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradeEntryWithRecordTypesReply;
  }
  export class GetGradeEntryFormForCreate {
    static readonly methodName = "GetGradeEntryFormForCreate";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntryFormForCreateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeEntryFormForCreateReply;
  }
  export class CreateGradeEntry {
    static readonly methodName = "CreateGradeEntry";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CreateGradeEntryRequest;
    static readonly responseType = dlkit_proto_grading_pb.CreateGradeEntryReply;
  }
  export class CanOverridecalculatedGradeEntries {
    static readonly methodName = "CanOverridecalculatedGradeEntries";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanOverridecalculatedGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanOverridecalculatedGradeEntriesReply;
  }
  export class GetGradeEntryFormForOverride {
    static readonly methodName = "GetGradeEntryFormForOverride";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntryFormForOverrideRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeEntryFormForOverrideReply;
  }
  export class OverrideCalculatedGradeEntry {
    static readonly methodName = "OverrideCalculatedGradeEntry";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.OverrideCalculatedGradeEntryRequest;
    static readonly responseType = dlkit_proto_grading_pb.OverrideCalculatedGradeEntryReply;
  }
  export class CanUpdateGradeEntries {
    static readonly methodName = "CanUpdateGradeEntries";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanUpdateGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanUpdateGradeEntriesReply;
  }
  export class GetGradeEntryFormForUpdate {
    static readonly methodName = "GetGradeEntryFormForUpdate";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradeEntryFormForUpdateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradeEntryFormForUpdateReply;
  }
  export class UpdateGradeEntry {
    static readonly methodName = "UpdateGradeEntry";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UpdateGradeEntryRequest;
    static readonly responseType = dlkit_proto_grading_pb.UpdateGradeEntryReply;
  }
  export class CanDeleteGradeEntries {
    static readonly methodName = "CanDeleteGradeEntries";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanDeleteGradeEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanDeleteGradeEntriesReply;
  }
  export class DeleteGradeEntry {
    static readonly methodName = "DeleteGradeEntry";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.DeleteGradeEntryRequest;
    static readonly responseType = dlkit_proto_grading_pb.DeleteGradeEntryReply;
  }
  export class CanManageGradeEntryAliases {
    static readonly methodName = "CanManageGradeEntryAliases";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanManageGradeEntryAliasesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanManageGradeEntryAliasesReply;
  }
  export class AliasGradeEntry {
    static readonly methodName = "AliasGradeEntry";
    static readonly service = GradeEntryAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AliasGradeEntryRequest;
    static readonly responseType = dlkit_proto_grading_pb.AliasGradeEntryReply;
  }
}
export class GradebookColumnLookupSession {
  static serviceName = "dlkit.proto.grading.GradebookColumnLookupSession";
}
export namespace GradebookColumnLookupSession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanLookupGradebookColumns {
    static readonly methodName = "CanLookupGradebookColumns";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanLookupGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanLookupGradebookColumnsReply;
  }
  export class UseComparativeGradebookColumnView {
    static readonly methodName = "UseComparativeGradebookColumnView";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseComparativeGradebookColumnViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseComparativeGradebookColumnViewReply;
  }
  export class UsePlenaryGradebookColumnView {
    static readonly methodName = "UsePlenaryGradebookColumnView";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UsePlenaryGradebookColumnViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UsePlenaryGradebookColumnViewReply;
  }
  export class UseFederatedGradebookView {
    static readonly methodName = "UseFederatedGradebookView";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseFederatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseFederatedGradebookViewReply;
  }
  export class UseIsolatedGradebookView {
    static readonly methodName = "UseIsolatedGradebookView";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseIsolatedGradebookViewReply;
  }
  export class GetGradebookColumn {
    static readonly methodName = "GetGradebookColumn";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookColumnReply;
  }
  export class GetGradebookColumnsByIds {
    static readonly methodName = "GetGradebookColumnsByIds";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsByIdsRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
  export class GetGradebookColumnsByGenusType {
    static readonly methodName = "GetGradebookColumnsByGenusType";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
  export class GetGradebookColumnsByParentGenusType {
    static readonly methodName = "GetGradebookColumnsByParentGenusType";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
  export class GetGradebookColumnsByRecordType {
    static readonly methodName = "GetGradebookColumnsByRecordType";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
  export class GetGradebookColumns {
    static readonly methodName = "GetGradebookColumns";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
  export class SupportsSummary {
    static readonly methodName = "SupportsSummary";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.SupportsSummaryRequest;
    static readonly responseType = dlkit_proto_grading_pb.SupportsSummaryReply;
  }
  export class GetGradebookColumnSummary {
    static readonly methodName = "GetGradebookColumnSummary";
    static readonly service = GradebookColumnLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnSummaryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookColumnSummaryReply;
  }
}
export class GradebookColumnQuerySession {
  static serviceName = "dlkit.proto.grading.GradebookColumnQuerySession";
}
export namespace GradebookColumnQuerySession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradebookColumnQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradebookColumnQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanSearchGradebookColumns {
    static readonly methodName = "CanSearchGradebookColumns";
    static readonly service = GradebookColumnQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanSearchGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanSearchGradebookColumnsReply;
  }
  export class UseFederatedGradebookView {
    static readonly methodName = "UseFederatedGradebookView";
    static readonly service = GradebookColumnQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseFederatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseFederatedGradebookViewReply;
  }
  export class UseIsolatedGradebookView {
    static readonly methodName = "UseIsolatedGradebookView";
    static readonly service = GradebookColumnQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseIsolatedGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseIsolatedGradebookViewReply;
  }
  export class GetGradebookColumnQuery {
    static readonly methodName = "GetGradebookColumnQuery";
    static readonly service = GradebookColumnQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnQueryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookColumnQueryReply;
  }
  export class GetGradebookColumnsByQuery {
    static readonly methodName = "GetGradebookColumnsByQuery";
    static readonly service = GradebookColumnQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsByQueryRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
}
export class GradebookColumnAdminSession {
  static serviceName = "dlkit.proto.grading.GradebookColumnAdminSession";
}
export namespace GradebookColumnAdminSession {
  export class GetGradebookId {
    static readonly methodName = "GetGradebookId";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookIdReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class CanCreateGradebookColumns {
    static readonly methodName = "CanCreateGradebookColumns";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradebookColumnsReply;
  }
  export class CanCreateGradebookColumnWithRecordTypes {
    static readonly methodName = "CanCreateGradebookColumnWithRecordTypes";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradebookColumnWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradebookColumnWithRecordTypesReply;
  }
  export class GetGradebookColumnFormForCreate {
    static readonly methodName = "GetGradebookColumnFormForCreate";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnFormForCreateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookColumnFormForCreateReply;
  }
  export class CreateGradebookColumn {
    static readonly methodName = "CreateGradebookColumn";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CreateGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.CreateGradebookColumnReply;
  }
  export class CanUpdateGradebookColumns {
    static readonly methodName = "CanUpdateGradebookColumns";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanUpdateGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanUpdateGradebookColumnsReply;
  }
  export class GetGradebookColumnFormForUpdate {
    static readonly methodName = "GetGradebookColumnFormForUpdate";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnFormForUpdateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookColumnFormForUpdateReply;
  }
  export class UpdateGradebookColumn {
    static readonly methodName = "UpdateGradebookColumn";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UpdateGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.UpdateGradebookColumnReply;
  }
  export class SequenceGradebookColumns {
    static readonly methodName = "SequenceGradebookColumns";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.SequenceGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.SequenceGradebookColumnsReply;
  }
  export class MoveGradebookColumn {
    static readonly methodName = "MoveGradebookColumn";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.MoveGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.MoveGradebookColumnReply;
  }
  export class CopyGradebookColumnEntries {
    static readonly methodName = "CopyGradebookColumnEntries";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CopyGradebookColumnEntriesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CopyGradebookColumnEntriesReply;
  }
  export class CanDeleteGradebookColumns {
    static readonly methodName = "CanDeleteGradebookColumns";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanDeleteGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanDeleteGradebookColumnsReply;
  }
  export class DeleteGradebookColumn {
    static readonly methodName = "DeleteGradebookColumn";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.DeleteGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.DeleteGradebookColumnReply;
  }
  export class CanManageGradebookColumnAliases {
    static readonly methodName = "CanManageGradebookColumnAliases";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanManageGradebookColumnAliasesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanManageGradebookColumnAliasesReply;
  }
  export class AliasGradebookColumn {
    static readonly methodName = "AliasGradebookColumn";
    static readonly service = GradebookColumnAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AliasGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.AliasGradebookColumnReply;
  }
}
export class GradebookColumnGradebookSession {
  static serviceName = "dlkit.proto.grading.GradebookColumnGradebookSession";
}
export namespace GradebookColumnGradebookSession {
  export class UseComparativeGradebookView {
    static readonly methodName = "UseComparativeGradebookView";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseComparativeGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseComparativeGradebookViewReply;
  }
  export class UsePlenaryGradebookView {
    static readonly methodName = "UsePlenaryGradebookView";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UsePlenaryGradebookViewReply;
  }
  export class CanLookupGradebookColumnGradebookMappings {
    static readonly methodName = "CanLookupGradebookColumnGradebookMappings";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanLookupGradebookColumnGradebookMappingsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanLookupGradebookColumnGradebookMappingsReply;
  }
  export class GetGradebookColumnIdsByGradebook {
    static readonly methodName = "GetGradebookColumnIdsByGradebook";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnIdsByGradebookRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetGradebookColumnsByGradebook {
    static readonly methodName = "GetGradebookColumnsByGradebook";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsByGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
  export class GetGradebookColumnIdsByGradebooks {
    static readonly methodName = "GetGradebookColumnIdsByGradebooks";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnIdsByGradebooksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetGradebookColumnsByGradebooks {
    static readonly methodName = "GetGradebookColumnsByGradebooks";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookColumnsByGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.GradebookColumn;
  }
  export class GetGradebookIdsByGradebookColumn {
    static readonly methodName = "GetGradebookIdsByGradebookColumn";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookIdsByGradebookColumnRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetGradebooksByGradebookColumn {
    static readonly methodName = "GetGradebooksByGradebookColumn";
    static readonly service = GradebookColumnGradebookSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksByGradebookColumnRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
}
export class GradebookColumnGradebookAssignmentSession {
  static serviceName = "dlkit.proto.grading.GradebookColumnGradebookAssignmentSession";
}
export namespace GradebookColumnGradebookAssignmentSession {
  export class CanAssignGradebookColumns {
    static readonly methodName = "CanAssignGradebookColumns";
    static readonly service = GradebookColumnGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanAssignGradebookColumnsRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanAssignGradebookColumnsReply;
  }
  export class CanAssignGradebookColumnsToGradebook {
    static readonly methodName = "CanAssignGradebookColumnsToGradebook";
    static readonly service = GradebookColumnGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanAssignGradebookColumnsToGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanAssignGradebookColumnsToGradebookReply;
  }
  export class GetAssignableGradebookIds {
    static readonly methodName = "GetAssignableGradebookIds";
    static readonly service = GradebookColumnGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetAssignableGradebookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableGradebookIdsForGradebookColumn {
    static readonly methodName = "GetAssignableGradebookIdsForGradebookColumn";
    static readonly service = GradebookColumnGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetAssignableGradebookIdsForGradebookColumnRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignGradebookColumnToGradebook {
    static readonly methodName = "AssignGradebookColumnToGradebook";
    static readonly service = GradebookColumnGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AssignGradebookColumnToGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.AssignGradebookColumnToGradebookReply;
  }
  export class UnassignGradebookColumnFromGradebook {
    static readonly methodName = "UnassignGradebookColumnFromGradebook";
    static readonly service = GradebookColumnGradebookAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UnassignGradebookColumnFromGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.UnassignGradebookColumnFromGradebookReply;
  }
}
export class GradebookLookupSession {
  static serviceName = "dlkit.proto.grading.GradebookLookupSession";
}
export namespace GradebookLookupSession {
  export class CanLookupGradebooks {
    static readonly methodName = "CanLookupGradebooks";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanLookupGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanLookupGradebooksReply;
  }
  export class UseComparativeGradebookView {
    static readonly methodName = "UseComparativeGradebookView";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseComparativeGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseComparativeGradebookViewReply;
  }
  export class UsePlenaryGradebookView {
    static readonly methodName = "UsePlenaryGradebookView";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UsePlenaryGradebookViewReply;
  }
  export class GetGradebook {
    static readonly methodName = "GetGradebook";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookReply;
  }
  export class GetGradebooksByIds {
    static readonly methodName = "GetGradebooksByIds";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksByIdsRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class GetGradebooksByGenusType {
    static readonly methodName = "GetGradebooksByGenusType";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksByGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class GetGradebooksByParentGenusType {
    static readonly methodName = "GetGradebooksByParentGenusType";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class GetGradebooksByRecordType {
    static readonly methodName = "GetGradebooksByRecordType";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksByRecordTypeRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class GetGradebooksByProvider {
    static readonly methodName = "GetGradebooksByProvider";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksByProviderRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class GetGradebooks {
    static readonly methodName = "GetGradebooks";
    static readonly service = GradebookLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
}
export class GradebookAdminSession {
  static serviceName = "dlkit.proto.grading.GradebookAdminSession";
}
export namespace GradebookAdminSession {
  export class CanCreateGradebooks {
    static readonly methodName = "CanCreateGradebooks";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradebooksReply;
  }
  export class CanCreateGradebookWithRecordTypes {
    static readonly methodName = "CanCreateGradebookWithRecordTypes";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanCreateGradebookWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanCreateGradebookWithRecordTypesReply;
  }
  export class GetGradebookFormForCreate {
    static readonly methodName = "GetGradebookFormForCreate";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookFormForCreateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookFormForCreateReply;
  }
  export class CreateGradebook {
    static readonly methodName = "CreateGradebook";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CreateGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.CreateGradebookReply;
  }
  export class CanUpdateGradebooks {
    static readonly methodName = "CanUpdateGradebooks";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanUpdateGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanUpdateGradebooksReply;
  }
  export class GetGradebookFormForUpdate {
    static readonly methodName = "GetGradebookFormForUpdate";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookFormForUpdateRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookFormForUpdateReply;
  }
  export class UpdateGradebook {
    static readonly methodName = "UpdateGradebook";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UpdateGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.UpdateGradebookReply;
  }
  export class CanDeleteGradebooks {
    static readonly methodName = "CanDeleteGradebooks";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanDeleteGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanDeleteGradebooksReply;
  }
  export class DeleteGradebook {
    static readonly methodName = "DeleteGradebook";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.DeleteGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.DeleteGradebookReply;
  }
  export class CanManageGradebookAliases {
    static readonly methodName = "CanManageGradebookAliases";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanManageGradebookAliasesRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanManageGradebookAliasesReply;
  }
  export class AliasGradebook {
    static readonly methodName = "AliasGradebook";
    static readonly service = GradebookAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AliasGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.AliasGradebookReply;
  }
}
export class GradebookHierarchySession {
  static serviceName = "dlkit.proto.grading.GradebookHierarchySession";
}
export namespace GradebookHierarchySession {
  export class GetGradebookHierarchyId {
    static readonly methodName = "GetGradebookHierarchyId";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookHierarchyIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookHierarchyIdReply;
  }
  export class GetGradebookHierarchy {
    static readonly methodName = "GetGradebookHierarchy";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookHierarchyRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookHierarchyReply;
  }
  export class CanAccessGradebookHierarchy {
    static readonly methodName = "CanAccessGradebookHierarchy";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanAccessGradebookHierarchyRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanAccessGradebookHierarchyReply;
  }
  export class UseComparativeGradebookView {
    static readonly methodName = "UseComparativeGradebookView";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UseComparativeGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UseComparativeGradebookViewReply;
  }
  export class UsePlenaryGradebookView {
    static readonly methodName = "UsePlenaryGradebookView";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.UsePlenaryGradebookViewRequest;
    static readonly responseType = dlkit_proto_grading_pb.UsePlenaryGradebookViewReply;
  }
  export class GetRootGradebookIds {
    static readonly methodName = "GetRootGradebookIds";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetRootGradebookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetRootGradebooks {
    static readonly methodName = "GetRootGradebooks";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetRootGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class HasParentGradebooks {
    static readonly methodName = "HasParentGradebooks";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.HasParentGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.HasParentGradebooksReply;
  }
  export class IsParentOfGradebook {
    static readonly methodName = "IsParentOfGradebook";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.IsParentOfGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.IsParentOfGradebookReply;
  }
  export class GetParentGradebookIds {
    static readonly methodName = "GetParentGradebookIds";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetParentGradebookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetParentGradebooks {
    static readonly methodName = "GetParentGradebooks";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetParentGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class IsAncestorOfGradebook {
    static readonly methodName = "IsAncestorOfGradebook";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.IsAncestorOfGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.IsAncestorOfGradebookReply;
  }
  export class HasChildGradebooks {
    static readonly methodName = "HasChildGradebooks";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.HasChildGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.HasChildGradebooksReply;
  }
  export class IsChildOfGradebook {
    static readonly methodName = "IsChildOfGradebook";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.IsChildOfGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.IsChildOfGradebookReply;
  }
  export class GetChildGradebookIds {
    static readonly methodName = "GetChildGradebookIds";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetChildGradebookIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetChildGradebooks {
    static readonly methodName = "GetChildGradebooks";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_grading_pb.GetChildGradebooksRequest;
    static readonly responseType = dlkit_proto_grading_pb.Gradebook;
  }
  export class IsDescendantOfGradebook {
    static readonly methodName = "IsDescendantOfGradebook";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.IsDescendantOfGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.IsDescendantOfGradebookReply;
  }
  export class GetGradebookNodeIds {
    static readonly methodName = "GetGradebookNodeIds";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookNodeIdsRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookNodeIdsReply;
  }
  export class GetGradebookNodes {
    static readonly methodName = "GetGradebookNodes";
    static readonly service = GradebookHierarchySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookNodesRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookNodesReply;
  }
}
export class GradebookHierarchyDesignSession {
  static serviceName = "dlkit.proto.grading.GradebookHierarchyDesignSession";
}
export namespace GradebookHierarchyDesignSession {
  export class GetGradebookHierarchyId {
    static readonly methodName = "GetGradebookHierarchyId";
    static readonly service = GradebookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookHierarchyIdRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookHierarchyIdReply;
  }
  export class GetGradebookHierarchy {
    static readonly methodName = "GetGradebookHierarchy";
    static readonly service = GradebookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.GetGradebookHierarchyRequest;
    static readonly responseType = dlkit_proto_grading_pb.GetGradebookHierarchyReply;
  }
  export class CanModifyGradebookHierarchy {
    static readonly methodName = "CanModifyGradebookHierarchy";
    static readonly service = GradebookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.CanModifyGradebookHierarchyRequest;
    static readonly responseType = dlkit_proto_grading_pb.CanModifyGradebookHierarchyReply;
  }
  export class AddRootGradebook {
    static readonly methodName = "AddRootGradebook";
    static readonly service = GradebookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AddRootGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.AddRootGradebookReply;
  }
  export class RemoveRootGradebook {
    static readonly methodName = "RemoveRootGradebook";
    static readonly service = GradebookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.RemoveRootGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.RemoveRootGradebookReply;
  }
  export class AddChildGradebook {
    static readonly methodName = "AddChildGradebook";
    static readonly service = GradebookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.AddChildGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.AddChildGradebookReply;
  }
  export class RemoveChildGradebook {
    static readonly methodName = "RemoveChildGradebook";
    static readonly service = GradebookHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_grading_pb.RemoveChildGradebookRequest;
    static readonly responseType = dlkit_proto_grading_pb.RemoveChildGradebookReply;
  }
}
