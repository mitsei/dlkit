// package: dlkit.proto.authentication
// file: dlkit/proto/authentication.proto

var jspb = require("google-protobuf");
var dlkit_proto_authentication_pb = require("../../dlkit/proto/authentication_pb");
var dlkit_primordium_id_primitives_pb = require("../../dlkit/primordium/id/primitives_pb");
var dlkit_primordium_locale_primitives_pb = require("../../dlkit/primordium/locale/primitives_pb");
var dlkit_primordium_type_primitives_pb = require("../../dlkit/primordium/type/primitives_pb");
var dlkit_proto_osid_pb = require("../../dlkit/proto/osid_pb");
var AgentLookupSession = {
  serviceName: "dlkit.proto.authentication.AgentLookupSession"
};
AgentLookupSession.GetAgencyId = {
  methodName: "GetAgencyId",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.GetAgencyIdRequest,
  responseType: dlkit_proto_authentication_pb.GetAgencyIdReply
};
AgentLookupSession.GetAgency = {
  methodName: "GetAgency",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.GetAgencyRequest,
  responseType: dlkit_proto_authentication_pb.GetAgencyReply
};
AgentLookupSession.CanLookupAgents = {
  methodName: "CanLookupAgents",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.CanLookupAgentsRequest,
  responseType: dlkit_proto_authentication_pb.CanLookupAgentsReply
};
AgentLookupSession.UseComparativeAgentView = {
  methodName: "UseComparativeAgentView",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.UseComparativeAgentViewRequest,
  responseType: dlkit_proto_authentication_pb.UseComparativeAgentViewReply
};
AgentLookupSession.UsePlenaryAgentView = {
  methodName: "UsePlenaryAgentView",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.UsePlenaryAgentViewRequest,
  responseType: dlkit_proto_authentication_pb.UsePlenaryAgentViewReply
};
AgentLookupSession.UseFederatedAgencyView = {
  methodName: "UseFederatedAgencyView",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.UseFederatedAgencyViewRequest,
  responseType: dlkit_proto_authentication_pb.UseFederatedAgencyViewReply
};
AgentLookupSession.UseIsolatedAgencyView = {
  methodName: "UseIsolatedAgencyView",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.UseIsolatedAgencyViewRequest,
  responseType: dlkit_proto_authentication_pb.UseIsolatedAgencyViewReply
};
AgentLookupSession.GetAgent = {
  methodName: "GetAgent",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_authentication_pb.GetAgentRequest,
  responseType: dlkit_proto_authentication_pb.GetAgentReply
};
AgentLookupSession.GetAgentsByIds = {
  methodName: "GetAgentsByIds",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authentication_pb.GetAgentsByIdsRequest,
  responseType: dlkit_proto_authentication_pb.Agent
};
AgentLookupSession.GetAgentsByGenusType = {
  methodName: "GetAgentsByGenusType",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authentication_pb.GetAgentsByGenusTypeRequest,
  responseType: dlkit_proto_authentication_pb.Agent
};
AgentLookupSession.GetAgentsByParentGenusType = {
  methodName: "GetAgentsByParentGenusType",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authentication_pb.GetAgentsByParentGenusTypeRequest,
  responseType: dlkit_proto_authentication_pb.Agent
};
AgentLookupSession.GetAgentsByRecordType = {
  methodName: "GetAgentsByRecordType",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authentication_pb.GetAgentsByRecordTypeRequest,
  responseType: dlkit_proto_authentication_pb.Agent
};
AgentLookupSession.GetAgents = {
  methodName: "GetAgents",
  service: AgentLookupSession,
  requestStream: false,
  responseStream: true,
  requestType: dlkit_proto_authentication_pb.GetAgentsRequest,
  responseType: dlkit_proto_authentication_pb.Agent
};
module.exports = {
  AgentLookupSession: AgentLookupSession,
};

