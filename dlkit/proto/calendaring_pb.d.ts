// package: dlkit.proto.calendaring
// file: dlkit/proto/calendaring.proto

import * as jspb from "google-protobuf";
import * as dlkit_primordium_calendaring_primitives_pb from "../../dlkit/primordium/calendaring/primitives_pb";
import * as dlkit_primordium_id_primitives_pb from "../../dlkit/primordium/id/primitives_pb";
import * as dlkit_primordium_locale_primitives_pb from "../../dlkit/primordium/locale/primitives_pb";
import * as dlkit_primordium_type_primitives_pb from "../../dlkit/primordium/type/primitives_pb";
import * as dlkit_proto_osid_pb from "../../dlkit/proto/osid_pb";
import * as google_protobuf_timestamp_pb from "google-protobuf/google/protobuf/timestamp_pb";

export class Event extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

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

  hasLocation(): boolean;
  clearLocation(): void;
  getLocation(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLocation(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getLocationDescription(): string;
  setLocationDescription(value: string): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  clearSponsorsList(): void;
  getSponsorsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setSponsorsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addSponsors(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Event.AsObject;
  static toObject(includeInstance: boolean, msg: Event): Event.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Event, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Event;
  static deserializeBinaryFromReader(message: Event, reader: jspb.BinaryReader): Event;
}

export namespace Event {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    location?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    locationDescription: string,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    sponsorsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class EventQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EventQuery.AsObject;
  static toObject(includeInstance: boolean, msg: EventQuery): EventQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EventQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EventQuery;
  static deserializeBinaryFromReader(message: EventQuery, reader: jspb.BinaryReader): EventQuery;
}

export namespace EventQuery {
  export type AsObject = {
  }
}

export class EventQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EventQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: EventQueryInspector): EventQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EventQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EventQueryInspector;
  static deserializeBinaryFromReader(message: EventQueryInspector, reader: jspb.BinaryReader): EventQueryInspector;
}

export namespace EventQueryInspector {
  export type AsObject = {
  }
}

export class EventForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EventForm.AsObject;
  static toObject(includeInstance: boolean, msg: EventForm): EventForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EventForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EventForm;
  static deserializeBinaryFromReader(message: EventForm, reader: jspb.BinaryReader): EventForm;
}

export namespace EventForm {
  export type AsObject = {
  }
}

export class EventSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EventSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: EventSearchOrder): EventSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EventSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EventSearchOrder;
  static deserializeBinaryFromReader(message: EventSearchOrder, reader: jspb.BinaryReader): EventSearchOrder;
}

export namespace EventSearchOrder {
  export type AsObject = {
  }
}

export class EventSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EventSearch.AsObject;
  static toObject(includeInstance: boolean, msg: EventSearch): EventSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EventSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EventSearch;
  static deserializeBinaryFromReader(message: EventSearch, reader: jspb.BinaryReader): EventSearch;
}

export namespace EventSearch {
  export type AsObject = {
  }
}

export class EventSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EventSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: EventSearchResults): EventSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EventSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EventSearchResults;
  static deserializeBinaryFromReader(message: EventSearchResults, reader: jspb.BinaryReader): EventSearchResults;
}

export namespace EventSearchResults {
  export type AsObject = {
  }
}

export class EventList extends jspb.Message {
  clearEventsList(): void;
  getEventsList(): Array<Event>;
  setEventsList(value: Array<Event>): void;
  addEvents(value?: Event, index?: number): Event;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): EventList.AsObject;
  static toObject(includeInstance: boolean, msg: EventList): EventList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: EventList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): EventList;
  static deserializeBinaryFromReader(message: EventList, reader: jspb.BinaryReader): EventList;
}

export namespace EventList {
  export type AsObject = {
    eventsList: Array<Event.AsObject>,
  }
}

export class RecurringEvent extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  clearSponsorsList(): void;
  getSponsorsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setSponsorsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addSponsors(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEvent.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEvent): RecurringEvent.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEvent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEvent;
  static deserializeBinaryFromReader(message: RecurringEvent, reader: jspb.BinaryReader): RecurringEvent;
}

export namespace RecurringEvent {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    sponsorsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
  }
}

export class RecurringEventQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEventQuery.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEventQuery): RecurringEventQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEventQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEventQuery;
  static deserializeBinaryFromReader(message: RecurringEventQuery, reader: jspb.BinaryReader): RecurringEventQuery;
}

export namespace RecurringEventQuery {
  export type AsObject = {
  }
}

export class RecurringEventQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEventQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEventQueryInspector): RecurringEventQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEventQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEventQueryInspector;
  static deserializeBinaryFromReader(message: RecurringEventQueryInspector, reader: jspb.BinaryReader): RecurringEventQueryInspector;
}

export namespace RecurringEventQueryInspector {
  export type AsObject = {
  }
}

export class RecurringEventForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEventForm.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEventForm): RecurringEventForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEventForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEventForm;
  static deserializeBinaryFromReader(message: RecurringEventForm, reader: jspb.BinaryReader): RecurringEventForm;
}

export namespace RecurringEventForm {
  export type AsObject = {
  }
}

