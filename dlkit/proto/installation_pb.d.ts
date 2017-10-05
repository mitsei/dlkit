// package: dlkit.proto.installation
// file: dlkit/proto/installation.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_installation_primitives_pb from "../../dlkit/primordium/installation/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_transport_objects_pb from "../../dlkit/primordium/transport/objects_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Package extends jspb.Message {
  getCopyright(): string;
  setCopyright(value: string): void;

  hasCreator(): boolean;
  clearCreator(): void;
  getCreator(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setCreator(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearDependenciesList(): void;
  getDependenciesList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setDependenciesList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addDependencies(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  hasDepot(): boolean;
  clearDepot(): void;
  getDepot(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setDepot(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasReleaseDate(): boolean;
  clearReleaseDate(): void;
  getReleaseDate(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setReleaseDate(value?: google_protobuf_timestamp_pb.Timestamp): void;

  getRequiresLicenseAcknowledgement(): boolean;
  setRequiresLicenseAcknowledgement(value: boolean): void;

  getUrl(): string;
  setUrl(value: string): void;

  hasVersion(): boolean;
  clearVersion(): void;
  getVersion(): dlkit_primordium_installation_primitives_pb.Version | undefined;
  setVersion(value?: dlkit_primordium_installation_primitives_pb.Version): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Package.AsObject;
  static toObject(includeInstance: boolean, msg: Package): Package.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Package, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Package;
  static deserializeBinaryFromReader(message: Package, reader: jspb.BinaryReader): Package;
}

export namespace Package {
  export type AsObject = {
    copyright: string,
    creator?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    dependenciesList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    depot?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    releaseDate?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    requiresLicenseAcknowledgement: boolean,
    url: string,
    version?: dlkit_primordium_installation_primitives_pb.Version.AsObject,
  }
}

export class PackageQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PackageQuery.AsObject;
  static toObject(includeInstance: boolean, msg: PackageQuery): PackageQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PackageQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PackageQuery;
  static deserializeBinaryFromReader(message: PackageQuery, reader: jspb.BinaryReader): PackageQuery;
}

export namespace PackageQuery {
  export type AsObject = {
  }
}

export class PackageQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PackageQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: PackageQueryInspector): PackageQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PackageQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PackageQueryInspector;
  static deserializeBinaryFromReader(message: PackageQueryInspector, reader: jspb.BinaryReader): PackageQueryInspector;
}

export namespace PackageQueryInspector {
  export type AsObject = {
  }
}

export class PackageForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PackageForm.AsObject;
  static toObject(includeInstance: boolean, msg: PackageForm): PackageForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PackageForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PackageForm;
  static deserializeBinaryFromReader(message: PackageForm, reader: jspb.BinaryReader): PackageForm;
}

export namespace PackageForm {
  export type AsObject = {
  }
}

export class PackageSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PackageSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: PackageSearchOrder): PackageSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PackageSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PackageSearchOrder;
  static deserializeBinaryFromReader(message: PackageSearchOrder, reader: jspb.BinaryReader): PackageSearchOrder;
}

export namespace PackageSearchOrder {
  export type AsObject = {
  }
}

export class PackageSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PackageSearch.AsObject;
  static toObject(includeInstance: boolean, msg: PackageSearch): PackageSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PackageSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PackageSearch;
  static deserializeBinaryFromReader(message: PackageSearch, reader: jspb.BinaryReader): PackageSearch;
}

export namespace PackageSearch {
  export type AsObject = {
  }
}

export class PackageSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PackageSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: PackageSearchResults): PackageSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PackageSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PackageSearchResults;
  static deserializeBinaryFromReader(message: PackageSearchResults, reader: jspb.BinaryReader): PackageSearchResults;
}

export namespace PackageSearchResults {
  export type AsObject = {
  }
}

export class PackageList extends jspb.Message {
  clearPackagesList(): void;
  getPackagesList(): Array<Package>;
  setPackagesList(value: Array<Package>): void;
  addPackages(value?: Package, index?: number): Package;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PackageList.AsObject;
  static toObject(includeInstance: boolean, msg: PackageList): PackageList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PackageList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PackageList;
  static deserializeBinaryFromReader(message: PackageList, reader: jspb.BinaryReader): PackageList;
}

export namespace PackageList {
  export type AsObject = {
    packagesList: Array<Package.AsObject>,
  }
}

export class InstallationContent extends jspb.Message {
  hasData(): boolean;
  clearData(): void;
  getData(): dlkit_primordium_transport_objects_pb.DataInputStream | undefined;
  setData(value?: dlkit_primordium_transport_objects_pb.DataInputStream): void;

