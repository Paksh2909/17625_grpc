# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import book_pb2 as book__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17inventory_service.proto\x12\x0b\x61ssignment3\x1a\nbook.proto\"4\n\x11\x43reateBookRequest\x12\x1f\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x11.assignment3.Book\"0\n\x0f\x43reateBookReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"N\n\x0cGetBookReply\x12\x1f\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x11.assignment3.Book\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t2\x9e\x01\n\tInventory\x12L\n\nCreateBook\x12\x1e.assignment3.CreateBookRequest\x1a\x1c.assignment3.CreateBookReply\"\x00\x12\x43\n\x07GetBook\x12\x1b.assignment3.GetBookRequest\x1a\x19.assignment3.GetBookReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEBOOKREQUEST._serialized_start=52
  _CREATEBOOKREQUEST._serialized_end=104
  _CREATEBOOKREPLY._serialized_start=106
  _CREATEBOOKREPLY._serialized_end=154
  _GETBOOKREQUEST._serialized_start=156
  _GETBOOKREQUEST._serialized_end=186
  _GETBOOKREPLY._serialized_start=188
  _GETBOOKREPLY._serialized_end=266
  _INVENTORY._serialized_start=269
  _INVENTORY._serialized_end=427
# @@protoc_insertion_point(module_scope)
