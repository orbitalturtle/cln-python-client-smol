import primitives_pb2 as _primitives_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddgossipRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: bytes
    def __init__(self, message: _Optional[bytes] = ...) -> None: ...

class AddgossipResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AutocleaninvoiceRequest(_message.Message):
    __slots__ = ["cycle_seconds", "expired_by"]
    CYCLE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_BY_FIELD_NUMBER: _ClassVar[int]
    cycle_seconds: int
    expired_by: int
    def __init__(self, expired_by: _Optional[int] = ..., cycle_seconds: _Optional[int] = ...) -> None: ...

class AutocleaninvoiceResponse(_message.Message):
    __slots__ = ["cycle_seconds", "enabled", "expired_by"]
    CYCLE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_BY_FIELD_NUMBER: _ClassVar[int]
    cycle_seconds: int
    enabled: bool
    expired_by: int
    def __init__(self, enabled: bool = ..., expired_by: _Optional[int] = ..., cycle_seconds: _Optional[int] = ...) -> None: ...

class CheckmessageRequest(_message.Message):
    __slots__ = ["message", "pubkey", "zbase"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    ZBASE_FIELD_NUMBER: _ClassVar[int]
    message: str
    pubkey: bytes
    zbase: str
    def __init__(self, message: _Optional[str] = ..., zbase: _Optional[str] = ..., pubkey: _Optional[bytes] = ...) -> None: ...

class CheckmessageResponse(_message.Message):
    __slots__ = ["pubkey", "verified"]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    VERIFIED_FIELD_NUMBER: _ClassVar[int]
    pubkey: bytes
    verified: bool
    def __init__(self, verified: bool = ..., pubkey: _Optional[bytes] = ...) -> None: ...

class CloseRequest(_message.Message):
    __slots__ = ["destination", "fee_negotiation_step", "feerange", "force_lease_closed", "id", "unilateraltimeout", "wrong_funding"]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FEERANGE_FIELD_NUMBER: _ClassVar[int]
    FEE_NEGOTIATION_STEP_FIELD_NUMBER: _ClassVar[int]
    FORCE_LEASE_CLOSED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    UNILATERALTIMEOUT_FIELD_NUMBER: _ClassVar[int]
    WRONG_FUNDING_FIELD_NUMBER: _ClassVar[int]
    destination: str
    fee_negotiation_step: str
    feerange: _containers.RepeatedCompositeFieldContainer[_primitives_pb2.Feerate]
    force_lease_closed: bool
    id: str
    unilateraltimeout: int
    wrong_funding: _primitives_pb2.Outpoint
    def __init__(self, id: _Optional[str] = ..., unilateraltimeout: _Optional[int] = ..., destination: _Optional[str] = ..., fee_negotiation_step: _Optional[str] = ..., wrong_funding: _Optional[_Union[_primitives_pb2.Outpoint, _Mapping]] = ..., force_lease_closed: bool = ..., feerange: _Optional[_Iterable[_Union[_primitives_pb2.Feerate, _Mapping]]] = ...) -> None: ...

class CloseResponse(_message.Message):
    __slots__ = ["item_type", "tx", "txid"]
    class CloseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    MUTUAL: CloseResponse.CloseType
    TXID_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    UNILATERAL: CloseResponse.CloseType
    UNOPENED: CloseResponse.CloseType
    item_type: CloseResponse.CloseType
    tx: bytes
    txid: bytes
    def __init__(self, item_type: _Optional[_Union[CloseResponse.CloseType, str]] = ..., tx: _Optional[bytes] = ..., txid: _Optional[bytes] = ...) -> None: ...

class ConnectAddress(_message.Message):
    __slots__ = ["address", "item_type", "port", "socket"]
    class ConnectAddressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IPV4: ConnectAddress.ConnectAddressType
    IPV6: ConnectAddress.ConnectAddressType
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SOCKET: ConnectAddress.ConnectAddressType
    PORT_FIELD_NUMBER: _ClassVar[int]
    SOCKET_FIELD_NUMBER: _ClassVar[int]
    TORV2: ConnectAddress.ConnectAddressType
    TORV3: ConnectAddress.ConnectAddressType
    address: str
    item_type: ConnectAddress.ConnectAddressType
    port: int
    socket: str
    def __init__(self, item_type: _Optional[_Union[ConnectAddress.ConnectAddressType, str]] = ..., socket: _Optional[str] = ..., address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ConnectRequest(_message.Message):
    __slots__ = ["host", "id", "port"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    host: str
    id: str
    port: int
    def __init__(self, id: _Optional[str] = ..., host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class ConnectResponse(_message.Message):
    __slots__ = ["direction", "features", "id"]
    class ConnectDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IN: ConnectResponse.ConnectDirection
    OUT: ConnectResponse.ConnectDirection
    direction: ConnectResponse.ConnectDirection
    features: bytes
    id: bytes
    def __init__(self, id: _Optional[bytes] = ..., features: _Optional[bytes] = ..., direction: _Optional[_Union[ConnectResponse.ConnectDirection, str]] = ...) -> None: ...

class CreateinvoiceRequest(_message.Message):
    __slots__ = ["invstring", "label", "preimage"]
    INVSTRING_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    invstring: str
    label: str
    preimage: bytes
    def __init__(self, invstring: _Optional[str] = ..., label: _Optional[str] = ..., preimage: _Optional[bytes] = ...) -> None: ...

class CreateinvoiceResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_received_msat", "bolt11", "bolt12", "description", "expires_at", "invreq_payer_note", "label", "local_offer_id", "paid_at", "pay_index", "payment_hash", "payment_preimage", "status"]
    class CreateinvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_RECEIVED_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED: CreateinvoiceResponse.CreateinvoiceStatus
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    INVREQ_PAYER_NOTE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    PAID: CreateinvoiceResponse.CreateinvoiceStatus
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PAY_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNPAID: CreateinvoiceResponse.CreateinvoiceStatus
    amount_msat: _primitives_pb2.Amount
    amount_received_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    description: str
    expires_at: int
    invreq_payer_note: str
    label: str
    local_offer_id: bytes
    paid_at: int
    pay_index: int
    payment_hash: bytes
    payment_preimage: bytes
    status: CreateinvoiceResponse.CreateinvoiceStatus
    def __init__(self, label: _Optional[str] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., status: _Optional[_Union[CreateinvoiceResponse.CreateinvoiceStatus, str]] = ..., description: _Optional[str] = ..., expires_at: _Optional[int] = ..., pay_index: _Optional[int] = ..., amount_received_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., paid_at: _Optional[int] = ..., payment_preimage: _Optional[bytes] = ..., local_offer_id: _Optional[bytes] = ..., invreq_payer_note: _Optional[str] = ...) -> None: ...

class CreateonionHops(_message.Message):
    __slots__ = ["payload", "pubkey"]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    pubkey: bytes
    def __init__(self, pubkey: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...

class CreateonionRequest(_message.Message):
    __slots__ = ["assocdata", "hops", "onion_size", "session_key"]
    ASSOCDATA_FIELD_NUMBER: _ClassVar[int]
    HOPS_FIELD_NUMBER: _ClassVar[int]
    ONION_SIZE_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    assocdata: bytes
    hops: _containers.RepeatedCompositeFieldContainer[CreateonionHops]
    onion_size: int
    session_key: bytes
    def __init__(self, hops: _Optional[_Iterable[_Union[CreateonionHops, _Mapping]]] = ..., assocdata: _Optional[bytes] = ..., session_key: _Optional[bytes] = ..., onion_size: _Optional[int] = ...) -> None: ...

class CreateonionResponse(_message.Message):
    __slots__ = ["onion", "shared_secrets"]
    ONION_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRETS_FIELD_NUMBER: _ClassVar[int]
    onion: bytes
    shared_secrets: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, onion: _Optional[bytes] = ..., shared_secrets: _Optional[_Iterable[bytes]] = ...) -> None: ...

class DatastoreRequest(_message.Message):
    __slots__ = ["generation", "hex", "key", "mode", "string"]
    class DatastoreMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATE_OR_APPEND: DatastoreRequest.DatastoreMode
    CREATE_OR_REPLACE: DatastoreRequest.DatastoreMode
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    HEX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MUST_APPEND: DatastoreRequest.DatastoreMode
    MUST_CREATE: DatastoreRequest.DatastoreMode
    MUST_REPLACE: DatastoreRequest.DatastoreMode
    STRING_FIELD_NUMBER: _ClassVar[int]
    generation: int
    hex: bytes
    key: _containers.RepeatedScalarFieldContainer[str]
    mode: DatastoreRequest.DatastoreMode
    string: str
    def __init__(self, key: _Optional[_Iterable[str]] = ..., string: _Optional[str] = ..., hex: _Optional[bytes] = ..., mode: _Optional[_Union[DatastoreRequest.DatastoreMode, str]] = ..., generation: _Optional[int] = ...) -> None: ...

class DatastoreResponse(_message.Message):
    __slots__ = ["generation", "hex", "key", "string"]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    HEX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    generation: int
    hex: bytes
    key: _containers.RepeatedScalarFieldContainer[str]
    string: str
    def __init__(self, key: _Optional[_Iterable[str]] = ..., generation: _Optional[int] = ..., hex: _Optional[bytes] = ..., string: _Optional[str] = ...) -> None: ...

class DeldatastoreRequest(_message.Message):
    __slots__ = ["generation", "key"]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    generation: int
    key: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[_Iterable[str]] = ..., generation: _Optional[int] = ...) -> None: ...

class DeldatastoreResponse(_message.Message):
    __slots__ = ["generation", "hex", "key", "string"]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    HEX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    generation: int
    hex: bytes
    key: _containers.RepeatedScalarFieldContainer[str]
    string: str
    def __init__(self, key: _Optional[_Iterable[str]] = ..., generation: _Optional[int] = ..., hex: _Optional[bytes] = ..., string: _Optional[str] = ...) -> None: ...

class DelexpiredinvoiceRequest(_message.Message):
    __slots__ = ["maxexpirytime"]
    MAXEXPIRYTIME_FIELD_NUMBER: _ClassVar[int]
    maxexpirytime: int
    def __init__(self, maxexpirytime: _Optional[int] = ...) -> None: ...

class DelexpiredinvoiceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DelinvoiceRequest(_message.Message):
    __slots__ = ["desconly", "label", "status"]
    class DelinvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DESCONLY_FIELD_NUMBER: _ClassVar[int]
    EXPIRED: DelinvoiceRequest.DelinvoiceStatus
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PAID: DelinvoiceRequest.DelinvoiceStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNPAID: DelinvoiceRequest.DelinvoiceStatus
    desconly: bool
    label: str
    status: DelinvoiceRequest.DelinvoiceStatus
    def __init__(self, label: _Optional[str] = ..., status: _Optional[_Union[DelinvoiceRequest.DelinvoiceStatus, str]] = ..., desconly: bool = ...) -> None: ...

class DelinvoiceResponse(_message.Message):
    __slots__ = ["amount_msat", "bolt11", "bolt12", "description", "expires_at", "invreq_payer_note", "label", "local_offer_id", "payment_hash", "status"]
    class DelinvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED: DelinvoiceResponse.DelinvoiceStatus
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    INVREQ_PAYER_NOTE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    PAID: DelinvoiceResponse.DelinvoiceStatus
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNPAID: DelinvoiceResponse.DelinvoiceStatus
    amount_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    description: str
    expires_at: int
    invreq_payer_note: str
    label: str
    local_offer_id: bytes
    payment_hash: bytes
    status: DelinvoiceResponse.DelinvoiceStatus
    def __init__(self, label: _Optional[str] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., description: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[DelinvoiceResponse.DelinvoiceStatus, str]] = ..., expires_at: _Optional[int] = ..., local_offer_id: _Optional[bytes] = ..., invreq_payer_note: _Optional[str] = ...) -> None: ...

class DisconnectRequest(_message.Message):
    __slots__ = ["force", "id"]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    force: bool
    id: bytes
    def __init__(self, id: _Optional[bytes] = ..., force: bool = ...) -> None: ...

class DisconnectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FeeratesOnchain_fee_estimates(_message.Message):
    __slots__ = ["htlc_success_satoshis", "htlc_timeout_satoshis", "mutual_close_satoshis", "opening_channel_satoshis", "unilateral_close_satoshis"]
    HTLC_SUCCESS_SATOSHIS_FIELD_NUMBER: _ClassVar[int]
    HTLC_TIMEOUT_SATOSHIS_FIELD_NUMBER: _ClassVar[int]
    MUTUAL_CLOSE_SATOSHIS_FIELD_NUMBER: _ClassVar[int]
    OPENING_CHANNEL_SATOSHIS_FIELD_NUMBER: _ClassVar[int]
    UNILATERAL_CLOSE_SATOSHIS_FIELD_NUMBER: _ClassVar[int]
    htlc_success_satoshis: int
    htlc_timeout_satoshis: int
    mutual_close_satoshis: int
    opening_channel_satoshis: int
    unilateral_close_satoshis: int
    def __init__(self, opening_channel_satoshis: _Optional[int] = ..., mutual_close_satoshis: _Optional[int] = ..., unilateral_close_satoshis: _Optional[int] = ..., htlc_timeout_satoshis: _Optional[int] = ..., htlc_success_satoshis: _Optional[int] = ...) -> None: ...

class FeeratesPerkb(_message.Message):
    __slots__ = ["delayed_to_us", "htlc_resolution", "max_acceptable", "min_acceptable", "mutual_close", "opening", "penalty", "unilateral_close"]
    DELAYED_TO_US_FIELD_NUMBER: _ClassVar[int]
    HTLC_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    MAX_ACCEPTABLE_FIELD_NUMBER: _ClassVar[int]
    MIN_ACCEPTABLE_FIELD_NUMBER: _ClassVar[int]
    MUTUAL_CLOSE_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    UNILATERAL_CLOSE_FIELD_NUMBER: _ClassVar[int]
    delayed_to_us: int
    htlc_resolution: int
    max_acceptable: int
    min_acceptable: int
    mutual_close: int
    opening: int
    penalty: int
    unilateral_close: int
    def __init__(self, min_acceptable: _Optional[int] = ..., max_acceptable: _Optional[int] = ..., opening: _Optional[int] = ..., mutual_close: _Optional[int] = ..., unilateral_close: _Optional[int] = ..., delayed_to_us: _Optional[int] = ..., htlc_resolution: _Optional[int] = ..., penalty: _Optional[int] = ...) -> None: ...

class FeeratesPerkw(_message.Message):
    __slots__ = ["delayed_to_us", "htlc_resolution", "max_acceptable", "min_acceptable", "mutual_close", "opening", "penalty", "unilateral_close"]
    DELAYED_TO_US_FIELD_NUMBER: _ClassVar[int]
    HTLC_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    MAX_ACCEPTABLE_FIELD_NUMBER: _ClassVar[int]
    MIN_ACCEPTABLE_FIELD_NUMBER: _ClassVar[int]
    MUTUAL_CLOSE_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    UNILATERAL_CLOSE_FIELD_NUMBER: _ClassVar[int]
    delayed_to_us: int
    htlc_resolution: int
    max_acceptable: int
    min_acceptable: int
    mutual_close: int
    opening: int
    penalty: int
    unilateral_close: int
    def __init__(self, min_acceptable: _Optional[int] = ..., max_acceptable: _Optional[int] = ..., opening: _Optional[int] = ..., mutual_close: _Optional[int] = ..., unilateral_close: _Optional[int] = ..., delayed_to_us: _Optional[int] = ..., htlc_resolution: _Optional[int] = ..., penalty: _Optional[int] = ...) -> None: ...

class FeeratesRequest(_message.Message):
    __slots__ = ["style"]
    class FeeratesStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    PERKB: FeeratesRequest.FeeratesStyle
    PERKW: FeeratesRequest.FeeratesStyle
    STYLE_FIELD_NUMBER: _ClassVar[int]
    style: FeeratesRequest.FeeratesStyle
    def __init__(self, style: _Optional[_Union[FeeratesRequest.FeeratesStyle, str]] = ...) -> None: ...

class FeeratesResponse(_message.Message):
    __slots__ = ["warning_missing_feerates"]
    WARNING_MISSING_FEERATES_FIELD_NUMBER: _ClassVar[int]
    warning_missing_feerates: str
    def __init__(self, warning_missing_feerates: _Optional[str] = ...) -> None: ...

class FundchannelRequest(_message.Message):
    __slots__ = ["amount", "announce", "close_to", "compact_lease", "feerate", "id", "minconf", "mindepth", "push_msat", "request_amt", "reserve", "utxos"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TO_FIELD_NUMBER: _ClassVar[int]
    COMPACT_LEASE_FIELD_NUMBER: _ClassVar[int]
    FEERATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MINCONF_FIELD_NUMBER: _ClassVar[int]
    MINDEPTH_FIELD_NUMBER: _ClassVar[int]
    PUSH_MSAT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_AMT_FIELD_NUMBER: _ClassVar[int]
    RESERVE_FIELD_NUMBER: _ClassVar[int]
    UTXOS_FIELD_NUMBER: _ClassVar[int]
    amount: _primitives_pb2.AmountOrAll
    announce: bool
    close_to: str
    compact_lease: str
    feerate: _primitives_pb2.Feerate
    id: bytes
    minconf: int
    mindepth: int
    push_msat: _primitives_pb2.Amount
    request_amt: _primitives_pb2.Amount
    reserve: _primitives_pb2.Amount
    utxos: _containers.RepeatedCompositeFieldContainer[_primitives_pb2.Outpoint]
    def __init__(self, id: _Optional[bytes] = ..., amount: _Optional[_Union[_primitives_pb2.AmountOrAll, _Mapping]] = ..., feerate: _Optional[_Union[_primitives_pb2.Feerate, _Mapping]] = ..., announce: bool = ..., minconf: _Optional[int] = ..., push_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., close_to: _Optional[str] = ..., request_amt: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., compact_lease: _Optional[str] = ..., utxos: _Optional[_Iterable[_Union[_primitives_pb2.Outpoint, _Mapping]]] = ..., mindepth: _Optional[int] = ..., reserve: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ...) -> None: ...

class FundchannelResponse(_message.Message):
    __slots__ = ["channel_id", "close_to", "mindepth", "outnum", "tx", "txid"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TO_FIELD_NUMBER: _ClassVar[int]
    MINDEPTH_FIELD_NUMBER: _ClassVar[int]
    OUTNUM_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    channel_id: bytes
    close_to: bytes
    mindepth: int
    outnum: int
    tx: bytes
    txid: bytes
    def __init__(self, tx: _Optional[bytes] = ..., txid: _Optional[bytes] = ..., outnum: _Optional[int] = ..., channel_id: _Optional[bytes] = ..., close_to: _Optional[bytes] = ..., mindepth: _Optional[int] = ...) -> None: ...

class FundpsbtRequest(_message.Message):
    __slots__ = ["excess_as_change", "feerate", "locktime", "min_witness_weight", "minconf", "reserve", "satoshi", "startweight"]
    EXCESS_AS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    FEERATE_FIELD_NUMBER: _ClassVar[int]
    LOCKTIME_FIELD_NUMBER: _ClassVar[int]
    MINCONF_FIELD_NUMBER: _ClassVar[int]
    MIN_WITNESS_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RESERVE_FIELD_NUMBER: _ClassVar[int]
    SATOSHI_FIELD_NUMBER: _ClassVar[int]
    STARTWEIGHT_FIELD_NUMBER: _ClassVar[int]
    excess_as_change: bool
    feerate: _primitives_pb2.Feerate
    locktime: int
    min_witness_weight: int
    minconf: int
    reserve: int
    satoshi: _primitives_pb2.AmountOrAll
    startweight: int
    def __init__(self, satoshi: _Optional[_Union[_primitives_pb2.AmountOrAll, _Mapping]] = ..., feerate: _Optional[_Union[_primitives_pb2.Feerate, _Mapping]] = ..., startweight: _Optional[int] = ..., minconf: _Optional[int] = ..., reserve: _Optional[int] = ..., locktime: _Optional[int] = ..., min_witness_weight: _Optional[int] = ..., excess_as_change: bool = ...) -> None: ...

class FundpsbtReservations(_message.Message):
    __slots__ = ["reserved", "reserved_to_block", "txid", "vout", "was_reserved"]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    RESERVED_TO_BLOCK_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    VOUT_FIELD_NUMBER: _ClassVar[int]
    WAS_RESERVED_FIELD_NUMBER: _ClassVar[int]
    reserved: bool
    reserved_to_block: int
    txid: bytes
    vout: int
    was_reserved: bool
    def __init__(self, txid: _Optional[bytes] = ..., vout: _Optional[int] = ..., was_reserved: bool = ..., reserved: bool = ..., reserved_to_block: _Optional[int] = ...) -> None: ...

class FundpsbtResponse(_message.Message):
    __slots__ = ["change_outnum", "estimated_final_weight", "excess_msat", "feerate_per_kw", "psbt", "reservations"]
    CHANGE_OUTNUM_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_FINAL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXCESS_MSAT_FIELD_NUMBER: _ClassVar[int]
    FEERATE_PER_KW_FIELD_NUMBER: _ClassVar[int]
    PSBT_FIELD_NUMBER: _ClassVar[int]
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    change_outnum: int
    estimated_final_weight: int
    excess_msat: _primitives_pb2.Amount
    feerate_per_kw: int
    psbt: str
    reservations: _containers.RepeatedCompositeFieldContainer[FundpsbtReservations]
    def __init__(self, psbt: _Optional[str] = ..., feerate_per_kw: _Optional[int] = ..., estimated_final_weight: _Optional[int] = ..., excess_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., change_outnum: _Optional[int] = ..., reservations: _Optional[_Iterable[_Union[FundpsbtReservations, _Mapping]]] = ...) -> None: ...

class GetinfoAddress(_message.Message):
    __slots__ = ["address", "item_type", "port"]
    class GetinfoAddressType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DNS: GetinfoAddress.GetinfoAddressType
    IPV4: GetinfoAddress.GetinfoAddressType
    IPV6: GetinfoAddress.GetinfoAddressType
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TORV2: GetinfoAddress.GetinfoAddressType
    TORV3: GetinfoAddress.GetinfoAddressType
    WEBSOCKET: GetinfoAddress.GetinfoAddressType
    address: str
    item_type: GetinfoAddress.GetinfoAddressType
    port: int
    def __init__(self, item_type: _Optional[_Union[GetinfoAddress.GetinfoAddressType, str]] = ..., port: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class GetinfoBinding(_message.Message):
    __slots__ = ["address", "item_type", "port", "socket"]
    class GetinfoBindingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IPV4: GetinfoBinding.GetinfoBindingType
    IPV6: GetinfoBinding.GetinfoBindingType
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SOCKET: GetinfoBinding.GetinfoBindingType
    PORT_FIELD_NUMBER: _ClassVar[int]
    SOCKET_FIELD_NUMBER: _ClassVar[int]
    TORV2: GetinfoBinding.GetinfoBindingType
    TORV3: GetinfoBinding.GetinfoBindingType
    address: str
    item_type: GetinfoBinding.GetinfoBindingType
    port: int
    socket: str
    def __init__(self, item_type: _Optional[_Union[GetinfoBinding.GetinfoBindingType, str]] = ..., address: _Optional[str] = ..., port: _Optional[int] = ..., socket: _Optional[str] = ...) -> None: ...

class GetinfoOur_features(_message.Message):
    __slots__ = ["channel", "init", "invoice", "node"]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    INIT_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    channel: bytes
    init: bytes
    invoice: bytes
    node: bytes
    def __init__(self, init: _Optional[bytes] = ..., node: _Optional[bytes] = ..., channel: _Optional[bytes] = ..., invoice: _Optional[bytes] = ...) -> None: ...

class GetinfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetinfoResponse(_message.Message):
    __slots__ = ["address", "alias", "binding", "blockheight", "color", "fees_collected_msat", "id", "lightning_dir", "msatoshi_fees_collected", "network", "num_active_channels", "num_inactive_channels", "num_peers", "num_pending_channels", "version", "warning_bitcoind_sync", "warning_lightningd_sync"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    BINDING_FIELD_NUMBER: _ClassVar[int]
    BLOCKHEIGHT_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FEES_COLLECTED_MSAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LIGHTNING_DIR_FIELD_NUMBER: _ClassVar[int]
    MSATOSHI_FEES_COLLECTED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    NUM_ACTIVE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    NUM_INACTIVE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    NUM_PEERS_FIELD_NUMBER: _ClassVar[int]
    NUM_PENDING_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WARNING_BITCOIND_SYNC_FIELD_NUMBER: _ClassVar[int]
    WARNING_LIGHTNINGD_SYNC_FIELD_NUMBER: _ClassVar[int]
    address: _containers.RepeatedCompositeFieldContainer[GetinfoAddress]
    alias: str
    binding: _containers.RepeatedCompositeFieldContainer[GetinfoBinding]
    blockheight: int
    color: bytes
    fees_collected_msat: _primitives_pb2.Amount
    id: bytes
    lightning_dir: str
    msatoshi_fees_collected: int
    network: str
    num_active_channels: int
    num_inactive_channels: int
    num_peers: int
    num_pending_channels: int
    version: str
    warning_bitcoind_sync: str
    warning_lightningd_sync: str
    def __init__(self, id: _Optional[bytes] = ..., alias: _Optional[str] = ..., color: _Optional[bytes] = ..., num_peers: _Optional[int] = ..., num_pending_channels: _Optional[int] = ..., num_active_channels: _Optional[int] = ..., num_inactive_channels: _Optional[int] = ..., version: _Optional[str] = ..., lightning_dir: _Optional[str] = ..., blockheight: _Optional[int] = ..., network: _Optional[str] = ..., msatoshi_fees_collected: _Optional[int] = ..., fees_collected_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., address: _Optional[_Iterable[_Union[GetinfoAddress, _Mapping]]] = ..., binding: _Optional[_Iterable[_Union[GetinfoBinding, _Mapping]]] = ..., warning_bitcoind_sync: _Optional[str] = ..., warning_lightningd_sync: _Optional[str] = ...) -> None: ...

class GetrouteRequest(_message.Message):
    __slots__ = ["amount_msat", "cltv", "exclude", "fromid", "fuzzpercent", "id", "maxhops", "riskfactor"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    CLTV_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    FROMID_FIELD_NUMBER: _ClassVar[int]
    FUZZPERCENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAXHOPS_FIELD_NUMBER: _ClassVar[int]
    RISKFACTOR_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    cltv: float
    exclude: _containers.RepeatedScalarFieldContainer[str]
    fromid: bytes
    fuzzpercent: int
    id: bytes
    maxhops: int
    riskfactor: int
    def __init__(self, id: _Optional[bytes] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., riskfactor: _Optional[int] = ..., cltv: _Optional[float] = ..., fromid: _Optional[bytes] = ..., fuzzpercent: _Optional[int] = ..., exclude: _Optional[_Iterable[str]] = ..., maxhops: _Optional[int] = ...) -> None: ...

class GetrouteResponse(_message.Message):
    __slots__ = ["route"]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    route: _containers.RepeatedCompositeFieldContainer[GetrouteRoute]
    def __init__(self, route: _Optional[_Iterable[_Union[GetrouteRoute, _Mapping]]] = ...) -> None: ...

class GetrouteRoute(_message.Message):
    __slots__ = ["amount_msat", "channel", "delay", "direction", "id", "msatoshi", "style"]
    class GetrouteRouteStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MSATOSHI_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    TLV: GetrouteRoute.GetrouteRouteStyle
    amount_msat: _primitives_pb2.Amount
    channel: str
    delay: int
    direction: int
    id: bytes
    msatoshi: int
    style: GetrouteRoute.GetrouteRouteStyle
    def __init__(self, id: _Optional[bytes] = ..., channel: _Optional[str] = ..., direction: _Optional[int] = ..., msatoshi: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., delay: _Optional[int] = ..., style: _Optional[_Union[GetrouteRoute.GetrouteRouteStyle, str]] = ...) -> None: ...

class InvoiceRequest(_message.Message):
    __slots__ = ["amount_msat", "cltv", "deschashonly", "description", "expiry", "exposeprivatechannels", "fallbacks", "label", "preimage"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    CLTV_FIELD_NUMBER: _ClassVar[int]
    DESCHASHONLY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    EXPOSEPRIVATECHANNELS_FIELD_NUMBER: _ClassVar[int]
    FALLBACKS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.AmountOrAny
    cltv: int
    deschashonly: bool
    description: str
    expiry: int
    exposeprivatechannels: bool
    fallbacks: _containers.RepeatedScalarFieldContainer[str]
    label: str
    preimage: bytes
    def __init__(self, amount_msat: _Optional[_Union[_primitives_pb2.AmountOrAny, _Mapping]] = ..., description: _Optional[str] = ..., label: _Optional[str] = ..., expiry: _Optional[int] = ..., fallbacks: _Optional[_Iterable[str]] = ..., preimage: _Optional[bytes] = ..., exposeprivatechannels: bool = ..., cltv: _Optional[int] = ..., deschashonly: bool = ...) -> None: ...

class InvoiceResponse(_message.Message):
    __slots__ = ["bolt11", "expires_at", "payment_hash", "payment_secret", "warning_capacity", "warning_deadends", "warning_mpp", "warning_offline", "warning_private_unused"]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    WARNING_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    WARNING_DEADENDS_FIELD_NUMBER: _ClassVar[int]
    WARNING_MPP_FIELD_NUMBER: _ClassVar[int]
    WARNING_OFFLINE_FIELD_NUMBER: _ClassVar[int]
    WARNING_PRIVATE_UNUSED_FIELD_NUMBER: _ClassVar[int]
    bolt11: str
    expires_at: int
    payment_hash: bytes
    payment_secret: bytes
    warning_capacity: str
    warning_deadends: str
    warning_mpp: str
    warning_offline: str
    warning_private_unused: str
    def __init__(self, bolt11: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., payment_secret: _Optional[bytes] = ..., expires_at: _Optional[int] = ..., warning_capacity: _Optional[str] = ..., warning_offline: _Optional[str] = ..., warning_deadends: _Optional[str] = ..., warning_private_unused: _Optional[str] = ..., warning_mpp: _Optional[str] = ...) -> None: ...

class KeysendRequest(_message.Message):
    __slots__ = ["amount_msat", "destination", "exemptfee", "extratlvs", "label", "maxdelay", "maxfeepercent", "retry_for", "routehints"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    EXEMPTFEE_FIELD_NUMBER: _ClassVar[int]
    EXTRATLVS_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    MAXDELAY_FIELD_NUMBER: _ClassVar[int]
    MAXFEEPERCENT_FIELD_NUMBER: _ClassVar[int]
    RETRY_FOR_FIELD_NUMBER: _ClassVar[int]
    ROUTEHINTS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    destination: bytes
    exemptfee: _primitives_pb2.Amount
    extratlvs: _primitives_pb2.TlvStream
    label: str
    maxdelay: int
    maxfeepercent: float
    retry_for: int
    routehints: _primitives_pb2.RoutehintList
    def __init__(self, destination: _Optional[bytes] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., label: _Optional[str] = ..., maxfeepercent: _Optional[float] = ..., retry_for: _Optional[int] = ..., maxdelay: _Optional[int] = ..., exemptfee: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., routehints: _Optional[_Union[_primitives_pb2.RoutehintList, _Mapping]] = ..., extratlvs: _Optional[_Union[_primitives_pb2.TlvStream, _Mapping]] = ...) -> None: ...

class KeysendResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_sent_msat", "created_at", "destination", "parts", "payment_hash", "payment_preimage", "status", "warning_partial_completion"]
    class KeysendStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_SENT_MSAT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: KeysendResponse.KeysendStatus
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNING_PARTIAL_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_sent_msat: _primitives_pb2.Amount
    created_at: float
    destination: bytes
    parts: int
    payment_hash: bytes
    payment_preimage: bytes
    status: KeysendResponse.KeysendStatus
    warning_partial_completion: str
    def __init__(self, payment_preimage: _Optional[bytes] = ..., destination: _Optional[bytes] = ..., payment_hash: _Optional[bytes] = ..., created_at: _Optional[float] = ..., parts: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., amount_sent_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., warning_partial_completion: _Optional[str] = ..., status: _Optional[_Union[KeysendResponse.KeysendStatus, str]] = ...) -> None: ...

class ListchannelsChannels(_message.Message):
    __slots__ = ["active", "amount_msat", "base_fee_millisatoshi", "channel_flags", "delay", "destination", "features", "fee_per_millionth", "htlc_maximum_msat", "htlc_minimum_msat", "last_update", "message_flags", "public", "short_channel_id", "source"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BASE_FEE_MILLISATOSHI_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    FEE_PER_MILLIONTH_FIELD_NUMBER: _ClassVar[int]
    HTLC_MAXIMUM_MSAT_FIELD_NUMBER: _ClassVar[int]
    HTLC_MINIMUM_MSAT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    SHORT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    amount_msat: _primitives_pb2.Amount
    base_fee_millisatoshi: int
    channel_flags: int
    delay: int
    destination: bytes
    features: bytes
    fee_per_millionth: int
    htlc_maximum_msat: _primitives_pb2.Amount
    htlc_minimum_msat: _primitives_pb2.Amount
    last_update: int
    message_flags: int
    public: bool
    short_channel_id: str
    source: bytes
    def __init__(self, source: _Optional[bytes] = ..., destination: _Optional[bytes] = ..., short_channel_id: _Optional[str] = ..., public: bool = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., message_flags: _Optional[int] = ..., channel_flags: _Optional[int] = ..., active: bool = ..., last_update: _Optional[int] = ..., base_fee_millisatoshi: _Optional[int] = ..., fee_per_millionth: _Optional[int] = ..., delay: _Optional[int] = ..., htlc_minimum_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., htlc_maximum_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., features: _Optional[bytes] = ...) -> None: ...

class ListchannelsRequest(_message.Message):
    __slots__ = ["destination", "short_channel_id", "source"]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SHORT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    destination: bytes
    short_channel_id: str
    source: bytes
    def __init__(self, short_channel_id: _Optional[str] = ..., source: _Optional[bytes] = ..., destination: _Optional[bytes] = ...) -> None: ...

class ListchannelsResponse(_message.Message):
    __slots__ = ["channels"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[ListchannelsChannels]
    def __init__(self, channels: _Optional[_Iterable[_Union[ListchannelsChannels, _Mapping]]] = ...) -> None: ...

class ListdatastoreDatastore(_message.Message):
    __slots__ = ["generation", "hex", "key", "string"]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    HEX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    generation: int
    hex: bytes
    key: _containers.RepeatedScalarFieldContainer[str]
    string: str
    def __init__(self, key: _Optional[_Iterable[str]] = ..., generation: _Optional[int] = ..., hex: _Optional[bytes] = ..., string: _Optional[str] = ...) -> None: ...

class ListdatastoreRequest(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key: _Optional[_Iterable[str]] = ...) -> None: ...

class ListdatastoreResponse(_message.Message):
    __slots__ = ["datastore"]
    DATASTORE_FIELD_NUMBER: _ClassVar[int]
    datastore: _containers.RepeatedCompositeFieldContainer[ListdatastoreDatastore]
    def __init__(self, datastore: _Optional[_Iterable[_Union[ListdatastoreDatastore, _Mapping]]] = ...) -> None: ...

class ListforwardsForwards(_message.Message):
    __slots__ = ["fee_msat", "in_channel", "in_htlc_id", "in_msat", "out_channel", "out_htlc_id", "out_msat", "received_time", "status", "style"]
    class ListforwardsForwardsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ListforwardsForwardsStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FAILED: ListforwardsForwards.ListforwardsForwardsStatus
    FEE_MSAT_FIELD_NUMBER: _ClassVar[int]
    IN_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    IN_HTLC_ID_FIELD_NUMBER: _ClassVar[int]
    IN_MSAT_FIELD_NUMBER: _ClassVar[int]
    LEGACY: ListforwardsForwards.ListforwardsForwardsStyle
    LOCAL_FAILED: ListforwardsForwards.ListforwardsForwardsStatus
    OFFERED: ListforwardsForwards.ListforwardsForwardsStatus
    OUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    OUT_HTLC_ID_FIELD_NUMBER: _ClassVar[int]
    OUT_MSAT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_TIME_FIELD_NUMBER: _ClassVar[int]
    SETTLED: ListforwardsForwards.ListforwardsForwardsStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    TLV: ListforwardsForwards.ListforwardsForwardsStyle
    fee_msat: _primitives_pb2.Amount
    in_channel: str
    in_htlc_id: int
    in_msat: _primitives_pb2.Amount
    out_channel: str
    out_htlc_id: int
    out_msat: _primitives_pb2.Amount
    received_time: float
    status: ListforwardsForwards.ListforwardsForwardsStatus
    style: ListforwardsForwards.ListforwardsForwardsStyle
    def __init__(self, in_channel: _Optional[str] = ..., in_htlc_id: _Optional[int] = ..., in_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., status: _Optional[_Union[ListforwardsForwards.ListforwardsForwardsStatus, str]] = ..., received_time: _Optional[float] = ..., out_channel: _Optional[str] = ..., out_htlc_id: _Optional[int] = ..., style: _Optional[_Union[ListforwardsForwards.ListforwardsForwardsStyle, str]] = ..., fee_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., out_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ...) -> None: ...

class ListforwardsRequest(_message.Message):
    __slots__ = ["in_channel", "out_channel", "status"]
    class ListforwardsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FAILED: ListforwardsRequest.ListforwardsStatus
    IN_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FAILED: ListforwardsRequest.ListforwardsStatus
    OFFERED: ListforwardsRequest.ListforwardsStatus
    OUT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SETTLED: ListforwardsRequest.ListforwardsStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    in_channel: str
    out_channel: str
    status: ListforwardsRequest.ListforwardsStatus
    def __init__(self, status: _Optional[_Union[ListforwardsRequest.ListforwardsStatus, str]] = ..., in_channel: _Optional[str] = ..., out_channel: _Optional[str] = ...) -> None: ...

class ListforwardsResponse(_message.Message):
    __slots__ = ["forwards"]
    FORWARDS_FIELD_NUMBER: _ClassVar[int]
    forwards: _containers.RepeatedCompositeFieldContainer[ListforwardsForwards]
    def __init__(self, forwards: _Optional[_Iterable[_Union[ListforwardsForwards, _Mapping]]] = ...) -> None: ...

class ListfundsChannels(_message.Message):
    __slots__ = ["amount_msat", "connected", "funding_output", "funding_txid", "our_amount_msat", "peer_id", "short_channel_id", "state"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    FUNDING_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    FUNDING_TXID_FIELD_NUMBER: _ClassVar[int]
    OUR_AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    SHORT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    connected: bool
    funding_output: int
    funding_txid: bytes
    our_amount_msat: _primitives_pb2.Amount
    peer_id: bytes
    short_channel_id: str
    state: _primitives_pb2.ChannelState
    def __init__(self, peer_id: _Optional[bytes] = ..., our_amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., funding_txid: _Optional[bytes] = ..., funding_output: _Optional[int] = ..., connected: bool = ..., state: _Optional[_Union[_primitives_pb2.ChannelState, str]] = ..., short_channel_id: _Optional[str] = ...) -> None: ...

class ListfundsOutputs(_message.Message):
    __slots__ = ["address", "amount_msat", "blockheight", "output", "redeemscript", "reserved", "scriptpubkey", "status", "txid"]
    class ListfundsOutputsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BLOCKHEIGHT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED: ListfundsOutputs.ListfundsOutputsStatus
    IMMATURE: ListfundsOutputs.ListfundsOutputsStatus
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    REDEEMSCRIPT_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    SCRIPTPUBKEY_FIELD_NUMBER: _ClassVar[int]
    SPENT: ListfundsOutputs.ListfundsOutputsStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    UNCONFIRMED: ListfundsOutputs.ListfundsOutputsStatus
    address: str
    amount_msat: _primitives_pb2.Amount
    blockheight: int
    output: int
    redeemscript: bytes
    reserved: bool
    scriptpubkey: bytes
    status: ListfundsOutputs.ListfundsOutputsStatus
    txid: bytes
    def __init__(self, txid: _Optional[bytes] = ..., output: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., scriptpubkey: _Optional[bytes] = ..., address: _Optional[str] = ..., redeemscript: _Optional[bytes] = ..., status: _Optional[_Union[ListfundsOutputs.ListfundsOutputsStatus, str]] = ..., reserved: bool = ..., blockheight: _Optional[int] = ...) -> None: ...

class ListfundsRequest(_message.Message):
    __slots__ = ["spent"]
    SPENT_FIELD_NUMBER: _ClassVar[int]
    spent: bool
    def __init__(self, spent: bool = ...) -> None: ...

class ListfundsResponse(_message.Message):
    __slots__ = ["channels", "outputs"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[ListfundsChannels]
    outputs: _containers.RepeatedCompositeFieldContainer[ListfundsOutputs]
    def __init__(self, outputs: _Optional[_Iterable[_Union[ListfundsOutputs, _Mapping]]] = ..., channels: _Optional[_Iterable[_Union[ListfundsChannels, _Mapping]]] = ...) -> None: ...

class ListinvoicesInvoices(_message.Message):
    __slots__ = ["amount_msat", "amount_received_msat", "bolt11", "bolt12", "description", "expires_at", "invreq_payer_note", "label", "local_offer_id", "paid_at", "pay_index", "payment_hash", "payment_preimage", "status"]
    class ListinvoicesInvoicesStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_RECEIVED_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED: ListinvoicesInvoices.ListinvoicesInvoicesStatus
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    INVREQ_PAYER_NOTE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    PAID: ListinvoicesInvoices.ListinvoicesInvoicesStatus
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PAY_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNPAID: ListinvoicesInvoices.ListinvoicesInvoicesStatus
    amount_msat: _primitives_pb2.Amount
    amount_received_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    description: str
    expires_at: int
    invreq_payer_note: str
    label: str
    local_offer_id: bytes
    paid_at: int
    pay_index: int
    payment_hash: bytes
    payment_preimage: bytes
    status: ListinvoicesInvoices.ListinvoicesInvoicesStatus
    def __init__(self, label: _Optional[str] = ..., description: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[ListinvoicesInvoices.ListinvoicesInvoicesStatus, str]] = ..., expires_at: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., local_offer_id: _Optional[bytes] = ..., invreq_payer_note: _Optional[str] = ..., pay_index: _Optional[int] = ..., amount_received_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., paid_at: _Optional[int] = ..., payment_preimage: _Optional[bytes] = ...) -> None: ...

class ListinvoicesRequest(_message.Message):
    __slots__ = ["invstring", "label", "offer_id", "payment_hash"]
    INVSTRING_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    OFFER_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    invstring: str
    label: str
    offer_id: str
    payment_hash: bytes
    def __init__(self, label: _Optional[str] = ..., invstring: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., offer_id: _Optional[str] = ...) -> None: ...

class ListinvoicesResponse(_message.Message):
    __slots__ = ["invoices"]
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    invoices: _containers.RepeatedCompositeFieldContainer[ListinvoicesInvoices]
    def __init__(self, invoices: _Optional[_Iterable[_Union[ListinvoicesInvoices, _Mapping]]] = ...) -> None: ...

class ListnodesNodes(_message.Message):
    __slots__ = ["addresses", "alias", "color", "features", "last_timestamp", "nodeid"]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    LAST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[ListnodesNodesAddresses]
    alias: str
    color: bytes
    features: bytes
    last_timestamp: int
    nodeid: bytes
    def __init__(self, nodeid: _Optional[bytes] = ..., last_timestamp: _Optional[int] = ..., alias: _Optional[str] = ..., color: _Optional[bytes] = ..., features: _Optional[bytes] = ..., addresses: _Optional[_Iterable[_Union[ListnodesNodesAddresses, _Mapping]]] = ...) -> None: ...

class ListnodesNodesAddresses(_message.Message):
    __slots__ = ["address", "item_type", "port"]
    class ListnodesNodesAddressesType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DNS: ListnodesNodesAddresses.ListnodesNodesAddressesType
    IPV4: ListnodesNodesAddresses.ListnodesNodesAddressesType
    IPV6: ListnodesNodesAddresses.ListnodesNodesAddressesType
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TORV2: ListnodesNodesAddresses.ListnodesNodesAddressesType
    TORV3: ListnodesNodesAddresses.ListnodesNodesAddressesType
    WEBSOCKET: ListnodesNodesAddresses.ListnodesNodesAddressesType
    address: str
    item_type: ListnodesNodesAddresses.ListnodesNodesAddressesType
    port: int
    def __init__(self, item_type: _Optional[_Union[ListnodesNodesAddresses.ListnodesNodesAddressesType, str]] = ..., port: _Optional[int] = ..., address: _Optional[str] = ...) -> None: ...

class ListnodesRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    def __init__(self, id: _Optional[bytes] = ...) -> None: ...

class ListnodesResponse(_message.Message):
    __slots__ = ["nodes"]
    NODES_FIELD_NUMBER: _ClassVar[int]
    nodes: _containers.RepeatedCompositeFieldContainer[ListnodesNodes]
    def __init__(self, nodes: _Optional[_Iterable[_Union[ListnodesNodes, _Mapping]]] = ...) -> None: ...

class ListpaysPays(_message.Message):
    __slots__ = ["bolt11", "bolt12", "completed_at", "created_at", "description", "destination", "erroronion", "label", "number_of_parts", "payment_hash", "preimage", "status"]
    class ListpaysPaysStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: ListpaysPays.ListpaysPaysStatus
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ERRORONION_FIELD_NUMBER: _ClassVar[int]
    FAILED: ListpaysPays.ListpaysPaysStatus
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_PARTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PENDING: ListpaysPays.ListpaysPaysStatus
    PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    bolt11: str
    bolt12: str
    completed_at: int
    created_at: int
    description: str
    destination: bytes
    erroronion: bytes
    label: str
    number_of_parts: int
    payment_hash: bytes
    preimage: bytes
    status: ListpaysPays.ListpaysPaysStatus
    def __init__(self, payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[ListpaysPays.ListpaysPaysStatus, str]] = ..., destination: _Optional[bytes] = ..., created_at: _Optional[int] = ..., completed_at: _Optional[int] = ..., label: _Optional[str] = ..., bolt11: _Optional[str] = ..., description: _Optional[str] = ..., bolt12: _Optional[str] = ..., preimage: _Optional[bytes] = ..., number_of_parts: _Optional[int] = ..., erroronion: _Optional[bytes] = ...) -> None: ...

class ListpaysRequest(_message.Message):
    __slots__ = ["bolt11", "payment_hash", "status"]
    class ListpaysStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: ListpaysRequest.ListpaysStatus
    FAILED: ListpaysRequest.ListpaysStatus
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PENDING: ListpaysRequest.ListpaysStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    bolt11: str
    payment_hash: bytes
    status: ListpaysRequest.ListpaysStatus
    def __init__(self, bolt11: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[ListpaysRequest.ListpaysStatus, str]] = ...) -> None: ...

class ListpaysResponse(_message.Message):
    __slots__ = ["pays"]
    PAYS_FIELD_NUMBER: _ClassVar[int]
    pays: _containers.RepeatedCompositeFieldContainer[ListpaysPays]
    def __init__(self, pays: _Optional[_Iterable[_Union[ListpaysPays, _Mapping]]] = ...) -> None: ...

class ListpeersPeers(_message.Message):
    __slots__ = ["channels", "connected", "features", "id", "log", "netaddr", "remote_addr"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    NETADDR_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDR_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[ListpeersPeersChannels]
    connected: bool
    features: bytes
    id: bytes
    log: _containers.RepeatedCompositeFieldContainer[ListpeersPeersLog]
    netaddr: _containers.RepeatedScalarFieldContainer[str]
    remote_addr: str
    def __init__(self, id: _Optional[bytes] = ..., connected: bool = ..., log: _Optional[_Iterable[_Union[ListpeersPeersLog, _Mapping]]] = ..., channels: _Optional[_Iterable[_Union[ListpeersPeersChannels, _Mapping]]] = ..., netaddr: _Optional[_Iterable[str]] = ..., remote_addr: _Optional[str] = ..., features: _Optional[bytes] = ...) -> None: ...

class ListpeersPeersChannels(_message.Message):
    __slots__ = ["channel_id", "close_to", "close_to_addr", "closer", "dust_limit_msat", "features", "fee_base_msat", "fee_proportional_millionths", "funding_outnum", "funding_txid", "htlcs", "in_fulfilled_msat", "in_offered_msat", "in_payments_fulfilled", "in_payments_offered", "inflight", "initial_feerate", "last_feerate", "max_accepted_htlcs", "max_to_us_msat", "max_total_htlc_in_msat", "maximum_htlc_out_msat", "min_to_us_msat", "minimum_htlc_in_msat", "minimum_htlc_out_msat", "next_fee_step", "next_feerate", "opener", "our_reserve_msat", "our_to_self_delay", "out_fulfilled_msat", "out_offered_msat", "out_payments_fulfilled", "out_payments_offered", "owner", "private", "receivable_msat", "scratch_txid", "short_channel_id", "spendable_msat", "state", "status", "their_reserve_msat", "their_to_self_delay", "to_us_msat", "total_msat"]
    class ListpeersPeersChannelsState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AWAITING_UNILATERAL: ListpeersPeersChannels.ListpeersPeersChannelsState
    CHANNELD_AWAITING_LOCKIN: ListpeersPeersChannels.ListpeersPeersChannelsState
    CHANNELD_NORMAL: ListpeersPeersChannels.ListpeersPeersChannelsState
    CHANNELD_SHUTTING_DOWN: ListpeersPeersChannels.ListpeersPeersChannelsState
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CLOSER_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TO_ADDR_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TO_FIELD_NUMBER: _ClassVar[int]
    CLOSINGD_COMPLETE: ListpeersPeersChannels.ListpeersPeersChannelsState
    CLOSINGD_SIGEXCHANGE: ListpeersPeersChannels.ListpeersPeersChannelsState
    DUALOPEND_AWAITING_LOCKIN: ListpeersPeersChannels.ListpeersPeersChannelsState
    DUALOPEND_OPEN_INIT: ListpeersPeersChannels.ListpeersPeersChannelsState
    DUST_LIMIT_MSAT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    FEE_BASE_MSAT_FIELD_NUMBER: _ClassVar[int]
    FEE_PROPORTIONAL_MILLIONTHS_FIELD_NUMBER: _ClassVar[int]
    FUNDING_OUTNUM_FIELD_NUMBER: _ClassVar[int]
    FUNDING_SPEND_SEEN: ListpeersPeersChannels.ListpeersPeersChannelsState
    FUNDING_TXID_FIELD_NUMBER: _ClassVar[int]
    HTLCS_FIELD_NUMBER: _ClassVar[int]
    INFLIGHT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_FEERATE_FIELD_NUMBER: _ClassVar[int]
    IN_FULFILLED_MSAT_FIELD_NUMBER: _ClassVar[int]
    IN_OFFERED_MSAT_FIELD_NUMBER: _ClassVar[int]
    IN_PAYMENTS_FULFILLED_FIELD_NUMBER: _ClassVar[int]
    IN_PAYMENTS_OFFERED_FIELD_NUMBER: _ClassVar[int]
    LAST_FEERATE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_HTLC_OUT_MSAT_FIELD_NUMBER: _ClassVar[int]
    MAX_ACCEPTED_HTLCS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOTAL_HTLC_IN_MSAT_FIELD_NUMBER: _ClassVar[int]
    MAX_TO_US_MSAT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_HTLC_IN_MSAT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_HTLC_OUT_MSAT_FIELD_NUMBER: _ClassVar[int]
    MIN_TO_US_MSAT_FIELD_NUMBER: _ClassVar[int]
    NEXT_FEERATE_FIELD_NUMBER: _ClassVar[int]
    NEXT_FEE_STEP_FIELD_NUMBER: _ClassVar[int]
    ONCHAIN: ListpeersPeersChannels.ListpeersPeersChannelsState
    OPENER_FIELD_NUMBER: _ClassVar[int]
    OPENINGD: ListpeersPeersChannels.ListpeersPeersChannelsState
    OUR_RESERVE_MSAT_FIELD_NUMBER: _ClassVar[int]
    OUR_TO_SELF_DELAY_FIELD_NUMBER: _ClassVar[int]
    OUT_FULFILLED_MSAT_FIELD_NUMBER: _ClassVar[int]
    OUT_OFFERED_MSAT_FIELD_NUMBER: _ClassVar[int]
    OUT_PAYMENTS_FULFILLED_FIELD_NUMBER: _ClassVar[int]
    OUT_PAYMENTS_OFFERED_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    RECEIVABLE_MSAT_FIELD_NUMBER: _ClassVar[int]
    SCRATCH_TXID_FIELD_NUMBER: _ClassVar[int]
    SHORT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SPENDABLE_MSAT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    THEIR_RESERVE_MSAT_FIELD_NUMBER: _ClassVar[int]
    THEIR_TO_SELF_DELAY_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MSAT_FIELD_NUMBER: _ClassVar[int]
    TO_US_MSAT_FIELD_NUMBER: _ClassVar[int]
    channel_id: bytes
    close_to: bytes
    close_to_addr: str
    closer: _primitives_pb2.ChannelSide
    dust_limit_msat: _primitives_pb2.Amount
    features: _containers.RepeatedScalarFieldContainer[str]
    fee_base_msat: _primitives_pb2.Amount
    fee_proportional_millionths: int
    funding_outnum: int
    funding_txid: bytes
    htlcs: _containers.RepeatedCompositeFieldContainer[ListpeersPeersChannelsHtlcs]
    in_fulfilled_msat: _primitives_pb2.Amount
    in_offered_msat: _primitives_pb2.Amount
    in_payments_fulfilled: int
    in_payments_offered: int
    inflight: _containers.RepeatedCompositeFieldContainer[ListpeersPeersChannelsInflight]
    initial_feerate: str
    last_feerate: str
    max_accepted_htlcs: int
    max_to_us_msat: _primitives_pb2.Amount
    max_total_htlc_in_msat: _primitives_pb2.Amount
    maximum_htlc_out_msat: _primitives_pb2.Amount
    min_to_us_msat: _primitives_pb2.Amount
    minimum_htlc_in_msat: _primitives_pb2.Amount
    minimum_htlc_out_msat: _primitives_pb2.Amount
    next_fee_step: int
    next_feerate: str
    opener: _primitives_pb2.ChannelSide
    our_reserve_msat: _primitives_pb2.Amount
    our_to_self_delay: int
    out_fulfilled_msat: _primitives_pb2.Amount
    out_offered_msat: _primitives_pb2.Amount
    out_payments_fulfilled: int
    out_payments_offered: int
    owner: str
    private: bool
    receivable_msat: _primitives_pb2.Amount
    scratch_txid: bytes
    short_channel_id: str
    spendable_msat: _primitives_pb2.Amount
    state: ListpeersPeersChannels.ListpeersPeersChannelsState
    status: _containers.RepeatedScalarFieldContainer[str]
    their_reserve_msat: _primitives_pb2.Amount
    their_to_self_delay: int
    to_us_msat: _primitives_pb2.Amount
    total_msat: _primitives_pb2.Amount
    def __init__(self, state: _Optional[_Union[ListpeersPeersChannels.ListpeersPeersChannelsState, str]] = ..., scratch_txid: _Optional[bytes] = ..., owner: _Optional[str] = ..., short_channel_id: _Optional[str] = ..., channel_id: _Optional[bytes] = ..., funding_txid: _Optional[bytes] = ..., funding_outnum: _Optional[int] = ..., initial_feerate: _Optional[str] = ..., last_feerate: _Optional[str] = ..., next_feerate: _Optional[str] = ..., next_fee_step: _Optional[int] = ..., inflight: _Optional[_Iterable[_Union[ListpeersPeersChannelsInflight, _Mapping]]] = ..., close_to: _Optional[bytes] = ..., private: bool = ..., opener: _Optional[_Union[_primitives_pb2.ChannelSide, str]] = ..., closer: _Optional[_Union[_primitives_pb2.ChannelSide, str]] = ..., features: _Optional[_Iterable[str]] = ..., to_us_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., min_to_us_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., max_to_us_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., total_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., fee_base_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., fee_proportional_millionths: _Optional[int] = ..., dust_limit_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., max_total_htlc_in_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., their_reserve_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., our_reserve_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., spendable_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., receivable_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., minimum_htlc_in_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., minimum_htlc_out_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., maximum_htlc_out_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., their_to_self_delay: _Optional[int] = ..., our_to_self_delay: _Optional[int] = ..., max_accepted_htlcs: _Optional[int] = ..., status: _Optional[_Iterable[str]] = ..., in_payments_offered: _Optional[int] = ..., in_offered_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., in_payments_fulfilled: _Optional[int] = ..., in_fulfilled_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., out_payments_offered: _Optional[int] = ..., out_offered_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., out_payments_fulfilled: _Optional[int] = ..., out_fulfilled_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., htlcs: _Optional[_Iterable[_Union[ListpeersPeersChannelsHtlcs, _Mapping]]] = ..., close_to_addr: _Optional[str] = ...) -> None: ...

class ListpeersPeersChannelsAlias(_message.Message):
    __slots__ = ["local", "remote"]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    local: str
    remote: str
    def __init__(self, local: _Optional[str] = ..., remote: _Optional[str] = ...) -> None: ...

class ListpeersPeersChannelsFeerate(_message.Message):
    __slots__ = ["perkb", "perkw"]
    PERKB_FIELD_NUMBER: _ClassVar[int]
    PERKW_FIELD_NUMBER: _ClassVar[int]
    perkb: int
    perkw: int
    def __init__(self, perkw: _Optional[int] = ..., perkb: _Optional[int] = ...) -> None: ...

class ListpeersPeersChannelsFunding(_message.Message):
    __slots__ = ["fee_paid_msat", "fee_rcvd_msat", "local_funds_msat", "local_msat", "pushed_msat", "remote_funds_msat", "remote_msat"]
    FEE_PAID_MSAT_FIELD_NUMBER: _ClassVar[int]
    FEE_RCVD_MSAT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FUNDS_MSAT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_MSAT_FIELD_NUMBER: _ClassVar[int]
    PUSHED_MSAT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_FUNDS_MSAT_FIELD_NUMBER: _ClassVar[int]
    REMOTE_MSAT_FIELD_NUMBER: _ClassVar[int]
    fee_paid_msat: _primitives_pb2.Amount
    fee_rcvd_msat: _primitives_pb2.Amount
    local_funds_msat: _primitives_pb2.Amount
    local_msat: _primitives_pb2.Amount
    pushed_msat: _primitives_pb2.Amount
    remote_funds_msat: _primitives_pb2.Amount
    remote_msat: _primitives_pb2.Amount
    def __init__(self, local_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., remote_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., pushed_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., local_funds_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., remote_funds_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., fee_paid_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., fee_rcvd_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ...) -> None: ...

class ListpeersPeersChannelsHtlcs(_message.Message):
    __slots__ = ["amount_msat", "direction", "expiry", "id", "local_trimmed", "payment_hash", "status"]
    class ListpeersPeersChannelsHtlcsDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IN: ListpeersPeersChannelsHtlcs.ListpeersPeersChannelsHtlcsDirection
    LOCAL_TRIMMED_FIELD_NUMBER: _ClassVar[int]
    OUT: ListpeersPeersChannelsHtlcs.ListpeersPeersChannelsHtlcsDirection
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    direction: ListpeersPeersChannelsHtlcs.ListpeersPeersChannelsHtlcsDirection
    expiry: int
    id: int
    local_trimmed: bool
    payment_hash: bytes
    status: str
    def __init__(self, direction: _Optional[_Union[ListpeersPeersChannelsHtlcs.ListpeersPeersChannelsHtlcsDirection, str]] = ..., id: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., expiry: _Optional[int] = ..., payment_hash: _Optional[bytes] = ..., local_trimmed: bool = ..., status: _Optional[str] = ...) -> None: ...

class ListpeersPeersChannelsInflight(_message.Message):
    __slots__ = ["feerate", "funding_outnum", "funding_txid", "our_funding_msat", "scratch_txid", "total_funding_msat"]
    FEERATE_FIELD_NUMBER: _ClassVar[int]
    FUNDING_OUTNUM_FIELD_NUMBER: _ClassVar[int]
    FUNDING_TXID_FIELD_NUMBER: _ClassVar[int]
    OUR_FUNDING_MSAT_FIELD_NUMBER: _ClassVar[int]
    SCRATCH_TXID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FUNDING_MSAT_FIELD_NUMBER: _ClassVar[int]
    feerate: str
    funding_outnum: int
    funding_txid: bytes
    our_funding_msat: _primitives_pb2.Amount
    scratch_txid: bytes
    total_funding_msat: _primitives_pb2.Amount
    def __init__(self, funding_txid: _Optional[bytes] = ..., funding_outnum: _Optional[int] = ..., feerate: _Optional[str] = ..., total_funding_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., our_funding_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., scratch_txid: _Optional[bytes] = ...) -> None: ...

class ListpeersPeersLog(_message.Message):
    __slots__ = ["data", "item_type", "log", "node_id", "num_skipped", "source", "time"]
    class ListpeersPeersLogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BROKEN: ListpeersPeersLog.ListpeersPeersLogType
    DATA_FIELD_NUMBER: _ClassVar[int]
    DEBUG: ListpeersPeersLog.ListpeersPeersLogType
    INFO: ListpeersPeersLog.ListpeersPeersLogType
    IO_IN: ListpeersPeersLog.ListpeersPeersLogType
    IO_OUT: ListpeersPeersLog.ListpeersPeersLogType
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED: ListpeersPeersLog.ListpeersPeersLogType
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    UNUSUAL: ListpeersPeersLog.ListpeersPeersLogType
    data: bytes
    item_type: ListpeersPeersLog.ListpeersPeersLogType
    log: str
    node_id: bytes
    num_skipped: int
    source: str
    time: str
    def __init__(self, item_type: _Optional[_Union[ListpeersPeersLog.ListpeersPeersLogType, str]] = ..., num_skipped: _Optional[int] = ..., time: _Optional[str] = ..., source: _Optional[str] = ..., log: _Optional[str] = ..., node_id: _Optional[bytes] = ..., data: _Optional[bytes] = ...) -> None: ...

class ListpeersRequest(_message.Message):
    __slots__ = ["id", "level"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    level: str
    def __init__(self, id: _Optional[bytes] = ..., level: _Optional[str] = ...) -> None: ...

class ListpeersResponse(_message.Message):
    __slots__ = ["peers"]
    PEERS_FIELD_NUMBER: _ClassVar[int]
    peers: _containers.RepeatedCompositeFieldContainer[ListpeersPeers]
    def __init__(self, peers: _Optional[_Iterable[_Union[ListpeersPeers, _Mapping]]] = ...) -> None: ...

class ListsendpaysPayments(_message.Message):
    __slots__ = ["amount_msat", "amount_sent_msat", "bolt11", "bolt12", "created_at", "description", "destination", "erroronion", "groupid", "id", "label", "payment_hash", "payment_preimage", "status"]
    class ListsendpaysPaymentsStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_SENT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: ListsendpaysPayments.ListsendpaysPaymentsStatus
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ERRORONION_FIELD_NUMBER: _ClassVar[int]
    FAILED: ListsendpaysPayments.ListsendpaysPaymentsStatus
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PENDING: ListsendpaysPayments.ListsendpaysPaymentsStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_sent_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    created_at: int
    description: str
    destination: bytes
    erroronion: bytes
    groupid: int
    id: int
    label: str
    payment_hash: bytes
    payment_preimage: bytes
    status: ListsendpaysPayments.ListsendpaysPaymentsStatus
    def __init__(self, id: _Optional[int] = ..., groupid: _Optional[int] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[ListsendpaysPayments.ListsendpaysPaymentsStatus, str]] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., destination: _Optional[bytes] = ..., created_at: _Optional[int] = ..., amount_sent_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., label: _Optional[str] = ..., bolt11: _Optional[str] = ..., description: _Optional[str] = ..., bolt12: _Optional[str] = ..., payment_preimage: _Optional[bytes] = ..., erroronion: _Optional[bytes] = ...) -> None: ...

class ListsendpaysRequest(_message.Message):
    __slots__ = ["bolt11", "payment_hash", "status"]
    class ListsendpaysStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: ListsendpaysRequest.ListsendpaysStatus
    FAILED: ListsendpaysRequest.ListsendpaysStatus
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PENDING: ListsendpaysRequest.ListsendpaysStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    bolt11: str
    payment_hash: bytes
    status: ListsendpaysRequest.ListsendpaysStatus
    def __init__(self, bolt11: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[ListsendpaysRequest.ListsendpaysStatus, str]] = ...) -> None: ...

class ListsendpaysResponse(_message.Message):
    __slots__ = ["payments"]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    payments: _containers.RepeatedCompositeFieldContainer[ListsendpaysPayments]
    def __init__(self, payments: _Optional[_Iterable[_Union[ListsendpaysPayments, _Mapping]]] = ...) -> None: ...

class ListtransactionsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListtransactionsResponse(_message.Message):
    __slots__ = ["transactions"]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[ListtransactionsTransactions]
    def __init__(self, transactions: _Optional[_Iterable[_Union[ListtransactionsTransactions, _Mapping]]] = ...) -> None: ...

class ListtransactionsTransactions(_message.Message):
    __slots__ = ["blockheight", "channel", "hash", "inputs", "locktime", "outputs", "rawtx", "txindex", "version"]
    BLOCKHEIGHT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    LOCKTIME_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    RAWTX_FIELD_NUMBER: _ClassVar[int]
    TXINDEX_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    blockheight: int
    channel: str
    hash: bytes
    inputs: _containers.RepeatedCompositeFieldContainer[ListtransactionsTransactionsInputs]
    locktime: int
    outputs: _containers.RepeatedCompositeFieldContainer[ListtransactionsTransactionsOutputs]
    rawtx: bytes
    txindex: int
    version: int
    def __init__(self, hash: _Optional[bytes] = ..., rawtx: _Optional[bytes] = ..., blockheight: _Optional[int] = ..., txindex: _Optional[int] = ..., channel: _Optional[str] = ..., locktime: _Optional[int] = ..., version: _Optional[int] = ..., inputs: _Optional[_Iterable[_Union[ListtransactionsTransactionsInputs, _Mapping]]] = ..., outputs: _Optional[_Iterable[_Union[ListtransactionsTransactionsOutputs, _Mapping]]] = ...) -> None: ...

class ListtransactionsTransactionsInputs(_message.Message):
    __slots__ = ["channel", "index", "item_type", "sequence", "txid"]
    class ListtransactionsTransactionsInputsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FUNDING: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    CHANNEL_HTLC_SUCCESS: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    CHANNEL_HTLC_TIMEOUT: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    CHANNEL_MUTUAL_CLOSE: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    CHANNEL_PENALTY: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    CHANNEL_SWEEP: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    CHANNEL_UNILATERAL_CHEAT: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    CHANNEL_UNILATERAL_CLOSE: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    DEPOSIT: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    THEIRS: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    TXID_FIELD_NUMBER: _ClassVar[int]
    WITHDRAW: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    channel: str
    index: int
    item_type: ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType
    sequence: int
    txid: bytes
    def __init__(self, txid: _Optional[bytes] = ..., index: _Optional[int] = ..., sequence: _Optional[int] = ..., item_type: _Optional[_Union[ListtransactionsTransactionsInputs.ListtransactionsTransactionsInputsType, str]] = ..., channel: _Optional[str] = ...) -> None: ...

class ListtransactionsTransactionsOutputs(_message.Message):
    __slots__ = ["amount_msat", "channel", "index", "item_type", "scriptPubKey"]
    class ListtransactionsTransactionsOutputsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FUNDING: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    CHANNEL_HTLC_SUCCESS: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    CHANNEL_HTLC_TIMEOUT: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    CHANNEL_MUTUAL_CLOSE: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    CHANNEL_PENALTY: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    CHANNEL_SWEEP: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    CHANNEL_UNILATERAL_CHEAT: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    CHANNEL_UNILATERAL_CLOSE: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    DEPOSIT: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCRIPTPUBKEY_FIELD_NUMBER: _ClassVar[int]
    THEIRS: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    WITHDRAW: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    amount_msat: _primitives_pb2.Amount
    channel: str
    index: int
    item_type: ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType
    scriptPubKey: bytes
    def __init__(self, index: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., scriptPubKey: _Optional[bytes] = ..., item_type: _Optional[_Union[ListtransactionsTransactionsOutputs.ListtransactionsTransactionsOutputsType, str]] = ..., channel: _Optional[str] = ...) -> None: ...

class NewaddrRequest(_message.Message):
    __slots__ = ["addresstype"]
    class NewaddrAddresstype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ADDRESSTYPE_FIELD_NUMBER: _ClassVar[int]
    ALL: NewaddrRequest.NewaddrAddresstype
    BECH32: NewaddrRequest.NewaddrAddresstype
    P2SH_SEGWIT: NewaddrRequest.NewaddrAddresstype
    addresstype: NewaddrRequest.NewaddrAddresstype
    def __init__(self, addresstype: _Optional[_Union[NewaddrRequest.NewaddrAddresstype, str]] = ...) -> None: ...

class NewaddrResponse(_message.Message):
    __slots__ = ["bech32", "p2sh_segwit"]
    BECH32_FIELD_NUMBER: _ClassVar[int]
    P2SH_SEGWIT_FIELD_NUMBER: _ClassVar[int]
    bech32: str
    p2sh_segwit: str
    def __init__(self, bech32: _Optional[str] = ..., p2sh_segwit: _Optional[str] = ...) -> None: ...

class PayRequest(_message.Message):
    __slots__ = ["amount_msat", "bolt11", "description", "exclude", "exemptfee", "label", "localinvreqid", "maxdelay", "maxfee", "maxfeepercent", "retry_for", "riskfactor"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    EXEMPTFEE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCALINVREQID_FIELD_NUMBER: _ClassVar[int]
    MAXDELAY_FIELD_NUMBER: _ClassVar[int]
    MAXFEEPERCENT_FIELD_NUMBER: _ClassVar[int]
    MAXFEE_FIELD_NUMBER: _ClassVar[int]
    RETRY_FOR_FIELD_NUMBER: _ClassVar[int]
    RISKFACTOR_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    bolt11: str
    description: str
    exclude: _containers.RepeatedScalarFieldContainer[str]
    exemptfee: _primitives_pb2.Amount
    label: str
    localinvreqid: bytes
    maxdelay: int
    maxfee: _primitives_pb2.Amount
    maxfeepercent: float
    retry_for: int
    riskfactor: float
    def __init__(self, bolt11: _Optional[str] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., label: _Optional[str] = ..., riskfactor: _Optional[float] = ..., maxfeepercent: _Optional[float] = ..., retry_for: _Optional[int] = ..., maxdelay: _Optional[int] = ..., exemptfee: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., localinvreqid: _Optional[bytes] = ..., exclude: _Optional[_Iterable[str]] = ..., maxfee: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...

class PayResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_sent_msat", "created_at", "destination", "parts", "payment_hash", "payment_preimage", "status", "warning_partial_completion"]
    class PayStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_SENT_MSAT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: PayResponse.PayStatus
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FAILED: PayResponse.PayStatus
    PARTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PENDING: PayResponse.PayStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WARNING_PARTIAL_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_sent_msat: _primitives_pb2.Amount
    created_at: float
    destination: bytes
    parts: int
    payment_hash: bytes
    payment_preimage: bytes
    status: PayResponse.PayStatus
    warning_partial_completion: str
    def __init__(self, payment_preimage: _Optional[bytes] = ..., destination: _Optional[bytes] = ..., payment_hash: _Optional[bytes] = ..., created_at: _Optional[float] = ..., parts: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., amount_sent_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., warning_partial_completion: _Optional[str] = ..., status: _Optional[_Union[PayResponse.PayStatus, str]] = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ["id", "len", "pongbytes"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEN_FIELD_NUMBER: _ClassVar[int]
    PONGBYTES_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    len: float
    pongbytes: float
    def __init__(self, id: _Optional[bytes] = ..., len: _Optional[float] = ..., pongbytes: _Optional[float] = ...) -> None: ...

class PingResponse(_message.Message):
    __slots__ = ["totlen"]
    TOTLEN_FIELD_NUMBER: _ClassVar[int]
    totlen: int
    def __init__(self, totlen: _Optional[int] = ...) -> None: ...

class SendonionFirst_hop(_message.Message):
    __slots__ = ["amount_msat", "delay", "id"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    delay: int
    id: bytes
    def __init__(self, id: _Optional[bytes] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., delay: _Optional[int] = ...) -> None: ...

class SendonionRequest(_message.Message):
    __slots__ = ["amount_msat", "bolt11", "destination", "groupid", "label", "localinvreqid", "onion", "partid", "payment_hash", "shared_secrets"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCALINVREQID_FIELD_NUMBER: _ClassVar[int]
    ONION_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    SHARED_SECRETS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    bolt11: str
    destination: bytes
    groupid: int
    label: str
    localinvreqid: bytes
    onion: bytes
    partid: int
    payment_hash: bytes
    shared_secrets: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, onion: _Optional[bytes] = ..., payment_hash: _Optional[bytes] = ..., label: _Optional[str] = ..., shared_secrets: _Optional[_Iterable[bytes]] = ..., partid: _Optional[int] = ..., bolt11: _Optional[str] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., destination: _Optional[bytes] = ..., localinvreqid: _Optional[bytes] = ..., groupid: _Optional[int] = ...) -> None: ...

class SendonionResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_sent_msat", "bolt11", "bolt12", "created_at", "destination", "id", "label", "message", "partid", "payment_hash", "payment_preimage", "status"]
    class SendonionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_SENT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: SendonionResponse.SendonionStatus
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PENDING: SendonionResponse.SendonionStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_sent_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    created_at: int
    destination: bytes
    id: int
    label: str
    message: str
    partid: int
    payment_hash: bytes
    payment_preimage: bytes
    status: SendonionResponse.SendonionStatus
    def __init__(self, id: _Optional[int] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[SendonionResponse.SendonionStatus, str]] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., destination: _Optional[bytes] = ..., created_at: _Optional[int] = ..., amount_sent_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., label: _Optional[str] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., partid: _Optional[int] = ..., payment_preimage: _Optional[bytes] = ..., message: _Optional[str] = ...) -> None: ...

class SendpayRequest(_message.Message):
    __slots__ = ["amount_msat", "bolt11", "groupid", "label", "localinvreqid", "partid", "payment_hash", "payment_secret", "route"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LOCALINVREQID_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    bolt11: str
    groupid: int
    label: str
    localinvreqid: bytes
    partid: int
    payment_hash: bytes
    payment_secret: bytes
    route: _containers.RepeatedCompositeFieldContainer[SendpayRoute]
    def __init__(self, route: _Optional[_Iterable[_Union[SendpayRoute, _Mapping]]] = ..., payment_hash: _Optional[bytes] = ..., label: _Optional[str] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., bolt11: _Optional[str] = ..., payment_secret: _Optional[bytes] = ..., partid: _Optional[int] = ..., localinvreqid: _Optional[bytes] = ..., groupid: _Optional[int] = ...) -> None: ...

class SendpayResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_sent_msat", "bolt11", "bolt12", "completed_at", "created_at", "destination", "groupid", "id", "label", "message", "partid", "payment_hash", "payment_preimage", "status"]
    class SendpayStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_SENT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: SendpayResponse.SendpayStatus
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PENDING: SendpayResponse.SendpayStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_sent_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    completed_at: int
    created_at: int
    destination: bytes
    groupid: int
    id: int
    label: str
    message: str
    partid: int
    payment_hash: bytes
    payment_preimage: bytes
    status: SendpayResponse.SendpayStatus
    def __init__(self, id: _Optional[int] = ..., groupid: _Optional[int] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[SendpayResponse.SendpayStatus, str]] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., destination: _Optional[bytes] = ..., created_at: _Optional[int] = ..., completed_at: _Optional[int] = ..., amount_sent_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., label: _Optional[str] = ..., partid: _Optional[int] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., payment_preimage: _Optional[bytes] = ..., message: _Optional[str] = ...) -> None: ...

class SendpayRoute(_message.Message):
    __slots__ = ["amount_msat", "channel", "delay", "id"]
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    channel: str
    delay: int
    id: bytes
    def __init__(self, amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., id: _Optional[bytes] = ..., delay: _Optional[int] = ..., channel: _Optional[str] = ...) -> None: ...

class SendpsbtRequest(_message.Message):
    __slots__ = ["psbt", "reserve"]
    PSBT_FIELD_NUMBER: _ClassVar[int]
    RESERVE_FIELD_NUMBER: _ClassVar[int]
    psbt: str
    reserve: bool
    def __init__(self, psbt: _Optional[str] = ..., reserve: bool = ...) -> None: ...

class SendpsbtResponse(_message.Message):
    __slots__ = ["tx", "txid"]
    TXID_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    tx: bytes
    txid: bytes
    def __init__(self, tx: _Optional[bytes] = ..., txid: _Optional[bytes] = ...) -> None: ...

class SetchannelChannels(_message.Message):
    __slots__ = ["channel_id", "fee_base_msat", "fee_proportional_millionths", "maximum_htlc_out_msat", "minimum_htlc_out_msat", "peer_id", "short_channel_id", "warning_htlcmax_too_high", "warning_htlcmin_too_low"]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    FEE_BASE_MSAT_FIELD_NUMBER: _ClassVar[int]
    FEE_PROPORTIONAL_MILLIONTHS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_HTLC_OUT_MSAT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_HTLC_OUT_MSAT_FIELD_NUMBER: _ClassVar[int]
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    SHORT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    WARNING_HTLCMAX_TOO_HIGH_FIELD_NUMBER: _ClassVar[int]
    WARNING_HTLCMIN_TOO_LOW_FIELD_NUMBER: _ClassVar[int]
    channel_id: bytes
    fee_base_msat: _primitives_pb2.Amount
    fee_proportional_millionths: int
    maximum_htlc_out_msat: _primitives_pb2.Amount
    minimum_htlc_out_msat: _primitives_pb2.Amount
    peer_id: bytes
    short_channel_id: str
    warning_htlcmax_too_high: str
    warning_htlcmin_too_low: str
    def __init__(self, peer_id: _Optional[bytes] = ..., channel_id: _Optional[bytes] = ..., short_channel_id: _Optional[str] = ..., fee_base_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., fee_proportional_millionths: _Optional[int] = ..., minimum_htlc_out_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., warning_htlcmin_too_low: _Optional[str] = ..., maximum_htlc_out_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., warning_htlcmax_too_high: _Optional[str] = ...) -> None: ...

class SetchannelRequest(_message.Message):
    __slots__ = ["enforcedelay", "feebase", "feeppm", "htlcmax", "htlcmin", "id"]
    ENFORCEDELAY_FIELD_NUMBER: _ClassVar[int]
    FEEBASE_FIELD_NUMBER: _ClassVar[int]
    FEEPPM_FIELD_NUMBER: _ClassVar[int]
    HTLCMAX_FIELD_NUMBER: _ClassVar[int]
    HTLCMIN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    enforcedelay: int
    feebase: _primitives_pb2.Amount
    feeppm: int
    htlcmax: _primitives_pb2.Amount
    htlcmin: _primitives_pb2.Amount
    id: str
    def __init__(self, id: _Optional[str] = ..., feebase: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., feeppm: _Optional[int] = ..., htlcmin: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., htlcmax: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., enforcedelay: _Optional[int] = ...) -> None: ...

class SetchannelResponse(_message.Message):
    __slots__ = ["channels"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[SetchannelChannels]
    def __init__(self, channels: _Optional[_Iterable[_Union[SetchannelChannels, _Mapping]]] = ...) -> None: ...

class SignmessageRequest(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class SignmessageResponse(_message.Message):
    __slots__ = ["recid", "signature", "zbase"]
    RECID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ZBASE_FIELD_NUMBER: _ClassVar[int]
    recid: bytes
    signature: bytes
    zbase: str
    def __init__(self, signature: _Optional[bytes] = ..., recid: _Optional[bytes] = ..., zbase: _Optional[str] = ...) -> None: ...

class SignpsbtRequest(_message.Message):
    __slots__ = ["psbt", "signonly"]
    PSBT_FIELD_NUMBER: _ClassVar[int]
    SIGNONLY_FIELD_NUMBER: _ClassVar[int]
    psbt: str
    signonly: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, psbt: _Optional[str] = ..., signonly: _Optional[_Iterable[int]] = ...) -> None: ...

class SignpsbtResponse(_message.Message):
    __slots__ = ["signed_psbt"]
    SIGNED_PSBT_FIELD_NUMBER: _ClassVar[int]
    signed_psbt: str
    def __init__(self, signed_psbt: _Optional[str] = ...) -> None: ...

class StopRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StopResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TxdiscardRequest(_message.Message):
    __slots__ = ["txid"]
    TXID_FIELD_NUMBER: _ClassVar[int]
    txid: bytes
    def __init__(self, txid: _Optional[bytes] = ...) -> None: ...

class TxdiscardResponse(_message.Message):
    __slots__ = ["txid", "unsigned_tx"]
    TXID_FIELD_NUMBER: _ClassVar[int]
    UNSIGNED_TX_FIELD_NUMBER: _ClassVar[int]
    txid: bytes
    unsigned_tx: bytes
    def __init__(self, unsigned_tx: _Optional[bytes] = ..., txid: _Optional[bytes] = ...) -> None: ...

class TxprepareRequest(_message.Message):
    __slots__ = ["feerate", "minconf", "outputs", "utxos"]
    FEERATE_FIELD_NUMBER: _ClassVar[int]
    MINCONF_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    UTXOS_FIELD_NUMBER: _ClassVar[int]
    feerate: _primitives_pb2.Feerate
    minconf: int
    outputs: _containers.RepeatedCompositeFieldContainer[_primitives_pb2.OutputDesc]
    utxos: _containers.RepeatedCompositeFieldContainer[_primitives_pb2.Outpoint]
    def __init__(self, outputs: _Optional[_Iterable[_Union[_primitives_pb2.OutputDesc, _Mapping]]] = ..., feerate: _Optional[_Union[_primitives_pb2.Feerate, _Mapping]] = ..., minconf: _Optional[int] = ..., utxos: _Optional[_Iterable[_Union[_primitives_pb2.Outpoint, _Mapping]]] = ...) -> None: ...

class TxprepareResponse(_message.Message):
    __slots__ = ["psbt", "txid", "unsigned_tx"]
    PSBT_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    UNSIGNED_TX_FIELD_NUMBER: _ClassVar[int]
    psbt: str
    txid: bytes
    unsigned_tx: bytes
    def __init__(self, psbt: _Optional[str] = ..., unsigned_tx: _Optional[bytes] = ..., txid: _Optional[bytes] = ...) -> None: ...

class TxsendRequest(_message.Message):
    __slots__ = ["txid"]
    TXID_FIELD_NUMBER: _ClassVar[int]
    txid: bytes
    def __init__(self, txid: _Optional[bytes] = ...) -> None: ...

class TxsendResponse(_message.Message):
    __slots__ = ["psbt", "tx", "txid"]
    PSBT_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    psbt: str
    tx: bytes
    txid: bytes
    def __init__(self, psbt: _Optional[str] = ..., tx: _Optional[bytes] = ..., txid: _Optional[bytes] = ...) -> None: ...

class UtxopsbtRequest(_message.Message):
    __slots__ = ["excess_as_change", "feerate", "locktime", "min_witness_weight", "reserve", "reservedok", "satoshi", "startweight", "utxos"]
    EXCESS_AS_CHANGE_FIELD_NUMBER: _ClassVar[int]
    FEERATE_FIELD_NUMBER: _ClassVar[int]
    LOCKTIME_FIELD_NUMBER: _ClassVar[int]
    MIN_WITNESS_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RESERVEDOK_FIELD_NUMBER: _ClassVar[int]
    RESERVE_FIELD_NUMBER: _ClassVar[int]
    SATOSHI_FIELD_NUMBER: _ClassVar[int]
    STARTWEIGHT_FIELD_NUMBER: _ClassVar[int]
    UTXOS_FIELD_NUMBER: _ClassVar[int]
    excess_as_change: bool
    feerate: _primitives_pb2.Feerate
    locktime: int
    min_witness_weight: int
    reserve: int
    reservedok: bool
    satoshi: _primitives_pb2.Amount
    startweight: int
    utxos: _containers.RepeatedCompositeFieldContainer[_primitives_pb2.Outpoint]
    def __init__(self, satoshi: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., feerate: _Optional[_Union[_primitives_pb2.Feerate, _Mapping]] = ..., startweight: _Optional[int] = ..., utxos: _Optional[_Iterable[_Union[_primitives_pb2.Outpoint, _Mapping]]] = ..., reserve: _Optional[int] = ..., reservedok: bool = ..., locktime: _Optional[int] = ..., min_witness_weight: _Optional[int] = ..., excess_as_change: bool = ...) -> None: ...

class UtxopsbtReservations(_message.Message):
    __slots__ = ["reserved", "reserved_to_block", "txid", "vout", "was_reserved"]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    RESERVED_TO_BLOCK_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    VOUT_FIELD_NUMBER: _ClassVar[int]
    WAS_RESERVED_FIELD_NUMBER: _ClassVar[int]
    reserved: bool
    reserved_to_block: int
    txid: bytes
    vout: int
    was_reserved: bool
    def __init__(self, txid: _Optional[bytes] = ..., vout: _Optional[int] = ..., was_reserved: bool = ..., reserved: bool = ..., reserved_to_block: _Optional[int] = ...) -> None: ...

class UtxopsbtResponse(_message.Message):
    __slots__ = ["change_outnum", "estimated_final_weight", "excess_msat", "feerate_per_kw", "psbt", "reservations"]
    CHANGE_OUTNUM_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_FINAL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXCESS_MSAT_FIELD_NUMBER: _ClassVar[int]
    FEERATE_PER_KW_FIELD_NUMBER: _ClassVar[int]
    PSBT_FIELD_NUMBER: _ClassVar[int]
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    change_outnum: int
    estimated_final_weight: int
    excess_msat: _primitives_pb2.Amount
    feerate_per_kw: int
    psbt: str
    reservations: _containers.RepeatedCompositeFieldContainer[UtxopsbtReservations]
    def __init__(self, psbt: _Optional[str] = ..., feerate_per_kw: _Optional[int] = ..., estimated_final_weight: _Optional[int] = ..., excess_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., change_outnum: _Optional[int] = ..., reservations: _Optional[_Iterable[_Union[UtxopsbtReservations, _Mapping]]] = ...) -> None: ...

class WaitanyinvoiceRequest(_message.Message):
    __slots__ = ["lastpay_index", "timeout"]
    LASTPAY_INDEX_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    lastpay_index: int
    timeout: int
    def __init__(self, lastpay_index: _Optional[int] = ..., timeout: _Optional[int] = ...) -> None: ...

class WaitanyinvoiceResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_received_msat", "bolt11", "bolt12", "description", "expires_at", "label", "paid_at", "pay_index", "payment_hash", "payment_preimage", "status"]
    class WaitanyinvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_RECEIVED_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED: WaitanyinvoiceResponse.WaitanyinvoiceStatus
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PAID: WaitanyinvoiceResponse.WaitanyinvoiceStatus
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PAY_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_received_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    description: str
    expires_at: int
    label: str
    paid_at: int
    pay_index: int
    payment_hash: bytes
    payment_preimage: bytes
    status: WaitanyinvoiceResponse.WaitanyinvoiceStatus
    def __init__(self, label: _Optional[str] = ..., description: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[WaitanyinvoiceResponse.WaitanyinvoiceStatus, str]] = ..., expires_at: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., pay_index: _Optional[int] = ..., amount_received_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., paid_at: _Optional[int] = ..., payment_preimage: _Optional[bytes] = ...) -> None: ...

class WaitinvoiceRequest(_message.Message):
    __slots__ = ["label"]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    label: str
    def __init__(self, label: _Optional[str] = ...) -> None: ...

class WaitinvoiceResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_received_msat", "bolt11", "bolt12", "description", "expires_at", "label", "paid_at", "pay_index", "payment_hash", "payment_preimage", "status"]
    class WaitinvoiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_RECEIVED_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRED: WaitinvoiceResponse.WaitinvoiceStatus
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PAID: WaitinvoiceResponse.WaitinvoiceStatus
    PAID_AT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    PAY_INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_received_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    description: str
    expires_at: int
    label: str
    paid_at: int
    pay_index: int
    payment_hash: bytes
    payment_preimage: bytes
    status: WaitinvoiceResponse.WaitinvoiceStatus
    def __init__(self, label: _Optional[str] = ..., description: _Optional[str] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[WaitinvoiceResponse.WaitinvoiceStatus, str]] = ..., expires_at: _Optional[int] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., pay_index: _Optional[int] = ..., amount_received_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., paid_at: _Optional[int] = ..., payment_preimage: _Optional[bytes] = ...) -> None: ...

class WaitsendpayRequest(_message.Message):
    __slots__ = ["groupid", "partid", "payment_hash", "timeout"]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    groupid: int
    partid: int
    payment_hash: bytes
    timeout: int
    def __init__(self, payment_hash: _Optional[bytes] = ..., timeout: _Optional[int] = ..., partid: _Optional[int] = ..., groupid: _Optional[int] = ...) -> None: ...

class WaitsendpayResponse(_message.Message):
    __slots__ = ["amount_msat", "amount_sent_msat", "bolt11", "bolt12", "completed_at", "created_at", "destination", "groupid", "id", "label", "partid", "payment_hash", "payment_preimage", "status"]
    class WaitsendpayStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AMOUNT_MSAT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_SENT_MSAT_FIELD_NUMBER: _ClassVar[int]
    BOLT11_FIELD_NUMBER: _ClassVar[int]
    BOLT12_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: WaitsendpayResponse.WaitsendpayStatus
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    PARTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_HASH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PREIMAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    amount_msat: _primitives_pb2.Amount
    amount_sent_msat: _primitives_pb2.Amount
    bolt11: str
    bolt12: str
    completed_at: float
    created_at: int
    destination: bytes
    groupid: int
    id: int
    label: str
    partid: int
    payment_hash: bytes
    payment_preimage: bytes
    status: WaitsendpayResponse.WaitsendpayStatus
    def __init__(self, id: _Optional[int] = ..., groupid: _Optional[int] = ..., payment_hash: _Optional[bytes] = ..., status: _Optional[_Union[WaitsendpayResponse.WaitsendpayStatus, str]] = ..., amount_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., destination: _Optional[bytes] = ..., created_at: _Optional[int] = ..., completed_at: _Optional[float] = ..., amount_sent_msat: _Optional[_Union[_primitives_pb2.Amount, _Mapping]] = ..., label: _Optional[str] = ..., partid: _Optional[int] = ..., bolt11: _Optional[str] = ..., bolt12: _Optional[str] = ..., payment_preimage: _Optional[bytes] = ...) -> None: ...

class WithdrawRequest(_message.Message):
    __slots__ = ["destination", "feerate", "minconf", "satoshi", "utxos"]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    FEERATE_FIELD_NUMBER: _ClassVar[int]
    MINCONF_FIELD_NUMBER: _ClassVar[int]
    SATOSHI_FIELD_NUMBER: _ClassVar[int]
    UTXOS_FIELD_NUMBER: _ClassVar[int]
    destination: str
    feerate: _primitives_pb2.Feerate
    minconf: int
    satoshi: _primitives_pb2.AmountOrAll
    utxos: _containers.RepeatedCompositeFieldContainer[_primitives_pb2.Outpoint]
    def __init__(self, destination: _Optional[str] = ..., satoshi: _Optional[_Union[_primitives_pb2.AmountOrAll, _Mapping]] = ..., feerate: _Optional[_Union[_primitives_pb2.Feerate, _Mapping]] = ..., minconf: _Optional[int] = ..., utxos: _Optional[_Iterable[_Union[_primitives_pb2.Outpoint, _Mapping]]] = ...) -> None: ...

class WithdrawResponse(_message.Message):
    __slots__ = ["psbt", "tx", "txid"]
    PSBT_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    TX_FIELD_NUMBER: _ClassVar[int]
    psbt: str
    tx: bytes
    txid: bytes
    def __init__(self, tx: _Optional[bytes] = ..., txid: _Optional[bytes] = ..., psbt: _Optional[str] = ...) -> None: ...
