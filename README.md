# GRPC File Transfer

This is a demo for transferring files over grpc

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

## Usage

To generate protos:

```bash
cd file_transfer
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file_transfer.proto
```

Server side:

```bash
python file_transfer/server.py
```

Client side:

```bash
python file_transfer/client.py
```
