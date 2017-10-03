# Python 3.2+ only
from concurrent import futures

import time

import grpc

from dlkit.proto import resource_pb2_grpc
from dlkit.grpc_adapter.resource import BinLookupSessionServicer

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    resource_pb2_grpc.add_BinLookupSessionServicer_to_server(
        BinLookupSessionServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
