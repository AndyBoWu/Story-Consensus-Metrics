"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtendermint/types/params.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto"\x87\x02\n\x0fConsensusParams\x12,\n\x05block\x18\x01 \x01(\x0b2\x1d.tendermint.types.BlockParams\x122\n\x08evidence\x18\x02 \x01(\x0b2 .tendermint.types.EvidenceParams\x124\n\tvalidator\x18\x03 \x01(\x0b2!.tendermint.types.ValidatorParams\x120\n\x07version\x18\x04 \x01(\x0b2\x1f.tendermint.types.VersionParams\x12*\n\x04abci\x18\x05 \x01(\x0b2\x1c.tendermint.types.ABCIParams"7\n\x0bBlockParams\x12\x11\n\tmax_bytes\x18\x01 \x01(\x03\x12\x0f\n\x07max_gas\x18\x02 \x01(\x03J\x04\x08\x03\x10\x04"~\n\x0eEvidenceParams\x12\x1a\n\x12max_age_num_blocks\x18\x01 \x01(\x03\x12=\n\x10max_age_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x11\n\tmax_bytes\x18\x03 \x01(\x03"2\n\x0fValidatorParams\x12\x15\n\rpub_key_types\x18\x01 \x03(\t:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01"&\n\rVersionParams\x12\x0b\n\x03app\x18\x01 \x01(\x04:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01">\n\x0cHashedParams\x12\x17\n\x0fblock_max_bytes\x18\x01 \x01(\x03\x12\x15\n\rblock_max_gas\x18\x02 \x01(\x03"3\n\nABCIParams\x12%\n\x1dvote_extensions_enable_height\x18\x01 \x01(\x03B9Z3github.com/cometbft/cometbft/proto/tendermint/types\xa8\xe2\x1e\x01b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.types.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/cometbft/cometbft/proto/tendermint/types\xa8\xe2\x1e\x01'
    _globals['_EVIDENCEPARAMS'].fields_by_name['max_age_duration']._options = None
    _globals['_EVIDENCEPARAMS'].fields_by_name['max_age_duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_VALIDATORPARAMS']._options = None
    _globals['_VALIDATORPARAMS']._serialized_options = b'\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01'
    _globals['_VERSIONPARAMS']._options = None
    _globals['_VERSIONPARAMS']._serialized_options = b'\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01'
    _globals['_CONSENSUSPARAMS']._serialized_start = 106
    _globals['_CONSENSUSPARAMS']._serialized_end = 369
    _globals['_BLOCKPARAMS']._serialized_start = 371
    _globals['_BLOCKPARAMS']._serialized_end = 426
    _globals['_EVIDENCEPARAMS']._serialized_start = 428
    _globals['_EVIDENCEPARAMS']._serialized_end = 554
    _globals['_VALIDATORPARAMS']._serialized_start = 556
    _globals['_VALIDATORPARAMS']._serialized_end = 606
    _globals['_VERSIONPARAMS']._serialized_start = 608
    _globals['_VERSIONPARAMS']._serialized_end = 646
    _globals['_HASHEDPARAMS']._serialized_start = 648
    _globals['_HASHEDPARAMS']._serialized_end = 710
    _globals['_ABCIPARAMS']._serialized_start = 712
    _globals['_ABCIPARAMS']._serialized_end = 763