export class RecurringEventSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEventSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEventSearchOrder): RecurringEventSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEventSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEventSearchOrder;
  static deserializeBinaryFromReader(message: RecurringEventSearchOrder, reader: jspb.BinaryReader): RecurringEventSearchOrder;
}

export namespace RecurringEventSearchOrder {
  export type AsObject = {
  }
}

export class RecurringEventSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEventSearch.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEventSearch): RecurringEventSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEventSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEventSearch;
  static deserializeBinaryFromReader(message: RecurringEventSearch, reader: jspb.BinaryReader): RecurringEventSearch;
}

export namespace RecurringEventSearch {
  export type AsObject = {
  }
}

export class RecurringEventSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEventSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEventSearchResults): RecurringEventSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEventSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEventSearchResults;
  static deserializeBinaryFromReader(message: RecurringEventSearchResults, reader: jspb.BinaryReader): RecurringEventSearchResults;
}

export namespace RecurringEventSearchResults {
  export type AsObject = {
  }
}

export class RecurringEventList extends jspb.Message {
  clearRecurringEventsList(): void;
  getRecurringEventsList(): Array<RecurringEvent>;
  setRecurringEventsList(value: Array<RecurringEvent>): void;
  addRecurringEvents(value?: RecurringEvent, index?: number): RecurringEvent;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RecurringEventList.AsObject;
  static toObject(includeInstance: boolean, msg: RecurringEventList): RecurringEventList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RecurringEventList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RecurringEventList;
  static deserializeBinaryFromReader(message: RecurringEventList, reader: jspb.BinaryReader): RecurringEventList;
}

export namespace RecurringEventList {
  export type AsObject = {
    recurringEventsList: Array<RecurringEvent.AsObject>,
  }
}

export class SupersedingEvent extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasSupersededDate(): boolean;
  clearSupersededDate(): void;
  getSupersededDate(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setSupersededDate(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasSupersededEvent(): boolean;
  clearSupersededEvent(): void;
  getSupersededEvent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSupersededEvent(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getSupersededEventPosition(): number;
  setSupersededEventPosition(value: number): void;

  hasSupersedingEvent(): boolean;
  clearSupersedingEvent(): void;
  getSupersedingEvent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setSupersedingEvent(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEvent.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEvent): SupersedingEvent.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEvent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEvent;
  static deserializeBinaryFromReader(message: SupersedingEvent, reader: jspb.BinaryReader): SupersedingEvent;
}

export namespace SupersedingEvent {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    supersededDate?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    supersededEvent?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    supersededEventPosition: number,
    supersedingEvent?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class SupersedingEventQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEventQuery.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEventQuery): SupersedingEventQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEventQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEventQuery;
  static deserializeBinaryFromReader(message: SupersedingEventQuery, reader: jspb.BinaryReader): SupersedingEventQuery;
}

export namespace SupersedingEventQuery {
  export type AsObject = {
  }
}

export class SupersedingEventQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEventQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEventQueryInspector): SupersedingEventQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEventQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEventQueryInspector;
  static deserializeBinaryFromReader(message: SupersedingEventQueryInspector, reader: jspb.BinaryReader): SupersedingEventQueryInspector;
}

export namespace SupersedingEventQueryInspector {
  export type AsObject = {
  }
}

export class SupersedingEventForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEventForm.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEventForm): SupersedingEventForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEventForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEventForm;
  static deserializeBinaryFromReader(message: SupersedingEventForm, reader: jspb.BinaryReader): SupersedingEventForm;
}

export namespace SupersedingEventForm {
  export type AsObject = {
  }
}

export class SupersedingEventSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEventSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEventSearchOrder): SupersedingEventSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEventSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEventSearchOrder;
  static deserializeBinaryFromReader(message: SupersedingEventSearchOrder, reader: jspb.BinaryReader): SupersedingEventSearchOrder;
}

export namespace SupersedingEventSearchOrder {
  export type AsObject = {
  }
}

export class SupersedingEventSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEventSearch.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEventSearch): SupersedingEventSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEventSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEventSearch;
  static deserializeBinaryFromReader(message: SupersedingEventSearch, reader: jspb.BinaryReader): SupersedingEventSearch;
}

export namespace SupersedingEventSearch {
  export type AsObject = {
  }
}

export class SupersedingEventSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEventSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEventSearchResults): SupersedingEventSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEventSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEventSearchResults;
  static deserializeBinaryFromReader(message: SupersedingEventSearchResults, reader: jspb.BinaryReader): SupersedingEventSearchResults;
}

export namespace SupersedingEventSearchResults {
  export type AsObject = {
  }
}

export class SupersedingEventList extends jspb.Message {
  clearSupersedingEventsList(): void;
  getSupersedingEventsList(): Array<SupersedingEvent>;
  setSupersedingEventsList(value: Array<SupersedingEvent>): void;
  addSupersedingEvents(value?: SupersedingEvent, index?: number): SupersedingEvent;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SupersedingEventList.AsObject;
  static toObject(includeInstance: boolean, msg: SupersedingEventList): SupersedingEventList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SupersedingEventList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SupersedingEventList;
  static deserializeBinaryFromReader(message: SupersedingEventList, reader: jspb.BinaryReader): SupersedingEventList;
}

