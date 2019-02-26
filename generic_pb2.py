# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='generic.proto',
  package='protobufpingpong',
  syntax='proto3',
  serialized_pb=_b('\n\rgeneric.proto\x12\x10protobufpingpong\"\xb5\x01\n\tProfessor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06office\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12@\n\x0b\x61ppointment\x18\x04 \x01(\x0e\x32+.protobufpingpong.Professor.AppointmentType\"9\n\x0f\x41ppointmentType\x12\r\n\tASSISTANT\x10\x00\x12\r\n\tASSOCIATE\x10\x01\x12\x08\n\x04\x46ULL\x10\x02\"=\n\nDepartment\x12/\n\nprofessors\x18\x01 \x03(\x0b\x32\x1b.protobufpingpong.Professor\"=\n\x07\x43ountry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x12\n\npopulation\x18\x03 \x01(\x05\"6\n\tContinent\x12)\n\x06states\x18\x01 \x03(\x0b\x32\x19.protobufpingpong.Country\"\xa6\x01\n\nConference\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0b\n\x03\x66\x65\x65\x18\x03 \x01(\x05\x12\x10\n\x08\x64\x65\x61\x64line\x18\x04 \x01(\t\x12\x31\n\x05track\x18\x05 \x01(\x0e\x32\".protobufpingpong.Conference.Track\"&\n\x05Track\x12\x0f\n\x0bSINGLETRACK\x10\x00\x12\x0c\n\x08TWOTRACK\x10\x01\"3\n\x03\x41\x43M\x12,\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1c.protobufpingpong.Conference\"\x97\x01\n\rSearchRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\x12<\n\tquerytype\x18\x02 \x01(\x0e\x32).protobufpingpong.SearchRequest.QueryType\"8\n\tQueryType\x12\x0e\n\nDEPARTMENT\x10\x00\x12\x0b\n\x07\x43OUNTRY\x10\x01\x12\x0e\n\nCONFERENCE\x10\x02\"\xae\x01\n\x0eSearchResponse\x12/\n\x07\x66\x61\x63ulty\x18\x05 \x01(\x0b\x32\x1c.protobufpingpong.DepartmentH\x00\x12\x30\n\tcountries\x18\x06 \x01(\x0b\x32\x1b.protobufpingpong.ContinentH\x00\x12,\n\x0b\x63onferences\x18\x07 \x01(\x0b\x32\x15.protobufpingpong.ACMH\x00\x42\x0b\n\tresponsesb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PROFESSOR_APPOINTMENTTYPE = _descriptor.EnumDescriptor(
  name='AppointmentType',
  full_name='protobufpingpong.Professor.AppointmentType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ASSISTANT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSOCIATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=160,
  serialized_end=217,
)
_sym_db.RegisterEnumDescriptor(_PROFESSOR_APPOINTMENTTYPE)

_CONFERENCE_TRACK = _descriptor.EnumDescriptor(
  name='Track',
  full_name='protobufpingpong.Conference.Track',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SINGLETRACK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWOTRACK', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=530,
  serialized_end=568,
)
_sym_db.RegisterEnumDescriptor(_CONFERENCE_TRACK)

_SEARCHREQUEST_QUERYTYPE = _descriptor.EnumDescriptor(
  name='QueryType',
  full_name='protobufpingpong.SearchRequest.QueryType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEPARTMENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNTRY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFERENCE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=719,
  serialized_end=775,
)
_sym_db.RegisterEnumDescriptor(_SEARCHREQUEST_QUERYTYPE)


_PROFESSOR = _descriptor.Descriptor(
  name='Professor',
  full_name='protobufpingpong.Professor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobufpingpong.Professor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='office', full_name='protobufpingpong.Professor.office', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='protobufpingpong.Professor.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appointment', full_name='protobufpingpong.Professor.appointment', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROFESSOR_APPOINTMENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=217,
)


_DEPARTMENT = _descriptor.Descriptor(
  name='Department',
  full_name='protobufpingpong.Department',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='professors', full_name='protobufpingpong.Department.professors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=280,
)


_COUNTRY = _descriptor.Descriptor(
  name='Country',
  full_name='protobufpingpong.Country',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobufpingpong.Country.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='protobufpingpong.Country.language', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='population', full_name='protobufpingpong.Country.population', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=343,
)


_CONTINENT = _descriptor.Descriptor(
  name='Continent',
  full_name='protobufpingpong.Continent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='states', full_name='protobufpingpong.Continent.states', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=399,
)


_CONFERENCE = _descriptor.Descriptor(
  name='Conference',
  full_name='protobufpingpong.Conference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='protobufpingpong.Conference.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='protobufpingpong.Conference.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fee', full_name='protobufpingpong.Conference.fee', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='protobufpingpong.Conference.deadline', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='track', full_name='protobufpingpong.Conference.track', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFERENCE_TRACK,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=568,
)


_ACM = _descriptor.Descriptor(
  name='ACM',
  full_name='protobufpingpong.ACM',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='protobufpingpong.ACM.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=570,
  serialized_end=621,
)


