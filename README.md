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
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file_transfer.proto
```

Server side:

```bash
python server.py
```

Client side:

```bash
python client.py
```