export namespace SupersedingEventList {
  export type AsObject = {
    supersedingEventsList: Array<SupersedingEvent.AsObject>,
  }
}

export class OffsetEvent extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasEndReferenceEvent(): boolean;
  clearEndReferenceEvent(): void;
  getEndReferenceEvent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setEndReferenceEvent(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasFixedDuration(): boolean;
  clearFixedDuration(): void;
  getFixedDuration(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setFixedDuration(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

  hasFixedEndOffset(): boolean;
  clearFixedEndOffset(): void;
  getFixedEndOffset(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setFixedEndOffset(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

  hasFixedStartOffset(): boolean;
  clearFixedStartOffset(): void;
  getFixedStartOffset(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setFixedStartOffset(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

  hasFixedStartTime(): boolean;
  clearFixedStartTime(): void;
  getFixedStartTime(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setFixedStartTime(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasLocation(): boolean;
  clearLocation(): void;
  getLocation(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLocation(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getLocationDescription(): string;
  setLocationDescription(value: string): void;

  getRelativeEndWeekday(): number;
  setRelativeEndWeekday(value: number): void;

  getRelativeStartWeekday(): number;
  setRelativeStartWeekday(value: number): void;

  getRelativeWeekdayEndOffset(): number;
  setRelativeWeekdayEndOffset(value: number): void;

  getRelativeWeekdayStartOffset(): number;
  setRelativeWeekdayStartOffset(value: number): void;

  clearSponsorsList(): void;
  getSponsorsList(): Array<dlkit_primordium_id_primitives_pb.Id>;
  setSponsorsList(value: Array<dlkit_primordium_id_primitives_pb.Id>): void;
  addSponsors(value?: dlkit_primordium_id_primitives_pb.Id, index?: number): dlkit_primordium_id_primitives_pb.Id;

  hasStartReferenceEvent(): boolean;
  clearStartReferenceEvent(): void;
  getStartReferenceEvent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setStartReferenceEvent(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEvent.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEvent): OffsetEvent.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEvent, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEvent;
  static deserializeBinaryFromReader(message: OffsetEvent, reader: jspb.BinaryReader): OffsetEvent;
}

export namespace OffsetEvent {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    endReferenceEvent?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    fixedDuration?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    fixedEndOffset?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    fixedStartOffset?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    fixedStartTime?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    location?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    locationDescription: string,
    relativeEndWeekday: number,
    relativeStartWeekday: number,
    relativeWeekdayEndOffset: number,
    relativeWeekdayStartOffset: number,
    sponsorsList: Array<dlkit_primordium_id_primitives_pb.Id.AsObject>,
    startReferenceEvent?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class OffsetEventQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEventQuery.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEventQuery): OffsetEventQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEventQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEventQuery;
  static deserializeBinaryFromReader(message: OffsetEventQuery, reader: jspb.BinaryReader): OffsetEventQuery;
}

export namespace OffsetEventQuery {
  export type AsObject = {
  }
}

export class OffsetEventQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEventQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEventQueryInspector): OffsetEventQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEventQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEventQueryInspector;
  static deserializeBinaryFromReader(message: OffsetEventQueryInspector, reader: jspb.BinaryReader): OffsetEventQueryInspector;
}

export namespace OffsetEventQueryInspector {
  export type AsObject = {
  }
}

export class OffsetEventForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEventForm.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEventForm): OffsetEventForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEventForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEventForm;
  static deserializeBinaryFromReader(message: OffsetEventForm, reader: jspb.BinaryReader): OffsetEventForm;
}

export namespace OffsetEventForm {
  export type AsObject = {
  }
}

export class OffsetEventSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEventSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEventSearchOrder): OffsetEventSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEventSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEventSearchOrder;
  static deserializeBinaryFromReader(message: OffsetEventSearchOrder, reader: jspb.BinaryReader): OffsetEventSearchOrder;
}

export namespace OffsetEventSearchOrder {
  export type AsObject = {
  }
}

export class OffsetEventSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEventSearch.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEventSearch): OffsetEventSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEventSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEventSearch;
  static deserializeBinaryFromReader(message: OffsetEventSearch, reader: jspb.BinaryReader): OffsetEventSearch;
}

export namespace OffsetEventSearch {
  export type AsObject = {
  }
}

export class OffsetEventSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEventSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEventSearchResults): OffsetEventSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEventSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEventSearchResults;
  static deserializeBinaryFromReader(message: OffsetEventSearchResults, reader: jspb.BinaryReader): OffsetEventSearchResults;
}

export namespace OffsetEventSearchResults {
  export type AsObject = {
  }
}

export class OffsetEventList extends jspb.Message {
  clearOffsetEventsList(): void;
  getOffsetEventsList(): Array<OffsetEvent>;
  setOffsetEventsList(value: Array<OffsetEvent>): void;
  addOffsetEvents(value?: OffsetEvent, index?: number): OffsetEvent;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): OffsetEventList.AsObject;
  static toObject(includeInstance: boolean, msg: OffsetEventList): OffsetEventList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: OffsetEventList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): OffsetEventList;
  static deserializeBinaryFromReader(message: OffsetEventList, reader: jspb.BinaryReader): OffsetEventList;
}

