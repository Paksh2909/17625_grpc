# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nbook.proto\x12\x0b\x61ssignment3\"\xf4\x01\n\x04\x42ook\x12\x0c\n\x04isbn\x18\x01 \x02(\t\x12\r\n\x05title\x18\x02 \x02(\t\x12\x0c\n\x04year\x18\x04 \x02(\x05\x12\x32\n\x05genre\x18\x03 \x02(\x0e\x32\x17.assignment3.Book.Genre:\nNONFICTION\x12(\n\x06\x61uthor\x18\x05 \x02(\x0b\x32\x18.assignment3.Book.Author\x1a\x16\n\x06\x41uthor\x12\x0c\n\x04name\x18\x06 \x02(\t\"K\n\x05Genre\x12\x0b\n\x07\x46ICTION\x10\x00\x12\x0b\n\x07\x46\x41NTASY\x10\x01\x12\x0b\n\x07ROMANCE\x10\x02\x12\x0b\n\x07MYSTERY\x10\x03\x12\x0e\n\nNONFICTION\x10\x04')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'book_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOK._serialized_start=28
  _BOOK._serialized_end=272
  _BOOK_AUTHOR._serialized_start=173
  _BOOK_AUTHOR._serialized_end=195
  _BOOK_GENRE._serialized_start=197
  _BOOK_GENRE._serialized_end=272
# @@protoc_insertion_point(module_scope)
