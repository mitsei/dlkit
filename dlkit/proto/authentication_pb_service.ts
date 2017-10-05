// package: dlkit.proto.authentication
// file: dlkit/proto/authentication.proto

import * as dlkit_proto_authentication_pb from "../../dlkit/proto/authentication_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
export class AgentLookupSession {
  static serviceName = "dlkit.proto.authentication.AgentLookupSession";
}
export namespace AgentLookupSession {
  export class GetAgencyId {
    static readonly methodName = "GetAgencyId";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgencyIdRequest;
    static readonly responseType = dlkit_proto_authentication_pb.GetAgencyIdReply;
  }
  export class GetAgency {
    static readonly methodName = "GetAgency";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgencyRequest;
    static readonly responseType = dlkit_proto_authentication_pb.GetAgencyReply;
  }
  export class CanLookupAgents {
    static readonly methodName = "CanLookupAgents";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.CanLookupAgentsRequest;
    static readonly responseType = dlkit_proto_authentication_pb.CanLookupAgentsReply;
  }
  export class UseComparativeAgentView {
    static readonly methodName = "UseComparativeAgentView";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.UseComparativeAgentViewRequest;
    static readonly responseType = dlkit_proto_authentication_pb.UseComparativeAgentViewReply;
  }
  export class UsePlenaryAgentView {
    static readonly methodName = "UsePlenaryAgentView";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.UsePlenaryAgentViewRequest;
    static readonly responseType = dlkit_proto_authentication_pb.UsePlenaryAgentViewReply;
  }
  export class UseFederatedAgencyView {
    static readonly methodName = "UseFederatedAgencyView";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.UseFederatedAgencyViewRequest;
    static readonly responseType = dlkit_proto_authentication_pb.UseFederatedAgencyViewReply;
  }
  export class UseIsolatedAgencyView {
    static readonly methodName = "UseIsolatedAgencyView";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.UseIsolatedAgencyViewRequest;
    static readonly responseType = dlkit_proto_authentication_pb.UseIsolatedAgencyViewReply;
  }
  export class GetAgent {
    static readonly methodName = "GetAgent";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgentRequest;
    static readonly responseType = dlkit_proto_authentication_pb.GetAgentReply;
  }
  export class GetAgentsByIds {
    static readonly methodName = "GetAgentsByIds";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgentsByIdsRequest;
    static readonly responseType = dlkit_proto_authentication_pb.Agent;
  }
  export class GetAgentsByGenusType {
    static readonly methodName = "GetAgentsByGenusType";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgentsByGenusTypeRequest;
    static readonly responseType = dlkit_proto_authentication_pb.Agent;
  }
  export class GetAgentsByParentGenusType {
    static readonly methodName = "GetAgentsByParentGenusType";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgentsByParentGenusTypeRequest;
    static readonly responseType = dlkit_proto_authentication_pb.Agent;
  }
  export class GetAgentsByRecordType {
    static readonly methodName = "GetAgentsByRecordType";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgentsByRecordTypeRequest;
    static readonly responseType = dlkit_proto_authentication_pb.Agent;
  }
  export class GetAgents {
    static readonly methodName = "GetAgents";
    static readonly service = AgentLookupSession;
    static readonly requestStream = false;
    static readonly responseStream = true;
    static readonly requestType = dlkit_proto_authentication_pb.GetAgentsRequest;
    static readonly responseType = dlkit_proto_authentication_pb.Agent;
  }
}