export namespace OffsetEventList {
  export type AsObject = {
    offsetEventsList: Array<OffsetEvent.AsObject>,
  }
}

export class Schedule extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

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

  clearLimitList(): void;
  getLimitList(): Array<number>;
  setLimitList(value: Array<number>): void;
  addLimit(value: number, index?: number): number;

  hasLocation(): boolean;
  clearLocation(): void;
  getLocation(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setLocation(value?: dlkit_primordium_id_primitives_pb.Id): void;

  getLocationDescription(): string;
  setLocationDescription(value: string): void;

  clearRecordTypeIdsList(): void;
  getRecordTypeIdsList(): Array<dlkit_primordium_type_primitives_pb.Type>;
  setRecordTypeIdsList(value: Array<dlkit_primordium_type_primitives_pb.Type>): void;
  addRecordTypeIds(value?: dlkit_primordium_type_primitives_pb.Type, index?: number): dlkit_primordium_type_primitives_pb.Type;

  hasScheduleEnd(): boolean;
  clearScheduleEnd(): void;
  getScheduleEnd(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setScheduleEnd(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasScheduleSlot(): boolean;
  clearScheduleSlot(): void;
  getScheduleSlot(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setScheduleSlot(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasScheduleStart(): boolean;
  clearScheduleStart(): void;
  getScheduleStart(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setScheduleStart(value?: google_protobuf_timestamp_pb.Timestamp): void;

  hasTimePeriod(): boolean;
  clearTimePeriod(): void;
  getTimePeriod(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setTimePeriod(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Schedule.AsObject;
  static toObject(includeInstance: boolean, msg: Schedule): Schedule.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Schedule, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Schedule;
  static deserializeBinaryFromReader(message: Schedule, reader: jspb.BinaryReader): Schedule;
}

export namespace Schedule {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    limitList: Array<number>,
    location?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    locationDescription: string,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    scheduleEnd?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    scheduleSlot?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    scheduleStart?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    timePeriod?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class ScheduleQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleQuery): ScheduleQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleQuery;
  static deserializeBinaryFromReader(message: ScheduleQuery, reader: jspb.BinaryReader): ScheduleQuery;
}

export namespace ScheduleQuery {
  export type AsObject = {
  }
}

export class ScheduleQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleQueryInspector): ScheduleQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleQueryInspector;
  static deserializeBinaryFromReader(message: ScheduleQueryInspector, reader: jspb.BinaryReader): ScheduleQueryInspector;
}

export namespace ScheduleQueryInspector {
  export type AsObject = {
  }
}

export class ScheduleForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleForm.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleForm): ScheduleForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleForm;
  static deserializeBinaryFromReader(message: ScheduleForm, reader: jspb.BinaryReader): ScheduleForm;
}

export namespace ScheduleForm {
  export type AsObject = {
  }
}

export class ScheduleSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSearchOrder): ScheduleSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSearchOrder;
  static deserializeBinaryFromReader(message: ScheduleSearchOrder, reader: jspb.BinaryReader): ScheduleSearchOrder;
}

export namespace ScheduleSearchOrder {
  export type AsObject = {
  }
}

export class ScheduleSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSearch): ScheduleSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSearch;
  static deserializeBinaryFromReader(message: ScheduleSearch, reader: jspb.BinaryReader): ScheduleSearch;
}

export namespace ScheduleSearch {
  export type AsObject = {
  }
}

export class ScheduleSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSearchResults): ScheduleSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSearchResults;
  static deserializeBinaryFromReader(message: ScheduleSearchResults, reader: jspb.BinaryReader): ScheduleSearchResults;
}

export namespace ScheduleSearchResults {
  export type AsObject = {
  }
}

export class ScheduleList extends jspb.Message {
  clearSchedulesList(): void;
  getSchedulesList(): Array<Schedule>;
  setSchedulesList(value: Array<Schedule>): void;
  addSchedules(value?: Schedule, index?: number): Schedule;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleList.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleList): ScheduleList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleList;
  static deserializeBinaryFromReader(message: ScheduleList, reader: jspb.BinaryReader): ScheduleList;
}

export namespace ScheduleList {
  export type AsObject = {
    schedulesList: Array<Schedule.AsObject>,
  }
}

export class ScheduleSlot extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDuration(): boolean;
  clearDuration(): void;
  getDuration(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setDuration(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

  hasFixedInterval(): boolean;
  clearFixedInterval(): void;
  getFixedInterval(): dlkit_primordium_calendaring_primitives_pb.Duration | undefined;
  setFixedInterval(value?: dlkit_primordium_calendaring_primitives_pb.Duration): void;

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

  getWeekOfMonth(): number;
  setWeekOfMonth(value: number): void;

  hasWeekdayTime(): boolean;
  clearWeekdayTime(): void;
  getWeekdayTime(): dlkit_primordium_calendaring_primitives_pb.Time | undefined;
  setWeekdayTime(value?: dlkit_primordium_calendaring_primitives_pb.Time): void;

  clearWeekdaysList(): void;
  getWeekdaysList(): Array<number>;
  setWeekdaysList(value: Array<number>): void;
  addWeekdays(value: number, index?: number): number;

  getWeeklyInterval(): number;
  setWeeklyInterval(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlot.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlot): ScheduleSlot.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlot, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlot;
  static deserializeBinaryFromReader(message: ScheduleSlot, reader: jspb.BinaryReader): ScheduleSlot;
}

export namespace ScheduleSlot {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    duration?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    fixedInterval?: dlkit_primordium_calendaring_primitives_pb.Duration.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    weekOfMonth: number,
    weekdayTime?: dlkit_primordium_calendaring_primitives_pb.Time.AsObject,
    weekdaysList: Array<number>,
    weeklyInterval: number,
  }
}

