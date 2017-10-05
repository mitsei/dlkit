// package: dlkit.proto.assessment_authoring
// file: dlkit/proto/assessment_authoring.proto

import * as dlkit_proto_assessment_authoring_pb from "../../dlkit/proto/assessment_authoring_pb";
import * as dlkit_primordium_calendaring_primitives_pb from "../../dlkit/primordium/calendaring/primitives_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_assessment_pb from "../../dlkit/proto/assessment_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
export class AssessmentPartLookupSession {
  static serviceName = "dlkit.proto.assessment_authoring.AssessmentPartLookupSession";
}
export namespace AssessmentPartLookupSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankReply;
  }
  export class CanLookupAssessmentParts {
    static readonly methodName = "CanLookupAssessmentParts";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartsReply;
  }
  export class UseComparativeAssessmentPartView {
    static readonly methodName = "UseComparativeAssessmentPartView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartViewReply;
  }
  export class UsePlenaryAssessmentPartView {
    static readonly methodName = "UsePlenaryAssessmentPartView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartViewReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply;
  }
  export class UseActiveAssessmentPartView {
    static readonly methodName = "UseActiveAssessmentPartView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseActiveAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseActiveAssessmentPartViewReply;
  }
  export class UseAnyStatusAssessmentPartView {
    static readonly methodName = "UseAnyStatusAssessmentPartView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseAnyStatusAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseAnyStatusAssessmentPartViewReply;
  }
  export class UseSequesteredAssessmentPartView {
    static readonly methodName = "UseSequesteredAssessmentPartView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewReply;
  }
  export class UseUnsequesteredAssessmentPartView {
    static readonly methodName = "UseUnsequesteredAssessmentPartView";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewReply;
  }
  export class GetAssessmentPart {
    static readonly methodName = "GetAssessmentPart";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartReply;
  }
  export class GetAssessmentPartsByIds {
    static readonly methodName = "GetAssessmentPartsByIds";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByIdsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
  export class GetAssessmentPartsByGenusType {
    static readonly methodName = "GetAssessmentPartsByGenusType";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
  export class GetAssessmentPartsByParentGenusType {
    static readonly methodName = "GetAssessmentPartsByParentGenusType";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
  export class GetAssessmentPartsByRecordType {
    static readonly methodName = "GetAssessmentPartsByRecordType";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
  export class GetAssessmentPartsForAssessment {
    static readonly methodName = "GetAssessmentPartsForAssessment";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsForAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
  export class GetAssessmentParts {
    static readonly methodName = "GetAssessmentParts";
    static readonly service = AssessmentPartLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
}
export class AssessmentPartQuerySession {
  static serviceName = "dlkit.proto.assessment_authoring.AssessmentPartQuerySession";
}
export namespace AssessmentPartQuerySession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankReply;
  }
  export class CanSearchAssessmentParts {
    static readonly methodName = "CanSearchAssessmentParts";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanSearchAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanSearchAssessmentPartsReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply;
  }
  export class UseSequesteredAssessmentPartView {
    static readonly methodName = "UseSequesteredAssessmentPartView";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseSequesteredAssessmentPartViewReply;
  }
  export class UseUnsequesteredAssessmentPartView {
    static readonly methodName = "UseUnsequesteredAssessmentPartView";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseUnsequesteredAssessmentPartViewReply;
  }
  export class GetAssessmentPartQuery {
    static readonly methodName = "GetAssessmentPartQuery";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartQueryRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartQueryReply;
  }
  export class GetAssessmentPartsByQuery {
    static readonly methodName = "GetAssessmentPartsByQuery";
    static readonly service = AssessmentPartQuerySession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByQueryRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
}
export class AssessmentPartAdminSession {
  static serviceName = "dlkit.proto.assessment_authoring.AssessmentPartAdminSession";
}
export namespace AssessmentPartAdminSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankReply;
  }
  export class CanCreateAssessmentParts {
    static readonly methodName = "CanCreateAssessmentParts";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartsReply;
  }
  export class CanCreateAssessmentPartWithRecordTypes {
    static readonly methodName = "CanCreateAssessmentPartWithRecordTypes";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanCreateAssessmentPartWithRecordTypesReply;
  }
  export class GetAssessmentPartFormForCreateForAssessment {
    static readonly methodName = "GetAssessmentPartFormForCreateForAssessment";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentReply;
  }
  export class CreateAssessmentPartForAssessment {
    static readonly methodName = "CreateAssessmentPartForAssessment";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentReply;
  }
  export class GetAssessmentPartFormForCreateForAssessmentPart {
    static readonly methodName = "GetAssessmentPartFormForCreateForAssessmentPart";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForCreateForAssessmentPartReply;
  }
  export class CreateAssessmentPartForAssessmentPart {
    static readonly methodName = "CreateAssessmentPartForAssessmentPart";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CreateAssessmentPartForAssessmentPartReply;
  }
  export class CanUpdateAssessmentParts {
    static readonly methodName = "CanUpdateAssessmentParts";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanUpdateAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanUpdateAssessmentPartsReply;
  }
  export class GetAssessmentPartFormForUpdate {
    static readonly methodName = "GetAssessmentPartFormForUpdate";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartFormForUpdateReply;
  }
  export class UpdateAssessmentPart {
    static readonly methodName = "UpdateAssessmentPart";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UpdateAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UpdateAssessmentPartReply;
  }
  export class CanDeleteAssessmentParts {
    static readonly methodName = "CanDeleteAssessmentParts";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanDeleteAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanDeleteAssessmentPartsReply;
  }
  export class DeleteAssessmentPart {
    static readonly methodName = "DeleteAssessmentPart";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.DeleteAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.DeleteAssessmentPartReply;
  }
  export class CanManageAssessmentPartAliases {
    static readonly methodName = "CanManageAssessmentPartAliases";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanManageAssessmentPartAliasesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanManageAssessmentPartAliasesReply;
  }
  export class AliasAssessmentPart {
    static readonly methodName = "AliasAssessmentPart";
    static readonly service = AssessmentPartAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.AliasAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AliasAssessmentPartReply;
  }
}
export class AssessmentPartBankSession {
  static serviceName = "dlkit.proto.assessment_authoring.AssessmentPartBankSession";
}
export namespace AssessmentPartBankSession {
  export class CanLookupAssessmentPartBankMappings {
    static readonly methodName = "CanLookupAssessmentPartBankMappings";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartBankMappingsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanLookupAssessmentPartBankMappingsReply;
  }
  export class UseComparativeAssessmentPartBankView {
    static readonly methodName = "UseComparativeAssessmentPartBankView";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseComparativeAssessmentPartBankViewReply;
  }
  export class UsePlenaryAssessmentPartBankView {
    static readonly methodName = "UsePlenaryAssessmentPartBankView";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartBankViewReply;
  }
  export class GetAssessmentPartIdsByBank {
    static readonly methodName = "GetAssessmentPartIdsByBank";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartIdsByBankRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentPartsByBank {
    static readonly methodName = "GetAssessmentPartsByBank";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
  export class GetAssessmentPartIdsByBanks {
    static readonly methodName = "GetAssessmentPartIdsByBanks";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartIdsByBanksRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssessmentPartsByBanks {
    static readonly methodName = "GetAssessmentPartsByBanks";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByBanksRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
  export class GetBankIdsByAssessmentPart {
    static readonly methodName = "GetBankIdsByAssessmentPart";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdsByAssessmentPartRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetBanksByAssessmentPart {
    static readonly methodName = "GetBanksByAssessmentPart";
    static readonly service = AssessmentPartBankSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBanksByAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Bank;
  }
}
export class AssessmentPartBankAssignmentSession {
  static serviceName = "dlkit.proto.assessment_authoring.AssessmentPartBankAssignmentSession";
}
export namespace AssessmentPartBankAssignmentSession {
  export class CanAssignAssessmentParts {
    static readonly methodName = "CanAssignAssessmentParts";
    static readonly service = AssessmentPartBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsReply;
  }
  export class CanAssignAssessmentPartsToBank {
    static readonly methodName = "CanAssignAssessmentPartsToBank";
    static readonly service = AssessmentPartBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsToBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanAssignAssessmentPartsToBankReply;
  }
  export class GetAssignableBankIds {
    static readonly methodName = "GetAssignableBankIds";
    static readonly service = AssessmentPartBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssignableBankIdsRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class GetAssignableBankIdsForAssessmentPart {
    static readonly methodName = "GetAssignableBankIdsForAssessmentPart";
    static readonly service = AssessmentPartBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssignableBankIdsForAssessmentPartRequest;
    static readonly responseType = dlkit_primordium_id_primitives_pb.Id;
  }
  export class AssignAssessmentPartToBank {
    static readonly methodName = "AssignAssessmentPartToBank";
    static readonly service = AssessmentPartBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.AssignAssessmentPartToBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssignAssessmentPartToBankReply;
  }
  export class UnassignAssessmentPartFromBank {
    static readonly methodName = "UnassignAssessmentPartFromBank";
    static readonly service = AssessmentPartBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UnassignAssessmentPartFromBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UnassignAssessmentPartFromBankReply;
  }
  export class ReassignAssessmentPartToBank {
    static readonly methodName = "ReassignAssessmentPartToBank";
    static readonly service = AssessmentPartBankAssignmentSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.ReassignAssessmentPartToBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.ReassignAssessmentPartToBankReply;
  }
}
export class AssessmentPartItemSession {
  static serviceName = "dlkit.proto.assessment_authoring.AssessmentPartItemSession";
}
export namespace AssessmentPartItemSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankReply;
  }
  export class CanAccessAssessmentPartItems {
    static readonly methodName = "CanAccessAssessmentPartItems";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanAccessAssessmentPartItemsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanAccessAssessmentPartItemsReply;
  }
  export class UseComparativeAsseessmentPartItemView {
    static readonly methodName = "UseComparativeAsseessmentPartItemView";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseComparativeAsseessmentPartItemViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseComparativeAsseessmentPartItemViewReply;
  }
  export class UsePlenaryAssessmentPartItemView {
    static readonly methodName = "UsePlenaryAssessmentPartItemView";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartItemViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UsePlenaryAssessmentPartItemViewReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply;
  }
  export class GetAssessmentPartItems {
    static readonly methodName = "GetAssessmentPartItems";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartItemsRequest;
    static readonly responseType = dlkit_proto_assessment_pb.Item;
  }
  export class GetAssessmentPartsByItem {
    static readonly methodName = "GetAssessmentPartsByItem";
    static readonly service = AssessmentPartItemSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetAssessmentPartsByItemRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AssessmentPart;
  }
}
export class AssessmentPartItemDesignSession {
  static serviceName = "dlkit.proto.assessment_authoring.AssessmentPartItemDesignSession";
}
export namespace AssessmentPartItemDesignSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankReply;
  }
  export class CanDesignAssessmentParts {
    static readonly methodName = "CanDesignAssessmentParts";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanDesignAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanDesignAssessmentPartsReply;
  }
  export class AddItem {
    static readonly methodName = "AddItem";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.AddItemRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AddItemReply;
  }
  export class MoveItemAhead {
    static readonly methodName = "MoveItemAhead";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.MoveItemAheadRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.MoveItemAheadReply;
  }
  export class MoveItemBehind {
    static readonly methodName = "MoveItemBehind";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.MoveItemBehindRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.MoveItemBehindReply;
  }
  export class OrderItems {
    static readonly methodName = "OrderItems";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.OrderItemsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.OrderItemsReply;
  }
  export class RemoveItem {
    static readonly methodName = "RemoveItem";
    static readonly service = AssessmentPartItemDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.RemoveItemRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.RemoveItemReply;
  }
}
export class SequenceRuleLookupSession {
  static serviceName = "dlkit.proto.assessment_authoring.SequenceRuleLookupSession";
}
export namespace SequenceRuleLookupSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankReply;
  }
  export class CanLookupSequenceRules {
    static readonly methodName = "CanLookupSequenceRules";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanLookupSequenceRulesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanLookupSequenceRulesReply;
  }
  export class UseComparativeSequenceRuleView {
    static readonly methodName = "UseComparativeSequenceRuleView";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseComparativeSequenceRuleViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseComparativeSequenceRuleViewReply;
  }
  export class UsePlenarySequenceRuleView {
    static readonly methodName = "UsePlenarySequenceRuleView";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UsePlenarySequenceRuleViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UsePlenarySequenceRuleViewReply;
  }
  export class UseFederatedBankView {
    static readonly methodName = "UseFederatedBankView";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseFederatedBankViewReply;
  }
  export class UseIsolatedBankView {
    static readonly methodName = "UseIsolatedBankView";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseIsolatedBankViewReply;
  }
  export class UseActiveSequenceRuleView {
    static readonly methodName = "UseActiveSequenceRuleView";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseActiveSequenceRuleViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseActiveSequenceRuleViewReply;
  }
  export class UseAnyStatusSequenceRuleView {
    static readonly methodName = "UseAnyStatusSequenceRuleView";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UseAnyStatusSequenceRuleViewRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UseAnyStatusSequenceRuleViewReply;
  }
  export class GetSequenceRule {
    static readonly methodName = "GetSequenceRule";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRuleRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetSequenceRuleReply;
  }
  export class GetSequenceRulesByIds {
    static readonly methodName = "GetSequenceRulesByIds";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesByIdsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRulesByGenusType {
    static readonly methodName = "GetSequenceRulesByGenusType";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesByGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRulesByParentGenusType {
    static readonly methodName = "GetSequenceRulesByParentGenusType";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRulesByRecordType {
    static readonly methodName = "GetSequenceRulesByRecordType";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesByRecordTypeRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRulesForAssessmentPart {
    static readonly methodName = "GetSequenceRulesForAssessmentPart";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesForAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRulesForNextAssessmentPart {
    static readonly methodName = "GetSequenceRulesForNextAssessmentPart";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesForNextAssessmentPartRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRulesForAssessmentParts {
    static readonly methodName = "GetSequenceRulesForAssessmentParts";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesForAssessmentPartsRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRulesForAssessment {
    static readonly methodName = "GetSequenceRulesForAssessment";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesForAssessmentRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
  export class GetSequenceRules {
    static readonly methodName = "GetSequenceRules";
    static readonly service = SequenceRuleLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRulesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.SequenceRule;
  }
}
export class SequenceRuleAdminSession {
  static serviceName = "dlkit.proto.assessment_authoring.SequenceRuleAdminSession";
}
export namespace SequenceRuleAdminSession {
  export class GetBankId {
    static readonly methodName = "GetBankId";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankIdRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankIdReply;
  }
  export class GetBank {
    static readonly methodName = "GetBank";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetBankRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetBankReply;
  }
  export class CanCreateSequenceRule {
    static readonly methodName = "CanCreateSequenceRule";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleReply;
  }
  export class CanCreateSequenceRuleWithRecordTypes {
    static readonly methodName = "CanCreateSequenceRuleWithRecordTypes";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleWithRecordTypesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanCreateSequenceRuleWithRecordTypesReply;
  }
  export class GetSequenceRuleFormForCreate {
    static readonly methodName = "GetSequenceRuleFormForCreate";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForCreateRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForCreateReply;
  }
  export class CreateSequenceRule {
    static readonly methodName = "CreateSequenceRule";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CreateSequenceRuleRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CreateSequenceRuleReply;
  }
  export class CanUpdateSequenceRules {
    static readonly methodName = "CanUpdateSequenceRules";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanUpdateSequenceRulesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanUpdateSequenceRulesReply;
  }
  export class GetSequenceRuleFormForUpdate {
    static readonly methodName = "GetSequenceRuleFormForUpdate";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForUpdateRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.GetSequenceRuleFormForUpdateReply;
  }
  export class UpdateSequenceRule {
    static readonly methodName = "UpdateSequenceRule";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.UpdateSequenceRuleRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.UpdateSequenceRuleReply;
  }
  export class CanDeleteSequenceRules {
    static readonly methodName = "CanDeleteSequenceRules";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanDeleteSequenceRulesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanDeleteSequenceRulesReply;
  }
  export class DeleteSequenceRule {
    static readonly methodName = "DeleteSequenceRule";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.DeleteSequenceRuleRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.DeleteSequenceRuleReply;
  }
  export class CanManageSequenceRuleAliases {
    static readonly methodName = "CanManageSequenceRuleAliases";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanManageSequenceRuleAliasesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanManageSequenceRuleAliasesReply;
  }
  export class AliasSequenceRule {
    static readonly methodName = "AliasSequenceRule";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.AliasSequenceRuleRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.AliasSequenceRuleReply;
  }
  export class CanSequenceSequenceRules {
    static readonly methodName = "CanSequenceSequenceRules";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.CanSequenceSequenceRulesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.CanSequenceSequenceRulesReply;
  }
  export class MoveSequenceRuleAhead {
    static readonly methodName = "MoveSequenceRuleAhead";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.MoveSequenceRuleAheadRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.MoveSequenceRuleAheadReply;
  }
  export class MoveSequenceRuleBehind {
    static readonly methodName = "MoveSequenceRuleBehind";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.MoveSequenceRuleBehindRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.MoveSequenceRuleBehindReply;
  }
  export class OrderSequenceRules {
    static readonly methodName = "OrderSequenceRules";
    static readonly service = SequenceRuleAdminSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_assessment_authoring_pb.OrderSequenceRulesRequest;
    static readonly responseType = dlkit_proto_assessment_authoring_pb.OrderSequenceRulesReply;
  }
}
