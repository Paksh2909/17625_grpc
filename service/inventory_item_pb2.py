# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory_item.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import book_pb2 as book__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14inventory_item.proto\x12\x0b\x61ssignment3\x1a\nbook.proto\"\xa8\x01\n\rInventoryItem\x12\x0e\n\x06number\x18\x01 \x02(\x05\x12!\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x11.assignment3.BookH\x00\x12\x31\n\x06status\x18\x03 \x02(\x0e\x32!.assignment3.InventoryItem.Status\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x04\x12\t\n\x05TAKEN\x10\x05\x42\r\n\x0b\x62ook_object')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inventory_item_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INVENTORYITEM._serialized_start=50
  _INVENTORYITEM._serialized_end=218
  _INVENTORYITEM_STATUS._serialized_start=169
  _INVENTORYITEM_STATUS._serialized_end=203
# @@protoc_insertion_point(module_scope)