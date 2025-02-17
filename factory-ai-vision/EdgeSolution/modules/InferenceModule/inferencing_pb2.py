# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inferencing.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='inferencing.proto',
  package='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11inferencing.proto\x12@microsoft.azure.media.live_video_analytics.extensibility.grpc.v1\"\x84\x08\n\tInference\x12g\n\x04type\x18\x01 \x01(\x0e\x32Y.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.InferenceType\x12\x0f\n\x07subtype\x18\x02 \x01(\t\x12\x14\n\x0cinference_id\x18\x03 \x01(\t\x12\x1a\n\x12related_inferences\x18\x04 \x03(\t\x12j\n\x0e\x63lassification\x18\x05 \x01(\x0b\x32P.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.ClassificationH\x00\x12Z\n\x06motion\x18\x06 \x01(\x0b\x32H.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.MotionH\x00\x12Z\n\x06\x65ntity\x18\x07 \x01(\x0b\x32H.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.EntityH\x00\x12V\n\x04text\x18\x08 \x01(\x0b\x32\x46.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.TextH\x00\x12X\n\x05\x65vent\x18\t \x01(\x0b\x32G.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.EventH\x00\x12\x61\n\x05other\x18\r \x01(\x0b\x32P.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.InferenceOtherH\x00\x12o\n\nextensions\x18\x0f \x03(\x0b\x32[.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.ExtensionsEntry\x1a\x31\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"e\n\rInferenceType\x12\x08\n\x04\x41UTO\x10\x00\x12\x12\n\x0e\x43LASSIFICATION\x10\x01\x12\n\n\x06MOTION\x10\x02\x12\n\n\x06\x45NTITY\x10\x03\x12\x08\n\x04TEXT\x10\x04\x12\t\n\x05\x45VENT\x10\x05\x12\t\n\x05OTHER\x10\x0f\x42\x07\n\x05value\"\xc5\x01\n\x0e\x43lassification\x12R\n\x03tag\x18\x01 \x01(\x0b\x32\x45.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Tag\x12_\n\nattributes\x18\x02 \x03(\x0b\x32K.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Attribute\"b\n\x06Motion\x12X\n\x03\x62ox\x18\x01 \x01(\x0b\x32K.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle\"\x97\x02\n\x06\x45ntity\x12R\n\x03tag\x18\x01 \x01(\x0b\x32\x45.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Tag\x12_\n\nattributes\x18\x02 \x03(\x0b\x32K.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Attribute\x12X\n\x03\x62ox\x18\x03 \x01(\x0b\x32K.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle\"W\n\x04Text\x12\r\n\x05value\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x05 \x01(\x04\x12\x15\n\rend_timestamp\x18\x06 \x01(\x04\"\xb5\x01\n\x05\x45vent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12k\n\nproperties\x18\x07 \x03(\x0b\x32W.microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"=\n\x0eInferenceOther\x12\x14\n\x0c\x63ontent_type\x18\x01 \x01(\t\x12\x15\n\rcontent_bytes\x18\x02 \x01(\x0c\"<\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02\"(\n\x03Tag\x12\r\n\x05value\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02\"7\n\tRectangle\x12\t\n\x01l\x18\x01 \x01(\x02\x12\t\n\x01t\x18\x02 \x01(\x02\x12\t\n\x01w\x18\x03 \x01(\x02\x12\t\n\x01h\x18\x04 \x01(\x02\x62\x06proto3'
)



_INFERENCE_INFERENCETYPE = _descriptor.EnumDescriptor(
  name='InferenceType',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.InferenceType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLASSIFICATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENTITY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVENT', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=6, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1006,
  serialized_end=1107,
)
_sym_db.RegisterEnumDescriptor(_INFERENCE_INFERENCETYPE)


_INFERENCE_EXTENSIONSENTRY = _descriptor.Descriptor(
  name='ExtensionsEntry',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.ExtensionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.ExtensionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.ExtensionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=955,
  serialized_end=1004,
)

_INFERENCE = _descriptor.Descriptor(
  name='Inference',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subtype', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.subtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inference_id', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.inference_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='related_inferences', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.related_inferences', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classification', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.classification', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='motion', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.motion', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entity', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.entity', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.text', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.event', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='other', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.other', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extensions', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.extensions', index=10,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_INFERENCE_EXTENSIONSENTRY, ],
  enum_types=[
    _INFERENCE_INFERENCETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=88,
  serialized_end=1116,
)


_CLASSIFICATION = _descriptor.Descriptor(
  name='Classification',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Classification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Classification.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Classification.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1119,
  serialized_end=1316,
)


_MOTION = _descriptor.Descriptor(
  name='Motion',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Motion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='box', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Motion.box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1318,
  serialized_end=1416,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Entity.tag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Entity.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='box', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Entity.box', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1419,
  serialized_end=1698,
)


_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Text.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Text.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_timestamp', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Text.start_timestamp', index=2,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Text.end_timestamp', index=3,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1700,
  serialized_end=1787,
)


_EVENT_PROPERTIESENTRY = _descriptor.Descriptor(
  name='PropertiesEntry',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event.PropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event.PropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event.PropertiesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1922,
  serialized_end=1971,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='properties', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event.properties', index=1,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_PROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1790,
  serialized_end=1971,
)


_INFERENCEOTHER = _descriptor.Descriptor(
  name='InferenceOther',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.InferenceOther',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.InferenceOther.content_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_bytes', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.InferenceOther.content_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1973,
  serialized_end=2034,
)


_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Attribute.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Attribute.confidence', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2036,
  serialized_end=2096,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Tag.value', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Tag.confidence', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2098,
  serialized_end=2138,
)


