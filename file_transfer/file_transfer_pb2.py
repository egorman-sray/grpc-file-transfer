# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_transfer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x66ile_transfer.proto\" \n\x0e\x46ileUploadData\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\"3\n\x0e\x46ileUploadInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0buploaded_by\x18\x02 \x01(\t\"^\n\x11\x46ileUploadRequest\x12\x1f\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0f.FileUploadDataH\x00\x12\x1f\n\x04info\x18\x02 \x01(\x0b\x32\x0f.FileUploadInfoH\x00\x42\x07\n\x05\x63hunk\"U\n\x12\x46ileUploadResponse\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.FileUploadStatus\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error*\x94\x01\n\x10\x46ileUploadStatus\x12\x17\n\x13\x46ILE_UPLOAD_UNKNOWN\x10\x00\x12\x17\n\x13\x46ILE_UPLOAD_SUCCESS\x10\x01\x12\x15\n\x11\x46ILE_UPLOAD_ERROR\x10\x02\x12\x1c\n\x18\x41\x43\x43OUNT_STATUS_SUSPENDED\x10\x03\x12\x19\n\x15\x41\x43\x43OUNT_STATUS_CLOSED\x10\x04\x32L\n\x13\x46ileTransferService\x12\x35\n\x06Upload\x12\x12.FileUploadRequest\x1a\x13.FileUploadResponse\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_transfer_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_FILEUPLOADSTATUS']._serialized_start=294
  _globals['_FILEUPLOADSTATUS']._serialized_end=442
  _globals['_FILEUPLOADDATA']._serialized_start=23
  _globals['_FILEUPLOADDATA']._serialized_end=55
  _globals['_FILEUPLOADINFO']._serialized_start=57
  _globals['_FILEUPLOADINFO']._serialized_end=108
  _globals['_FILEUPLOADREQUEST']._serialized_start=110
  _globals['_FILEUPLOADREQUEST']._serialized_end=204
  _globals['_FILEUPLOADRESPONSE']._serialized_start=206
  _globals['_FILEUPLOADRESPONSE']._serialized_end=291
  _globals['_FILETRANSFERSERVICE']._serialized_start=444
  _globals['_FILETRANSFERSERVICE']._serialized_end=520
# @@protoc_insertion_point(module_scope)