_SEARCHREQUEST = _descriptor.Descriptor(
  name='SearchRequest',
  full_name='protobufpingpong.SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='protobufpingpong.SearchRequest.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='querytype', full_name='protobufpingpong.SearchRequest.querytype', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SEARCHREQUEST_QUERYTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=624,
  serialized_end=775,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='protobufpingpong.SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faculty', full_name='protobufpingpong.SearchResponse.faculty', index=0,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='countries', full_name='protobufpingpong.SearchResponse.countries', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conferences', full_name='protobufpingpong.SearchResponse.conferences', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='responses', full_name='protobufpingpong.SearchResponse.responses',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=778,
  serialized_end=952,
)

_PROFESSOR.fields_by_name['appointment'].enum_type = _PROFESSOR_APPOINTMENTTYPE
_PROFESSOR_APPOINTMENTTYPE.containing_type = _PROFESSOR
_DEPARTMENT.fields_by_name['professors'].message_type = _PROFESSOR
_CONTINENT.fields_by_name['states'].message_type = _COUNTRY
_CONFERENCE.fields_by_name['track'].enum_type = _CONFERENCE_TRACK
_CONFERENCE_TRACK.containing_type = _CONFERENCE
_ACM.fields_by_name['events'].message_type = _CONFERENCE
_SEARCHREQUEST.fields_by_name['querytype'].enum_type = _SEARCHREQUEST_QUERYTYPE
_SEARCHREQUEST_QUERYTYPE.containing_type = _SEARCHREQUEST
_SEARCHRESPONSE.fields_by_name['faculty'].message_type = _DEPARTMENT
_SEARCHRESPONSE.fields_by_name['countries'].message_type = _CONTINENT
_SEARCHRESPONSE.fields_by_name['conferences'].message_type = _ACM
_SEARCHRESPONSE.oneofs_by_name['responses'].fields.append(
  _SEARCHRESPONSE.fields_by_name['faculty'])
_SEARCHRESPONSE.fields_by_name['faculty'].containing_oneof = _SEARCHRESPONSE.oneofs_by_name['responses']
_SEARCHRESPONSE.oneofs_by_name['responses'].fields.append(
  _SEARCHRESPONSE.fields_by_name['countries'])
_SEARCHRESPONSE.fields_by_name['countries'].containing_oneof = _SEARCHRESPONSE.oneofs_by_name['responses']
_SEARCHRESPONSE.oneofs_by_name['responses'].fields.append(
  _SEARCHRESPONSE.fields_by_name['conferences'])
_SEARCHRESPONSE.fields_by_name['conferences'].containing_oneof = _SEARCHRESPONSE.oneofs_by_name['responses']
DESCRIPTOR.message_types_by_name['Professor'] = _PROFESSOR
DESCRIPTOR.message_types_by_name['Department'] = _DEPARTMENT
DESCRIPTOR.message_types_by_name['Country'] = _COUNTRY
DESCRIPTOR.message_types_by_name['Continent'] = _CONTINENT
DESCRIPTOR.message_types_by_name['Conference'] = _CONFERENCE
DESCRIPTOR.message_types_by_name['ACM'] = _ACM
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE

Professor = _reflection.GeneratedProtocolMessageType('Professor', (_message.Message,), dict(
  DESCRIPTOR = _PROFESSOR,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.Professor)
  ))
_sym_db.RegisterMessage(Professor)

Department = _reflection.GeneratedProtocolMessageType('Department', (_message.Message,), dict(
  DESCRIPTOR = _DEPARTMENT,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.Department)
  ))
_sym_db.RegisterMessage(Department)

Country = _reflection.GeneratedProtocolMessageType('Country', (_message.Message,), dict(
  DESCRIPTOR = _COUNTRY,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.Country)
  ))
_sym_db.RegisterMessage(Country)

Continent = _reflection.GeneratedProtocolMessageType('Continent', (_message.Message,), dict(
  DESCRIPTOR = _CONTINENT,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.Continent)
  ))
_sym_db.RegisterMessage(Continent)

Conference = _reflection.GeneratedProtocolMessageType('Conference', (_message.Message,), dict(
  DESCRIPTOR = _CONFERENCE,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.Conference)
  ))
_sym_db.RegisterMessage(Conference)

ACM = _reflection.GeneratedProtocolMessageType('ACM', (_message.Message,), dict(
  DESCRIPTOR = _ACM,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.ACM)
  ))
_sym_db.RegisterMessage(ACM)

SearchRequest = _reflection.GeneratedProtocolMessageType('SearchRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQUEST,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.SearchRequest)
  ))
_sym_db.RegisterMessage(SearchRequest)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHRESPONSE,
  __module__ = 'generic_pb2'
  # @@protoc_insertion_point(class_scope:protobufpingpong.SearchResponse)
  ))
_sym_db.RegisterMessage(SearchResponse)


# @@protoc_insertion_point(module_scope)
