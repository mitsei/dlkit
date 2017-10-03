import grpc

from dlkit.proto import resource_pb2
from dlkit.proto import resource_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = resource_pb2_grpc.BinLookupSessionStub(channel)
    for bin_ in stub.GetBins(resource_pb2.GetBinsRequest()):
        print(bin_)


if __name__ == '__main__':
    run()
