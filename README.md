# GRPC File Transfer

This is a demo for transferring files over grpc

__Features__

1. File upload implemented using [client streaming](https://grpc.io/docs/what-is-grpc/core-concepts/#client-streaming-rpc)
2. File chunking to configurable size (default: 1MB)
3. File information passed as part of stream, including:
    1. name of the file
    2. who uploaded the file
    3. file checksum
4. File checksum is compared by server to ensure file integrity

__Possible future features__

1. Asynchronous client response handler

## Installation

Create an environment:

```bash
python -m venv .env
source .env/bin/activate
```

Install packages:

```bash
python -m pip install -r requirements.txt
```

To generate protos:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file_transfer.proto
```

## Usage

Server side:

```bash
python server.py
```

Client side:

```bash
python client.py
```
