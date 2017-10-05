// package: dlkit.proto.proxy
// file: dlkit/proto/proxy.proto

import * as dlkit_proto_proxy_pb from "../../dlkit/proto/proxy_pb";
export class ProxySession {
  static serviceName = "dlkit.proto.proxy.ProxySession";
}
export namespace ProxySession {
  export class GetProxyCondition {
    static readonly methodName = "GetProxyCondition";
    static readonly service = ProxySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_proxy_pb.GetProxyConditionRequest;
    static readonly responseType = dlkit_proto_proxy_pb.GetProxyConditionReply;
  }
  export class GetProxy {
    static readonly methodName = "GetProxy";
    static readonly service = ProxySession;
    static readonly requestStream = false;
    static readonly responseStream = false;
    static readonly requestType = dlkit_proto_proxy_pb.GetProxyRequest;
    static readonly responseType = dlkit_proto_proxy_pb.GetProxyReply;
  }
}
