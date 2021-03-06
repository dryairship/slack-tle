# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_server/api_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_server/api_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1dgrpc_server/api_service.proto\" \n\rRatingRequest\x12\x0f\n\x07handles\x18\x01 \x03(\t\"\x1b\n\x0bRatingReply\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t29\n\nAPIService\x12+\n\tGetRating\x12\x0e.RatingRequest\x1a\x0c.RatingReply\"\x00\x62\x06proto3'
)




_RATINGREQUEST = _descriptor.Descriptor(
  name='RatingRequest',
  full_name='RatingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='handles', full_name='RatingRequest.handles', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=65,
)


_RATINGREPLY = _descriptor.Descriptor(
  name='RatingReply',
  full_name='RatingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='RatingReply.file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['RatingRequest'] = _RATINGREQUEST
DESCRIPTOR.message_types_by_name['RatingReply'] = _RATINGREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RatingRequest = _reflection.GeneratedProtocolMessageType('RatingRequest', (_message.Message,), {
  'DESCRIPTOR' : _RATINGREQUEST,
  '__module__' : 'grpc_server.api_service_pb2'
  # @@protoc_insertion_point(class_scope:RatingRequest)
  })
_sym_db.RegisterMessage(RatingRequest)

RatingReply = _reflection.GeneratedProtocolMessageType('RatingReply', (_message.Message,), {
  'DESCRIPTOR' : _RATINGREPLY,
  '__module__' : 'grpc_server.api_service_pb2'
  # @@protoc_insertion_point(class_scope:RatingReply)
  })
_sym_db.RegisterMessage(RatingReply)



_APISERVICE = _descriptor.ServiceDescriptor(
  name='APIService',
  full_name='APIService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=96,
  serialized_end=153,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRating',
    full_name='APIService.GetRating',
    index=0,
    containing_service=None,
    input_type=_RATINGREQUEST,
    output_type=_RATINGREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_APISERVICE)

DESCRIPTOR.services_by_name['APIService'] = _APISERVICE

# @@protoc_insertion_point(module_scope)
