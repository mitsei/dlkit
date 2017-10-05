// package: dlkit.proto.ontology
// file: dlkit/proto/ontology.proto

var jspb = require("google-protobuf");
var dlkit_proto_ontology_pb = require("../../dlkit/proto/ontology_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_hierarchy_pb = require("../../dlkit/proto/hierarchy_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var SubjectHierarchyDesignSession = {
  serviceName: "dlkit.proto.ontology.SubjectHierarchyDesignSession"
};
SubjectHierarchyDesignSession.GetSubjectHierarchyId = {
  methodName: "GetSubjectHierarchyId",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.GetSubjectHierarchyIdRequest,
  responseType: dlkit_proto_ontology_pb.GetSubjectHierarchyIdReply
};
SubjectHierarchyDesignSession.GetSubjectHierarchy = {
  methodName: "GetSubjectHierarchy",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.GetSubjectHierarchyRequest,
  responseType: dlkit_proto_ontology_pb.GetSubjectHierarchyReply
};
SubjectHierarchyDesignSession.CanModifySubjectHierarchy = {
  methodName: "CanModifySubjectHierarchy",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.CanModifySubjectHierarchyRequest,
  responseType: dlkit_proto_ontology_pb.CanModifySubjectHierarchyReply
};
SubjectHierarchyDesignSession.AddRootSubject = {
  methodName: "AddRootSubject",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.AddRootSubjectRequest,
  responseType: dlkit_proto_ontology_pb.AddRootSubjectReply
};
SubjectHierarchyDesignSession.RemoveRootSubject = {
  methodName: "RemoveRootSubject",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.RemoveRootSubjectRequest,
  responseType: dlkit_proto_ontology_pb.RemoveRootSubjectReply
};
SubjectHierarchyDesignSession.AddChildSubject = {
  methodName: "AddChildSubject",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.AddChildSubjectRequest,
  responseType: dlkit_proto_ontology_pb.AddChildSubjectReply
};
SubjectHierarchyDesignSession.RemoveChildSubject = {
  methodName: "RemoveChildSubject",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.RemoveChildSubjectRequest,
  responseType: dlkit_proto_ontology_pb.RemoveChildSubjectReply
};
SubjectHierarchyDesignSession.RemoveChildSubjects = {
  methodName: "RemoveChildSubjects",
  service: SubjectHierarchyDesignSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_ontology_pb.RemoveChildSubjectsRequest,
  responseType: dlkit_proto_ontology_pb.RemoveChildSubjectsReply
};
module.exports = {
  SubjectHierarchyDesignSession: SubjectHierarchyDesignSession,
};