_RECTANGLE = _descriptor.Descriptor(
  name='Rectangle',
  full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='l', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle.l', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='t', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle.t', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='w', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle.w', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='h', full_name='microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle.h', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2140,
  serialized_end=2195,
)

_INFERENCE_EXTENSIONSENTRY.containing_type = _INFERENCE
_INFERENCE.fields_by_name['type'].enum_type = _INFERENCE_INFERENCETYPE
_INFERENCE.fields_by_name['classification'].message_type = _CLASSIFICATION
_INFERENCE.fields_by_name['motion'].message_type = _MOTION
_INFERENCE.fields_by_name['entity'].message_type = _ENTITY
_INFERENCE.fields_by_name['text'].message_type = _TEXT
_INFERENCE.fields_by_name['event'].message_type = _EVENT
_INFERENCE.fields_by_name['other'].message_type = _INFERENCEOTHER
_INFERENCE.fields_by_name['extensions'].message_type = _INFERENCE_EXTENSIONSENTRY
_INFERENCE_INFERENCETYPE.containing_type = _INFERENCE
_INFERENCE.oneofs_by_name['value'].fields.append(
  _INFERENCE.fields_by_name['classification'])
_INFERENCE.fields_by_name['classification'].containing_oneof = _INFERENCE.oneofs_by_name['value']
_INFERENCE.oneofs_by_name['value'].fields.append(
  _INFERENCE.fields_by_name['motion'])
_INFERENCE.fields_by_name['motion'].containing_oneof = _INFERENCE.oneofs_by_name['value']
_INFERENCE.oneofs_by_name['value'].fields.append(
  _INFERENCE.fields_by_name['entity'])
_INFERENCE.fields_by_name['entity'].containing_oneof = _INFERENCE.oneofs_by_name['value']
_INFERENCE.oneofs_by_name['value'].fields.append(
  _INFERENCE.fields_by_name['text'])
_INFERENCE.fields_by_name['text'].containing_oneof = _INFERENCE.oneofs_by_name['value']
_INFERENCE.oneofs_by_name['value'].fields.append(
  _INFERENCE.fields_by_name['event'])
_INFERENCE.fields_by_name['event'].containing_oneof = _INFERENCE.oneofs_by_name['value']
_INFERENCE.oneofs_by_name['value'].fields.append(
  _INFERENCE.fields_by_name['other'])
_INFERENCE.fields_by_name['other'].containing_oneof = _INFERENCE.oneofs_by_name['value']
_CLASSIFICATION.fields_by_name['tag'].message_type = _TAG
_CLASSIFICATION.fields_by_name['attributes'].message_type = _ATTRIBUTE
_MOTION.fields_by_name['box'].message_type = _RECTANGLE
_ENTITY.fields_by_name['tag'].message_type = _TAG
_ENTITY.fields_by_name['attributes'].message_type = _ATTRIBUTE
_ENTITY.fields_by_name['box'].message_type = _RECTANGLE
_EVENT_PROPERTIESENTRY.containing_type = _EVENT
_EVENT.fields_by_name['properties'].message_type = _EVENT_PROPERTIESENTRY
DESCRIPTOR.message_types_by_name['Inference'] = _INFERENCE
DESCRIPTOR.message_types_by_name['Classification'] = _CLASSIFICATION
DESCRIPTOR.message_types_by_name['Motion'] = _MOTION
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Text'] = _TEXT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['InferenceOther'] = _INFERENCEOTHER
DESCRIPTOR.message_types_by_name['Attribute'] = _ATTRIBUTE
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['Rectangle'] = _RECTANGLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Inference = _reflection.GeneratedProtocolMessageType('Inference', (_message.Message,), {

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _INFERENCE_EXTENSIONSENTRY,
    '__module__' : 'inferencing_pb2'
    # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _INFERENCE,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Inference)
  })
_sym_db.RegisterMessage(Inference)
_sym_db.RegisterMessage(Inference.ExtensionsEntry)

Classification = _reflection.GeneratedProtocolMessageType('Classification', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFICATION,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Classification)
  })
_sym_db.RegisterMessage(Classification)

Motion = _reflection.GeneratedProtocolMessageType('Motion', (_message.Message,), {
  'DESCRIPTOR' : _MOTION,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Motion)
  })
_sym_db.RegisterMessage(Motion)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Entity)
  })
_sym_db.RegisterMessage(Entity)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), {
  'DESCRIPTOR' : _TEXT,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Text)
  })
_sym_db.RegisterMessage(Text)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'PropertiesEntry' : _reflection.GeneratedProtocolMessageType('PropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_PROPERTIESENTRY,
    '__module__' : 'inferencing_pb2'
    # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event.PropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.PropertiesEntry)

InferenceOther = _reflection.GeneratedProtocolMessageType('InferenceOther', (_message.Message,), {
  'DESCRIPTOR' : _INFERENCEOTHER,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.InferenceOther)
  })
_sym_db.RegisterMessage(InferenceOther)

Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
  'DESCRIPTOR' : _ATTRIBUTE,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Attribute)
  })
_sym_db.RegisterMessage(Attribute)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), {
  'DESCRIPTOR' : _TAG,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Tag)
  })
_sym_db.RegisterMessage(Tag)

Rectangle = _reflection.GeneratedProtocolMessageType('Rectangle', (_message.Message,), {
  'DESCRIPTOR' : _RECTANGLE,
  '__module__' : 'inferencing_pb2'
  # @@protoc_insertion_point(class_scope:microsoft.azure.media.live_video_analytics.extensibility.grpc.v1.Rectangle)
  })
_sym_db.RegisterMessage(Rectangle)


_INFERENCE_EXTENSIONSENTRY._options = None
_EVENT_PROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
