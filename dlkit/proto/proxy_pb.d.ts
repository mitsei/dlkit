// package: dlkit.proto.proxy
// file: dlkit/proto/proxy.proto

import * as jspb from "google-protobuf";

export class Proxy extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Proxy.AsObject;
  static toObject(includeInstance: boolean, msg: Proxy): Proxy.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Proxy, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Proxy;
  static deserializeBinaryFromReader(message: Proxy, reader: jspb.BinaryReader): Proxy;
}

export namespace Proxy {
  export type AsObject = {
  }
}

export class ProxyCondition extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ProxyCondition.AsObject;
  static toObject(includeInstance: boolean, msg: ProxyCondition): ProxyCondition.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ProxyCondition, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ProxyCondition;
  static deserializeBinaryFromReader(message: ProxyCondition, reader: jspb.BinaryReader): ProxyCondition;
}

export namespace ProxyCondition {
  export type AsObject = {
  }
}

export class GetProxyConditionReply extends jspb.Message {
  hasProxyCondition(): boolean;
  clearProxyCondition(): void;
  getProxyCondition(): ProxyCondition | undefined;
  setProxyCondition(value?: ProxyCondition): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProxyConditionReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetProxyConditionReply): GetProxyConditionReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProxyConditionReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProxyConditionReply;
  static deserializeBinaryFromReader(message: GetProxyConditionReply, reader: jspb.BinaryReader): GetProxyConditionReply;
}

export namespace GetProxyConditionReply {
  export type AsObject = {
    proxyCondition?: ProxyCondition.AsObject,
  }
}

export class GetProxyConditionRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProxyConditionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProxyConditionRequest): GetProxyConditionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProxyConditionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProxyConditionRequest;
  static deserializeBinaryFromReader(message: GetProxyConditionRequest, reader: jspb.BinaryReader): GetProxyConditionRequest;
}

export namespace GetProxyConditionRequest {
  export type AsObject = {
  }
}

export class GetProxyReply extends jspb.Message {
  hasProxy(): boolean;
  clearProxy(): void;
  getProxy(): Proxy | undefined;
  setProxy(value?: Proxy): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProxyReply.AsObject;
  static toObject(includeInstance: boolean, msg: GetProxyReply): GetProxyReply.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProxyReply, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProxyReply;
  static deserializeBinaryFromReader(message: GetProxyReply, reader: jspb.BinaryReader): GetProxyReply;
}

export namespace GetProxyReply {
  export type AsObject = {
    proxy?: Proxy.AsObject,
  }
}

export class GetProxyRequest extends jspb.Message {
  hasInput_(): boolean;
  clearInput_(): void;
  getInput_(): ProxyCondition | undefined;
  setInput_(value?: ProxyCondition): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetProxyRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetProxyRequest): GetProxyRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetProxyRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetProxyRequest;
  static deserializeBinaryFromReader(message: GetProxyRequest, reader: jspb.BinaryReader): GetProxyRequest;
}

export namespace GetProxyRequest {
  export type AsObject = {
    input_?: ProxyCondition.AsObject,
  }
}

