from dlkit.json_.resource import sessions as json_resource_sessions
from dlkit.primordium.id import primitives_pb2 as id_primitives
from dlkit.primordium.locale import primitives_pb2 as locale_primitives
from dlkit.primordium.type import primitives_pb2 as type_primitives
from dlkit.proto import resource_pb2
from dlkit.proto import resource_pb2_grpc


class BinLookupSessionServicer(resource_pb2_grpc.BinLookupSessionServicer,
                               json_resource_sessions.BinLookupSession):
    def __init__(self, runtime):
        # Deal with runtime and initialization somehow?
        self._runtime = runtime
        self._catalog_session = None
        self._proxy = None

    def GetBins(self, request, context):
        for bin_ in self.get_bins():
            yield resource_pb2.Bin(
                displayName=locale_primitives.DisplayText(
                    text=bin_.display_name.text,
                    format_type_id=type_primitives.Type(
                        authority=bin_.display_name.format_type.authority,
                        identifier=bin_.display_name.format_type.identifier,
                        namespace=bin_.display_name.format_type.namespace
                    ),
                    language_type_id=type_primitives.Type(
                        authority=bin_.display_name.language_type.authority,
                        identifier=bin_.display_name.language_type.identifier,
                        namespace=bin_.display_name.language_type.namespace
                    ),
                    script_type_id=type_primitives.Type(
                        authority=bin_.display_name.script_type.authority,
                        identifier=bin_.display_name.script_type.identifier,
                        namespace=bin_.display_name.script_type.namespace
                    )
                ),
                description=locale_primitives.DisplayText(
                    text=bin_.description.text,
                    format_type_id=type_primitives.Type(
                        authority=bin_.description.format_type.authority,
                        identifier=bin_.description.format_type.identifier,
                        namespace=bin_.description.format_type.namespace
                    ),
                    language_type_id=type_primitives.Type(
                        authority=bin_.description.language_type.authority,
                        identifier=bin_.description.language_type.identifier,
                        namespace=bin_.description.language_type.namespace
                    ),
                    script_type_id=type_primitives.Type(
                        authority=bin_.description.script_type.authority,
                        identifier=bin_.description.script_type.identifier,
                        namespace=bin_.description.script_type.namespace
                    )
                ),
                id=id_primitives.Id(
                    authority=bin_.ident.authority,
                    identifier=bin_.ident.identifier,
                    namespace=bin_.ident.namespace
                ),
                genusTypeId=type_primitives.Type(
                    authority=bin_.genus_type.authority,
                    identifier=bin_.genus_type.identifier,
                    namespace=bin_.genus_type.namespace
                ),
                recordTypeIds=[type_primitives.Type(
                    authority=record_type.authority,
                    identifier=record_type.identifier,
                    namespace=record_type.namespace
                ) for record_type in bin_.record_types]
            )