export class ScheduleSlotQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlotQuery.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlotQuery): ScheduleSlotQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlotQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlotQuery;
  static deserializeBinaryFromReader(message: ScheduleSlotQuery, reader: jspb.BinaryReader): ScheduleSlotQuery;
}

export namespace ScheduleSlotQuery {
  export type AsObject = {
  }
}

export class ScheduleSlotQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlotQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlotQueryInspector): ScheduleSlotQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlotQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlotQueryInspector;
  static deserializeBinaryFromReader(message: ScheduleSlotQueryInspector, reader: jspb.BinaryReader): ScheduleSlotQueryInspector;
}

export namespace ScheduleSlotQueryInspector {
  export type AsObject = {
  }
}

export class ScheduleSlotForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlotForm.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlotForm): ScheduleSlotForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlotForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlotForm;
  static deserializeBinaryFromReader(message: ScheduleSlotForm, reader: jspb.BinaryReader): ScheduleSlotForm;
}

export namespace ScheduleSlotForm {
  export type AsObject = {
  }
}

export class ScheduleSlotSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlotSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlotSearchOrder): ScheduleSlotSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlotSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlotSearchOrder;
  static deserializeBinaryFromReader(message: ScheduleSlotSearchOrder, reader: jspb.BinaryReader): ScheduleSlotSearchOrder;
}

export namespace ScheduleSlotSearchOrder {
  export type AsObject = {
  }
}

export class ScheduleSlotSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlotSearch.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlotSearch): ScheduleSlotSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlotSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlotSearch;
  static deserializeBinaryFromReader(message: ScheduleSlotSearch, reader: jspb.BinaryReader): ScheduleSlotSearch;
}

export namespace ScheduleSlotSearch {
  export type AsObject = {
  }
}

export class ScheduleSlotSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlotSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlotSearchResults): ScheduleSlotSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlotSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlotSearchResults;
  static deserializeBinaryFromReader(message: ScheduleSlotSearchResults, reader: jspb.BinaryReader): ScheduleSlotSearchResults;
}

export namespace ScheduleSlotSearchResults {
  export type AsObject = {
  }
}

export class ScheduleSlotList extends jspb.Message {
  clearScheduleSlotsList(): void;
  getScheduleSlotsList(): Array<ScheduleSlot>;
  setScheduleSlotsList(value: Array<ScheduleSlot>): void;
  addScheduleSlots(value?: ScheduleSlot, index?: number): ScheduleSlot;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ScheduleSlotList.AsObject;
  static toObject(includeInstance: boolean, msg: ScheduleSlotList): ScheduleSlotList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ScheduleSlotList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ScheduleSlotList;
  static deserializeBinaryFromReader(message: ScheduleSlotList, reader: jspb.BinaryReader): ScheduleSlotList;
}

export namespace ScheduleSlotList {
  export type AsObject = {
    scheduleSlotsList: Array<ScheduleSlot.AsObject>,
  }
}

export class TimePeriod extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasDescription(): boolean;
  clearDescription(): void;
  getDescription(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDescription(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasDisplayName(): boolean;
  clearDisplayName(): void;
  getDisplayName(): dlkit_primordium_locale_primitives_pb.DisplayText | undefined;
  setDisplayName(value?: dlkit_primordium_locale_primitives_pb.DisplayText): void;

  hasEnd(): boolean;
  clearEnd(): void;
  getEnd(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setEnd(value?: google_protobuf_timestamp_pb.Timestamp): void;

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

  hasStart(): boolean;
  clearStart(): void;
  getStart(): google_protobuf_timestamp_pb.Timestamp | undefined;
  setStart(value?: google_protobuf_timestamp_pb.Timestamp): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriod.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriod): TimePeriod.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriod, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriod;
  static deserializeBinaryFromReader(message: TimePeriod, reader: jspb.BinaryReader): TimePeriod;
}

export namespace TimePeriod {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    end?: google_protobuf_timestamp_pb.Timestamp.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
    start?: google_protobuf_timestamp_pb.Timestamp.AsObject,
  }
}

export class TimePeriodQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriodQuery.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriodQuery): TimePeriodQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriodQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriodQuery;
  static deserializeBinaryFromReader(message: TimePeriodQuery, reader: jspb.BinaryReader): TimePeriodQuery;
}

export namespace TimePeriodQuery {
  export type AsObject = {
  }
}

export class TimePeriodQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriodQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriodQueryInspector): TimePeriodQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriodQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriodQueryInspector;
  static deserializeBinaryFromReader(message: TimePeriodQueryInspector, reader: jspb.BinaryReader): TimePeriodQueryInspector;
}

