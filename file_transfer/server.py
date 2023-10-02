from concurrent import futures
import os
import tempfile

import grpc

import file_transfer_pb2_grpc as pb2_grpc
import file_transfer_pb2 as pb2


class FileTransferService(pb2_grpc.FileTransferService):

    def __init__(self, save_directory):
        self.__save_directory = save_directory

    def Upload(self, request_iterator, context):
        # Extract metadata from request
        metadata = dict(context.invocation_metadata())
        print(f"Recieved upload request for file '{metadata['file_name']}', metadata: {metadata}")

        try:
            # Save chunks to file path
            file_path = os.path.join(self.__save_directory, metadata["file_name"])
            self.__save_chunks_to_file(chunks=request_iterator, file_path=file_path)
        
        except Exception as ee:
            # Return an error response
            print(f"Failed to upload file to '{file_path}': {ee}")
            return pb2.FileUploadResponse(
                status=pb2.FILE_UPLOAD_ERROR, error=f"Failed to upload file: {ee}"
            )

        # Return a success response
        print(f"Successfully uploaded file to '{file_path}'")
        return pb2.FileUploadResponse(status=pb2.FILE_UPLOAD_SUCCESS, error=None)

    def __save_chunks_to_file(self, chunks, file_path):
        # Write all chunks to a new file at file_path
        with open(file_path, "wb") as file:
            for chunk in chunks:
                file.write(chunk.buffer)

if __name__ == "__main__":
    
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_directory:

        # Set the temporary directory as save directory for service
        service = FileTransferService(save_directory=temp_directory)

        # Create grpc server at localhost:50051
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_FileTransferServiceServicer_to_server(service, server)
        server.add_insecure_port('[::]:50051')

        # Run grpc server until terminated
        server.start()
        server.wait_for_termination()
