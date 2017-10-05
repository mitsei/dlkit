// package: dlkit.proto.proxy
// file: dlkit/proto/proxy.proto

var jspb = require("google-protobuf");
var dlkit_proto_proxy_pb = require("../../dlkit/proto/proxy_pb");
var ProxySession = {
  serviceName: "dlkit.proto.proxy.ProxySession"
};
ProxySession.GetProxyCondition = {
  methodName: "GetProxyCondition",
  service: ProxySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_proxy_pb.GetProxyConditionRequest,
  responseType: dlkit_proto_proxy_pb.GetProxyConditionReply
};
ProxySession.GetProxy = {
  methodName: "GetProxy",
  service: ProxySession,
  requestStream: false,
  responseStream: false,
  requestType: dlkit_proto_proxy_pb.GetProxyRequest,
  responseType: dlkit_proto_proxy_pb.GetProxyReply
};
module.exports = {
  ProxySession: ProxySession,
};