export namespace TimePeriodQueryInspector {
  export type AsObject = {
  }
}

export class TimePeriodForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriodForm.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriodForm): TimePeriodForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriodForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriodForm;
  static deserializeBinaryFromReader(message: TimePeriodForm, reader: jspb.BinaryReader): TimePeriodForm;
}

export namespace TimePeriodForm {
  export type AsObject = {
  }
}

export class TimePeriodSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriodSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriodSearchOrder): TimePeriodSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriodSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriodSearchOrder;
  static deserializeBinaryFromReader(message: TimePeriodSearchOrder, reader: jspb.BinaryReader): TimePeriodSearchOrder;
}

export namespace TimePeriodSearchOrder {
  export type AsObject = {
  }
}

export class TimePeriodSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriodSearch.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriodSearch): TimePeriodSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriodSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriodSearch;
  static deserializeBinaryFromReader(message: TimePeriodSearch, reader: jspb.BinaryReader): TimePeriodSearch;
}

export namespace TimePeriodSearch {
  export type AsObject = {
  }
}

export class TimePeriodSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriodSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriodSearchResults): TimePeriodSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriodSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriodSearchResults;
  static deserializeBinaryFromReader(message: TimePeriodSearchResults, reader: jspb.BinaryReader): TimePeriodSearchResults;
}

export namespace TimePeriodSearchResults {
  export type AsObject = {
  }
}

export class TimePeriodList extends jspb.Message {
  clearTimePeriodsList(): void;
  getTimePeriodsList(): Array<TimePeriod>;
  setTimePeriodsList(value: Array<TimePeriod>): void;
  addTimePeriods(value?: TimePeriod, index?: number): TimePeriod;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimePeriodList.AsObject;
  static toObject(includeInstance: boolean, msg: TimePeriodList): TimePeriodList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimePeriodList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimePeriodList;
  static deserializeBinaryFromReader(message: TimePeriodList, reader: jspb.BinaryReader): TimePeriodList;
}

export namespace TimePeriodList {
  export type AsObject = {
    timePeriodsList: Array<TimePeriod.AsObject>,
  }
}

export class Commitment extends jspb.Message {
  hasCalendar(): boolean;
  clearCalendar(): void;
  getCalendar(): dlkit_proto_osid_pb.OsidCatalog | undefined;
  setCalendar(value?: dlkit_proto_osid_pb.OsidCatalog): void;

  hasEvent(): boolean;
  clearEvent(): void;
  getEvent(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setEvent(value?: dlkit_primordium_id_primitives_pb.Id): void;

  hasResource(): boolean;
  clearResource(): void;
  getResource(): dlkit_primordium_id_primitives_pb.Id | undefined;
  setResource(value?: dlkit_primordium_id_primitives_pb.Id): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Commitment.AsObject;
  static toObject(includeInstance: boolean, msg: Commitment): Commitment.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Commitment, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Commitment;
  static deserializeBinaryFromReader(message: Commitment, reader: jspb.BinaryReader): Commitment;
}

export namespace Commitment {
  export type AsObject = {
    calendar?: dlkit_proto_osid_pb.OsidCatalog.AsObject,
    event?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    resource?: dlkit_primordium_id_primitives_pb.Id.AsObject,
  }
}

export class CommitmentQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommitmentQuery.AsObject;
  static toObject(includeInstance: boolean, msg: CommitmentQuery): CommitmentQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommitmentQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommitmentQuery;
  static deserializeBinaryFromReader(message: CommitmentQuery, reader: jspb.BinaryReader): CommitmentQuery;
}

export namespace CommitmentQuery {
  export type AsObject = {
  }
}

export class CommitmentQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommitmentQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: CommitmentQueryInspector): CommitmentQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommitmentQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommitmentQueryInspector;
  static deserializeBinaryFromReader(message: CommitmentQueryInspector, reader: jspb.BinaryReader): CommitmentQueryInspector;
}

export namespace CommitmentQueryInspector {
  export type AsObject = {
  }
}

export class CommitmentForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommitmentForm.AsObject;
  static toObject(includeInstance: boolean, msg: CommitmentForm): CommitmentForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommitmentForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommitmentForm;
  static deserializeBinaryFromReader(message: CommitmentForm, reader: jspb.BinaryReader): CommitmentForm;
}

export namespace CommitmentForm {
  export type AsObject = {
  }
}

export class CommitmentSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommitmentSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: CommitmentSearchOrder): CommitmentSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommitmentSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommitmentSearchOrder;
  static deserializeBinaryFromReader(message: CommitmentSearchOrder, reader: jspb.BinaryReader): CommitmentSearchOrder;
}

export namespace CommitmentSearchOrder {
  export type AsObject = {
  }
}

export class CommitmentSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommitmentSearch.AsObject;
  static toObject(includeInstance: boolean, msg: CommitmentSearch): CommitmentSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommitmentSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommitmentSearch;
  static deserializeBinaryFromReader(message: CommitmentSearch, reader: jspb.BinaryReader): CommitmentSearch;
}

export namespace CommitmentSearch {
  export type AsObject = {
  }
}

