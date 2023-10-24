import hashlib

import grpc
from concurrent import futures
import logging as log

# import the generated classes
import file_transfer_pb2
import file_transfer_pb2_grpc
MAX_MESSAGE_LENGTH = 500 * 1024 * 1024

# create a class to define the server functions, derived from
# hello_pb2_grpc.HelloServicer
class HelloWorld(file_transfer_pb2_grpc.HelloServicer):
    # method that takes the request and returns the response
    def hello(self, request, context):
        # print("Got request " + str(request))
        return file_transfer_pb2.HelloResponse(message=hashlib.md5(request.file_data.encode('utf-8')).hexdigest())


# create the grpc server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ])
# add the defined class to the server
file_transfer_pb2_grpc.add_HelloServicer_to_server(
        HelloWorld(), server)

# expose and start the server
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