  hasDepot(): boolean;
  clearDepot(): void;
  getDepot(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setDepot(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasPackage(): boolean;
  clearPackage(): void;
  getPackage(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setPackage(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationContent.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationContent): InstallationContent.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationContent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationContent;
  static deserializeBinaryFromReader(message: InstallationContent, reader: jspb.BinaryReader): InstallationContent;
}

export namespace InstallationContent {
  export type AsObject = {
    data?: dlkit_primordium_transport_objects_pb.DataInputStream.AsObject,
    depot?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    pb_package?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class InstallationContentQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationContentQuery.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationContentQuery): InstallationContentQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationContentQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationContentQuery;
  static deserializeBinaryFromReader(message: InstallationContentQuery, reader: jspb.BinaryReader): InstallationContentQuery;
}

export namespace InstallationContentQuery {
  export type AsObject = {
  }
}

export class InstallationContentQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationContentQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationContentQueryInspector): InstallationContentQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationContentQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationContentQueryInspector;
  static deserializeBinaryFromReader(message: InstallationContentQueryInspector, reader: jspb.BinaryReader): InstallationContentQueryInspector;
}

export namespace InstallationContentQueryInspector {
  export type AsObject = {
  }
}

export class InstallationContentForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationContentForm.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationContentForm): InstallationContentForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationContentForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationContentForm;
  static deserializeBinaryFromReader(message: InstallationContentForm, reader: jspb.BinaryReader): InstallationContentForm;
}

export namespace InstallationContentForm {
  export type AsObject = {
  }
}

export class InstallationContentList extends jspb.Message {
  clearInstallationContentsList(): void;
  getInstallationContentsList(): Array<InstallationContent>;
  setInstallationContentsList(value: Array<InstallationContent>): void;
  addInstallationContents(value?: InstallationContent, index?: number): InstallationContent;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationContentList.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationContentList): InstallationContentList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationContentList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationContentList;
  static deserializeBinaryFromReader(message: InstallationContentList, reader: jspb.BinaryReader): InstallationContentList;
}

export namespace InstallationContentList {
  export type AsObject = {
    installationContentsList: Array<InstallationContent.AsObject>,
  }
}

export class Depot extends jspb.Message {
  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Depot.AsObject;
  static toObject(includeInstance: boolean, msg: Depot): Depot.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Depot, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Depot;
  static deserializeBinaryFromReader(message: Depot, reader: jspb.BinaryReader): Depot;
}

export namespace Depot {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class DepotQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotQuery.AsObject;
  static toObject(includeInstance: boolean, msg: DepotQuery): DepotQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotQuery;
  static deserializeBinaryFromReader(message: DepotQuery, reader: jspb.BinaryReader): DepotQuery;
}

export namespace DepotQuery {
  export type AsObject = {
  }
}

export class DepotQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: DepotQueryInspector): DepotQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotQueryInspector;
  static deserializeBinaryFromReader(message: DepotQueryInspector, reader: jspb.BinaryReader): DepotQueryInspector;
}

export namespace DepotQueryInspector {
  export type AsObject = {
  }
}

export class DepotForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotForm.AsObject;
  static toObject(includeInstance: boolean, msg: DepotForm): DepotForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotForm;
  static deserializeBinaryFromReader(message: DepotForm, reader: jspb.BinaryReader): DepotForm;
}

export namespace DepotForm {
  export type AsObject = {
  }
}

export class DepotSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: DepotSearchOrder): DepotSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotSearchOrder;
  static deserializeBinaryFromReader(message: DepotSearchOrder, reader: jspb.BinaryReader): DepotSearchOrder;
}

export namespace DepotSearchOrder {
  export type AsObject = {
  }
}

export class DepotSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotSearch.AsObject;
  static toObject(includeInstance: boolean, msg: DepotSearch): DepotSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotSearch;
  static deserializeBinaryFromReader(message: DepotSearch, reader: jspb.BinaryReader): DepotSearch;
}

export namespace DepotSearch {
  export type AsObject = {
  }
}

export class DepotSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: DepotSearchResults): DepotSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotSearchResults;
  static deserializeBinaryFromReader(message: DepotSearchResults, reader: jspb.BinaryReader): DepotSearchResults;
}

export namespace DepotSearchResults {
  export type AsObject = {
  }
}

export class DepotList extends jspb.Message {
  clearDepotsList(): void;
  getDepotsList(): Array<Depot>;
  setDepotsList(value: Array<Depot>): void;
  addDepots(value?: Depot, index?: number): Depot;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotList.AsObject;
  static toObject(includeInstance: boolean, msg: DepotList): DepotList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotList;
  static deserializeBinaryFromReader(message: DepotList, reader: jspb.BinaryReader): DepotList;
}

export namespace DepotList {
  export type AsObject = {
    depotsList: Array<Depot.AsObject>,
  }
}

export class DepotNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotNode.AsObject;
  static toObject(includeInstance: boolean, msg: DepotNode): DepotNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotNode;
  static deserializeBinaryFromReader(message: DepotNode, reader: jspb.BinaryReader): DepotNode;
}

export namespace DepotNode {
  export type AsObject = {
  }
}

export class DepotNodeList extends jspb.Message {
  clearDepotNodesList(): void;
  getDepotNodesList(): Array<DepotNode>;
  setDepotNodesList(value: Array<DepotNode>): void;
  addDepotNodes(value?: DepotNode, index?: number): DepotNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DepotNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: DepotNodeList): DepotNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DepotNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DepotNodeList;
  static deserializeBinaryFromReader(message: DepotNodeList, reader: jspb.BinaryReader): DepotNodeList;
}