export class CommitmentSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommitmentSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: CommitmentSearchResults): CommitmentSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommitmentSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommitmentSearchResults;
  static deserializeBinaryFromReader(message: CommitmentSearchResults, reader: jspb.BinaryReader): CommitmentSearchResults;
}

export namespace CommitmentSearchResults {
  export type AsObject = {
  }
}

export class CommitmentList extends jspb.Message {
  clearCommitmentsList(): void;
  getCommitmentsList(): Array<Commitment>;
  setCommitmentsList(value: Array<Commitment>): void;
  addCommitments(value?: Commitment, index?: number): Commitment;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommitmentList.AsObject;
  static toObject(includeInstance: boolean, msg: CommitmentList): CommitmentList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CommitmentList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommitmentList;
  static deserializeBinaryFromReader(message: CommitmentList, reader: jspb.BinaryReader): CommitmentList;
}

export namespace CommitmentList {
  export type AsObject = {
    commitmentsList: Array<Commitment.AsObject>,
  }
}

export class Calendar extends jspb.Message {
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
  toObject(includeInstance?: boolean): Calendar.AsObject;
  static toObject(includeInstance: boolean, msg: Calendar): Calendar.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Calendar, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Calendar;
  static deserializeBinaryFromReader(message: Calendar, reader: jspb.BinaryReader): Calendar;
}

export namespace Calendar {
  export type AsObject = {
    description?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    displayName?: dlkit_primordium_locale_primitives_pb.DisplayText.AsObject,
    genusTypeId?: dlkit_primordium_type_primitives_pb.Type.AsObject,
    id?: dlkit_primordium_id_primitives_pb.Id.AsObject,
    recordTypeIdsList: Array<dlkit_primordium_type_primitives_pb.Type.AsObject>,
  }
}

export class CalendarQuery extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarQuery.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarQuery): CalendarQuery.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarQuery, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarQuery;
  static deserializeBinaryFromReader(message: CalendarQuery, reader: jspb.BinaryReader): CalendarQuery;
}

export namespace CalendarQuery {
  export type AsObject = {
  }
}

export class CalendarQueryInspector extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarQueryInspector.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarQueryInspector): CalendarQueryInspector.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarQueryInspector, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarQueryInspector;
  static deserializeBinaryFromReader(message: CalendarQueryInspector, reader: jspb.BinaryReader): CalendarQueryInspector;
}

export namespace CalendarQueryInspector {
  export type AsObject = {
  }
}

export class CalendarForm extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarForm.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarForm): CalendarForm.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarForm, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarForm;
  static deserializeBinaryFromReader(message: CalendarForm, reader: jspb.BinaryReader): CalendarForm;
}

export namespace CalendarForm {
  export type AsObject = {
  }
}

export class CalendarSearchOrder extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarSearchOrder.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarSearchOrder): CalendarSearchOrder.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarSearchOrder, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarSearchOrder;
  static deserializeBinaryFromReader(message: CalendarSearchOrder, reader: jspb.BinaryReader): CalendarSearchOrder;
}

export namespace CalendarSearchOrder {
  export type AsObject = {
  }
}

export class CalendarSearch extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarSearch.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarSearch): CalendarSearch.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarSearch, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarSearch;
  static deserializeBinaryFromReader(message: CalendarSearch, reader: jspb.BinaryReader): CalendarSearch;
}

export namespace CalendarSearch {
  export type AsObject = {
  }
}

export class CalendarSearchResults extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarSearchResults.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarSearchResults): CalendarSearchResults.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarSearchResults, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarSearchResults;
  static deserializeBinaryFromReader(message: CalendarSearchResults, reader: jspb.BinaryReader): CalendarSearchResults;
}

export namespace CalendarSearchResults {
  export type AsObject = {
  }
}

export class CalendarList extends jspb.Message {
  clearCalendarsList(): void;
  getCalendarsList(): Array<Calendar>;
  setCalendarsList(value: Array<Calendar>): void;
  addCalendars(value?: Calendar, index?: number): Calendar;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarList.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarList): CalendarList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarList;
  static deserializeBinaryFromReader(message: CalendarList, reader: jspb.BinaryReader): CalendarList;
}

export namespace CalendarList {
  export type AsObject = {
    calendarsList: Array<Calendar.AsObject>,
  }
}

export class CalendarNode extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarNode.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarNode): CalendarNode.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarNode, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarNode;
  static deserializeBinaryFromReader(message: CalendarNode, reader: jspb.BinaryReader): CalendarNode;
}

export namespace CalendarNode {
  export type AsObject = {
  }
}

export class CalendarNodeList extends jspb.Message {
  clearCalendarNodesList(): void;
  getCalendarNodesList(): Array<CalendarNode>;
  setCalendarNodesList(value: Array<CalendarNode>): void;
  addCalendarNodes(value?: CalendarNode, index?: number): CalendarNode;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CalendarNodeList.AsObject;
  static toObject(includeInstance: boolean, msg: CalendarNodeList): CalendarNodeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: CalendarNodeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CalendarNodeList;
  static deserializeBinaryFromReader(message: CalendarNodeList, reader: jspb.BinaryReader): CalendarNodeList;
}

export namespace CalendarNodeList {
  export type AsObject = {
    calendarNodesList: Array<CalendarNode.AsObject>,
  }
}

