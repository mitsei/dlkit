from dlkit.json_.resource import sessions as json_resource_sessions
from dlkit.proto import resource_pb2
from dlkit.proto import resource_pb2_grpc


class BinLookupSessionServicer(resource_pb2_grpc.BinLookupSessionServicer,
                               json_resource_sessions.BinLookupSession):
    # def __init__(self):
    #     # Deal with runtime and initialization somehow?
    #     pass

    def GetBins(self, request, context):
        bins = self.get_bins()
        for bin_ in bins:
            import pdb
            pdb.set_trace()
            yield resource_pb2.Bin(displayName=bin_.display_name,
                                   description=bin_.description,
                                   id=bin_.ident,
                                   genusTypeId=bin_.genus_type,
                                   recordTypeIds=bin_.record_types)
