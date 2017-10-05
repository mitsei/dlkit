// package: dlkit.proto.ontology
// file: dlkit/proto/ontology.proto

import * as dlkit_proto_ontology_pb from "../../dlkit/proto/ontology_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_hierarchy_pb from "../../dlkit/proto/hierarchy_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
export class SubjectHierarchyDesignSession {
  static serviceName = "dlkit.proto.ontology.SubjectHierarchyDesignSession";
}
export namespace SubjectHierarchyDesignSession {
  export class GetSubjectHierarchyId {
    static readonly methodName = "GetSubjectHierarchyId";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.GetSubjectHierarchyIdRequest;
    static readonly responseType = dlkit_proto_ontology_pb.GetSubjectHierarchyIdReply;
  }
  export class GetSubjectHierarchy {
    static readonly methodName = "GetSubjectHierarchy";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.GetSubjectHierarchyRequest;
    static readonly responseType = dlkit_proto_ontology_pb.GetSubjectHierarchyReply;
  }
  export class CanModifySubjectHierarchy {
    static readonly methodName = "CanModifySubjectHierarchy";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.CanModifySubjectHierarchyRequest;
    static readonly responseType = dlkit_proto_ontology_pb.CanModifySubjectHierarchyReply;
  }
  export class AddRootSubject {
    static readonly methodName = "AddRootSubject";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.AddRootSubjectRequest;
    static readonly responseType = dlkit_proto_ontology_pb.AddRootSubjectReply;
  }
  export class RemoveRootSubject {
    static readonly methodName = "RemoveRootSubject";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.RemoveRootSubjectRequest;
    static readonly responseType = dlkit_proto_ontology_pb.RemoveRootSubjectReply;
  }
  export class AddChildSubject {
    static readonly methodName = "AddChildSubject";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.AddChildSubjectRequest;
    static readonly responseType = dlkit_proto_ontology_pb.AddChildSubjectReply;
  }
  export class RemoveChildSubject {
    static readonly methodName = "RemoveChildSubject";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.RemoveChildSubjectRequest;
    static readonly responseType = dlkit_proto_ontology_pb.RemoveChildSubjectReply;
  }
  export class RemoveChildSubjects {
    static readonly methodName = "RemoveChildSubjects";
    static readonly service = SubjectHierarchyDesignSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_ontology_pb.RemoveChildSubjectsRequest;
    static readonly responseType = dlkit_proto_ontology_pb.RemoveChildSubjectsReply;
  }
}
