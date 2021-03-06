# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from collections import deque
from concurrent import futures
from random import seed
from random import randint
import logging
import time
import grpc

import streamPOC_pb2
import streamPOC_pb2_grpc


class Greeter(streamPOC_pb2_grpc.StreamPOCserviceServicer):

    def __init__(self):
        # seed random number generator
        seed(1)

    def requestData(self, request, context):
        x = 0
        while request.name == 'true':
            time.sleep(.2)
            y = randint(1, 10)
            if x < 1000:
                x = x + 1
            if x == 1000:
                x = 0
            yield streamPOC_pb2.numberReply(x=x, y=y)

    def serve():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        streamPOC_pb2_grpc.add_StreamPOCserviceServicer_to_server(Greeter(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    greeter = Greeter
    server = greeter.serve()