export class MeetingTime extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MeetingTime.AsObject;
  static toObject(includeInstance: boolean, msg: MeetingTime): MeetingTime.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MeetingTime, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MeetingTime;
  static deserializeBinaryFromReader(message: MeetingTime, reader: jspb.BinaryReader): MeetingTime;
}

export namespace MeetingTime {
  export type AsObject = {
  }
}

export class MeetingTimeList extends jspb.Message {
  clearMeetingTimesList(): void;
  getMeetingTimesList(): Array<MeetingTime>;
  setMeetingTimesList(value: Array<MeetingTime>): void;
  addMeetingTimes(value?: MeetingTime, index?: number): MeetingTime;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): MeetingTimeList.AsObject;
  static toObject(includeInstance: boolean, msg: MeetingTimeList): MeetingTimeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: MeetingTimeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): MeetingTimeList;
  static deserializeBinaryFromReader(message: MeetingTimeList, reader: jspb.BinaryReader): MeetingTimeList;
}

export namespace MeetingTimeList {
  export type AsObject = {
    meetingTimesList: Array<MeetingTime.AsObject>,
  }
}

export class TimeList extends jspb.Message {
  clearTimesList(): void;
  getTimesList(): Array<dlkit_primordium_calendaring_primitives_pb.Time>;
  setTimesList(value: Array<dlkit_primordium_calendaring_primitives_pb.Time>): void;
  addTimes(value?: dlkit_primordium_calendaring_primitives_pb.Time, index?: number): dlkit_primordium_calendaring_primitives_pb.Time;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TimeList.AsObject;
  static toObject(includeInstance: boolean, msg: TimeList): TimeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: TimeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TimeList;
  static deserializeBinaryFromReader(message: TimeList, reader: jspb.BinaryReader): TimeList;
}

export namespace TimeList {
  export type AsObject = {
    timesList: Array<dlkit_primordium_calendaring_primitives_pb.Time.AsObject>,
  }
}

export class DateTimeList extends jspb.Message {
  clearDateTimesList(): void;
  getDateTimesList(): Array<google_protobuf_timestamp_pb.Timestamp>;
  setDateTimesList(value: Array<google_protobuf_timestamp_pb.Timestamp>): void;
  addDateTimes(value?: google_protobuf_timestamp_pb.Timestamp, index?: number): google_protobuf_timestamp_pb.Timestamp;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DateTimeList.AsObject;
  static toObject(includeInstance: boolean, msg: DateTimeList): DateTimeList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DateTimeList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DateTimeList;
  static deserializeBinaryFromReader(message: DateTimeList, reader: jspb.BinaryReader): DateTimeList;
}

export namespace DateTimeList {
  export type AsObject = {
    dateTimesList: Array<google_protobuf_timestamp_pb.Timestamp.AsObject>,
  }
}

export class DurationList extends jspb.Message {
  clearDurationsList(): void;
  getDurationsList(): Array<dlkit_primordium_calendaring_primitives_pb.Duration>;
  setDurationsList(value: Array<dlkit_primordium_calendaring_primitives_pb.Duration>): void;
  addDurations(value?: dlkit_primordium_calendaring_primitives_pb.Duration, index?: number): dlkit_primordium_calendaring_primitives_pb.Duration;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DurationList.AsObject;
  static toObject(includeInstance: boolean, msg: DurationList): DurationList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DurationList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DurationList;
  static deserializeBinaryFromReader(message: DurationList, reader: jspb.BinaryReader): DurationList;
}

export namespace DurationList {
  export type AsObject = {
    durationsList: Array<dlkit_primordium_calendaring_primitives_pb.Duration.AsObject>,
  }
}

export class DateTimeInterval extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DateTimeInterval.AsObject;
  static toObject(includeInstance: boolean, msg: DateTimeInterval): DateTimeInterval.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DateTimeInterval, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DateTimeInterval;
  static deserializeBinaryFromReader(message: DateTimeInterval, reader: jspb.BinaryReader): DateTimeInterval;
}

export namespace DateTimeInterval {
  export type AsObject = {
  }
}

export class DateTimeIntervalList extends jspb.Message {
  clearDateTimeIntervalsList(): void;
  getDateTimeIntervalsList(): Array<dlkit_primordium_calendaring_primitives_pb.DateTimeInterval>;
  setDateTimeIntervalsList(value: Array<dlkit_primordium_calendaring_primitives_pb.DateTimeInterval>): void;
  addDateTimeIntervals(value?: dlkit_primordium_calendaring_primitives_pb.DateTimeInterval, index?: number): dlkit_primordium_calendaring_primitives_pb.DateTimeInterval;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DateTimeIntervalList.AsObject;
  static toObject(includeInstance: boolean, msg: DateTimeIntervalList): DateTimeIntervalList.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: DateTimeIntervalList, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DateTimeIntervalList;
  static deserializeBinaryFromReader(message: DateTimeIntervalList, reader: jspb.BinaryReader): DateTimeIntervalList;
}

export namespace DateTimeIntervalList {
  export type AsObject = {
    dateTimeIntervalsList: Array<dlkit_primordium_calendaring_primitives_pb.DateTimeInterval.AsObject>,
  }
}

