import os
import tempfile

import grpc

import file_transfer_pb2_grpc as pb2_grpc
import file_transfer_pb2 as pb2


class FileTransferClient:

    CHUNK_SIZE = 1024 * 1024

    def __init__(self, file_directory, service_stub):
        self.__file_directory = file_directory
        self.__service_stub = service_stub

    def upload(self, file_name):
        try:
            # Generate chunks for file
            file_path = os.path.join(self.__file_directory, file_name)
            file_chunks = self.__generate_file_chunks(file_path)
        
        except Exception as ee:
            print(f"Error while generating file chunks: {ee}")
            return

        try:
            # Create metadata for request
            # Note: not a fan of metadata having no required structure
            metadata = (
                ("file_name", file_name),
            )

            # Send file upload request to server
            print(f"Uploading file '{file_name}'...")
            response = self.__service_stub.Upload(
                file_chunks, metadata=metadata
            )
        
        except grpc.RpcError as re:
            print(f"Error while making request: {re}")
            return
        
        print(f"Successfully uploaded file '{file_name}', response: {response}")
    
    def __generate_file_chunks(self, file_path):
        # Return chunks of file as a generator
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(self.CHUNK_SIZE)
                if len(chunk) == 0:
                    return
                yield pb2.FileUploadChunk(buffer=chunk)


if __name__ == '__main__':

    # Create a temporary named file
    with tempfile.NamedTemporaryFile() as temp_file:
        
        # Write a message to the temp_file
        temp_file.write(b"Ed is great" * int(2e6))
        file_name = os.path.basename(temp_file.name)
        file_directory = os.path.dirname(temp_file.name)

        # Create grpc client connection at localhost:50051
        channel = grpc.insecure_channel("[::]:50051")
        service_stub = pb2_grpc.FileTransferServiceStub(channel)
        client = FileTransferClient(file_directory=file_directory, service_stub=service_stub)
    
        # Upload file
        client.upload(file_name=file_name)
