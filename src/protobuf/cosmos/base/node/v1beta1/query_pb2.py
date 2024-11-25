"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cosmos/base/node/v1beta1/query.proto\x12\x18cosmos.base.node.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto"\x0f\n\rConfigRequest"w\n\x0eConfigResponse\x12\x19\n\x11minimum_gas_price\x18\x01 \x01(\t\x12\x1b\n\x13pruning_keep_recent\x18\x02 \x01(\t\x12\x18\n\x10pruning_interval\x18\x03 \x01(\t\x12\x13\n\x0bhalt_height\x18\x04 \x01(\x04"\x0f\n\rStatusRequest"\x9e\x01\n\x0eStatusResponse\x12\x1d\n\x15earliest_store_height\x18\x01 \x01(\x04\x12\x0e\n\x06height\x18\x02 \x01(\x04\x123\n\ttimestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x04\x90\xdf\x1f\x01\x12\x10\n\x08app_hash\x18\x04 \x01(\x0c\x12\x16\n\x0evalidator_hash\x18\x05 \x01(\x0c2\x99\x02\n\x07Service\x12\x85\x01\n\x06Config\x12\'.cosmos.base.node.v1beta1.ConfigRequest\x1a(.cosmos.base.node.v1beta1.ConfigResponse"(\x82\xd3\xe4\x93\x02"\x12 /cosmos/base/node/v1beta1/config\x12\x85\x01\n\x06Status\x12\'.cosmos.base.node.v1beta1.StatusRequest\x1a(.cosmos.base.node.v1beta1.StatusResponse"(\x82\xd3\xe4\x93\x02"\x12 /cosmos/base/node/v1beta1/statusB/Z-github.com/cosmos/cosmos-sdk/client/grpc/nodeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.node.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/client/grpc/node'
    _globals['_STATUSRESPONSE'].fields_by_name['timestamp']._options = None
    _globals['_STATUSRESPONSE'].fields_by_name['timestamp']._serialized_options = b'\x90\xdf\x1f\x01'
    _globals['_SERVICE'].methods_by_name['Config']._options = None
    _globals['_SERVICE'].methods_by_name['Config']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /cosmos/base/node/v1beta1/config'
    _globals['_SERVICE'].methods_by_name['Status']._options = None
    _globals['_SERVICE'].methods_by_name['Status']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /cosmos/base/node/v1beta1/status'
    _globals['_CONFIGREQUEST']._serialized_start = 151
    _globals['_CONFIGREQUEST']._serialized_end = 166
    _globals['_CONFIGRESPONSE']._serialized_start = 168
    _globals['_CONFIGRESPONSE']._serialized_end = 287
    _globals['_STATUSREQUEST']._serialized_start = 289
    _globals['_STATUSREQUEST']._serialized_end = 304
    _globals['_STATUSRESPONSE']._serialized_start = 307
    _globals['_STATUSRESPONSE']._serialized_end = 465
    _globals['_SERVICE']._serialized_start = 468
    _globals['_SERVICE']._serialized_end = 749