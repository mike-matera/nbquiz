# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: nbquiz/runtime/checker.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'nbquiz/runtime/checker.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cnbquiz/runtime/checker.proto\x12\x07\x63hecker\"\x1d\n\x0bTestRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\"=\n\tTestReply\x12\x10\n\x08response\x18\x01 \x01(\t\x12\x13\n\x06status\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\t\n\x07_status2B\n\x07\x43hecker\x12\x37\n\trun_tests\x12\x14.checker.TestRequest\x1a\x12.checker.TestReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nbquiz.runtime.checker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TESTREQUEST']._serialized_start=41
  _globals['_TESTREQUEST']._serialized_end=70
  _globals['_TESTREPLY']._serialized_start=72
  _globals['_TESTREPLY']._serialized_end=133
  _globals['_CHECKER']._serialized_start=135
  _globals['_CHECKER']._serialized_end=201
# @@protoc_insertion_point(module_scope)