export namespace DepotNodeList {
  export type AsObject = {
    depotNodesList: Array<DepotNode.AsObject>,
  }
}

export class Installation extends jspb.Message {
  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasPackage(): boolean;
  clearPackage(): void;
  getPackage(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setPackage(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasSite(): boolean;
  clearSite(): void;
  getSite(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSite(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Installation.AsObject;
  static toObject(includeInstance: boolean, msg: Installation): Installation.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Installation, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Installation;
  static deserializeBinaryFromReader(message: Installation, reader: jspb.BinaryReader): Installation;
}

export namespace Installation {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    pb_package?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    site?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class InstallationQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationQuery.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationQuery): InstallationQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationQuery;
  static deserializeBinaryFromReader(message: InstallationQuery, reader: jspb.BinaryReader): InstallationQuery;
}

export namespace InstallationQuery {
  export type AsObject = {
  }
}

export class InstallationQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationQueryInspector): InstallationQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationQueryInspector;
  static deserializeBinaryFromReader(message: InstallationQueryInspector, reader: jspb.BinaryReader): InstallationQueryInspector;
}

export namespace InstallationQueryInspector {
  export type AsObject = {
  }
}

export class InstallationSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationSearchOrder): InstallationSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationSearchOrder;
  static deserializeBinaryFromReader(message: InstallationSearchOrder, reader: jspb.BinaryReader): InstallationSearchOrder;
}

export namespace InstallationSearchOrder {
  export type AsObject = {
  }
}

export class InstallationSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationSearch.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationSearch): InstallationSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationSearch;
  static deserializeBinaryFromReader(message: InstallationSearch, reader: jspb.BinaryReader): InstallationSearch;
}

export namespace InstallationSearch {
  export type AsObject = {
  }
}

export class InstallationSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationSearchResults): InstallationSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationSearchResults;
  static deserializeBinaryFromReader(message: InstallationSearchResults, reader: jspb.BinaryReader): InstallationSearchResults;
}

export namespace InstallationSearchResults {
  export type AsObject = {
  }
}

export class InstallationList extends jspb.Message {
  clearInstallationsList(): void;
  getInstallationsList(): Array<Installation>;
  setInstallationsList(value: Array<Installation>): void;
  addInstallations(value?: Installation, index?: number): Installation;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InstallationList.AsObject;
  static toObject(includeInstance: boolean, msg: InstallationList): InstallationList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InstallationList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InstallationList;
  static deserializeBinaryFromReader(message: InstallationList, reader: jspb.BinaryReader): InstallationList;
}

export namespace InstallationList {
  export type AsObject = {
    installationsList: Array<Installation.AsObject>,
  }
}

export class Site extends jspb.Message {
  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasGenusTypeId(): boolean;
  clearGenusTypeId(): void;
  getGenusTypeId(): dlkit_primordium_type_primitives_pb.Type | undefined;
  setGenusTypeId(value?: dlkit_primordium_type_primitives_pb.Type): void;

  hasId(): boolean;
  clearId(): void;
  getId(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setId(value?: dlkit_primordium_id_primitives_pb.Id): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Site.AsObject;
  static toObject(includeInstance: boolean, msg: Site): Site.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Site, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Site;
  static deserializeBinaryFromReader(message: Site, reader: jspb.BinaryReader): Site;
}

export namespace Site {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class SiteQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SiteQuery.AsObject;
  static toObject(includeInstance: boolean, msg: SiteQuery): SiteQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SiteQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SiteQuery;
  static deserializeBinaryFromReader(message: SiteQuery, reader: jspb.BinaryReader): SiteQuery;
}

export namespace SiteQuery {
  export type AsObject = {
  }
}

export class SiteQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SiteQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: SiteQueryInspector): SiteQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SiteQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SiteQueryInspector;
  static deserializeBinaryFromReader(message: SiteQueryInspector, reader: jspb.BinaryReader): SiteQueryInspector;
}

export namespace SiteQueryInspector {
  export type AsObject = {
  }
}

export class SiteSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SiteSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: SiteSearchOrder): SiteSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SiteSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SiteSearchOrder;
  static deserializeBinaryFromReader(message: SiteSearchOrder, reader: jspb.BinaryReader): SiteSearchOrder;
}

export namespace SiteSearchOrder {
  export type AsObject = {
  }
}

export class SiteList extends jspb.Message {
  clearSitesList(): void;
  getSitesList(): Array<Site>;
  setSitesList(value: Array<Site>): void;
  addSites(value?: Site, index?: number): Site;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SiteList.AsObject;
  static toObject(includeInstance: boolean, msg: SiteList): SiteList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SiteList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SiteList;
  static deserializeBinaryFromReader(message: SiteList, reader: jspb.BinaryReader): SiteList;
}

export namespace SiteList {
  export type AsObject = {
    sitesList: Array<Site.AsObject>,
  }
}

