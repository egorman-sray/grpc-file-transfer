import hashlib

import grpc

import file_transfer_pb2
import file_transfer_pb2_grpc
MAX_MESSAGE_LENGTH = 500 * 1024 * 1024
def run():
   file = open("too_big.json", encoding='utf-8')
   data = file.read()
   with grpc.insecure_channel('localhost:50051', options=[
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH),
    ]) as channel:
      stub = file_transfer_pb2_grpc.HelloStub(channel)
      print(hashlib.md5(data.encode('utf-8')).hexdigest())
      response = stub.hello(file_transfer_pb2.HelloRequest(file_name='John', file_data=data))
   print(response.message)
run()
