import os
import tempfile
from typing import List

import grpc

import file_transfer_pb2_grpc as pb2_grpc
import file_transfer_pb2 as pb2


class FileTransferClient:
    CHUNK_SIZE = 1024 * 1024

    def __init__(self, file_directory: str, service_stub: pb2_grpc.FileTransferServiceStub) -> None:
        self.__file_directory = file_directory
        self.__service_stub = service_stub

    def upload(self, file_name: str, uploaded_by: str) -> None:
        try:
            # Generate chunks for file
            file_chunks = self.__generate_file_chunks(file_name, uploaded_by)

        except Exception as ee:
            print(f"Error while generating file chunks: {ee}")
            return

        try:
            # Send file upload request to server
            print(f"Uploading file '{file_name}'...")
            response = self.__service_stub.Upload(file_chunks)

        except grpc.RpcError as re:
            print(f"Error while making request: {re}")
            return

        print(
            f"Successfully uploaded file with name '{file_name}' as user '{uploaded_by}', response: '{response}'"
        )

    def __generate_file_chunks(
        self,
        file_name: str,
        uploaded_by: str
    ) -> List[pb2.FileUploadRequest]:
        # Add info chunk to generator
        yield pb2.FileUploadRequest(
            info=pb2.FileUploadInfo(name=file_name, uploaded_by=uploaded_by)
        )

        # Add chunks of file in byte format
        file_path = os.path.join(self.__file_directory, file_name)

        with open(file_path, "rb") as file:
            while True:
                file_chunk = file.read(self.CHUNK_SIZE)
                if len(file_chunk) == 0:
                    return

                yield pb2.FileUploadRequest(data=pb2.FileUploadData(buffer=file_chunk))


if __name__ == "__main__":
    # Create a temporary named file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Write a message to the temp_file
        temp_file.write(b"Ed is great" * int(2e6))
        file_name = os.path.basename(temp_file.name)
        file_directory = os.path.dirname(temp_file.name)

        # Create grpc client connection at localhost:50051
        channel = grpc.insecure_channel("[::]:50051")
        service_stub = pb2_grpc.FileTransferServiceStub(channel)
        client = FileTransferClient(
            file_directory=file_directory, service_stub=service_stub
        )

        # Upload file
        client.upload(file_name=file_name, uploaded_by="me")
