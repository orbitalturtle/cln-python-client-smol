from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

AwaitingUnilateral: ChannelState
ChanneldAwaitingLockin: ChannelState
ChanneldNormal: ChannelState
ChanneldShuttingDown: ChannelState
ClosingdComplete: ChannelState
ClosingdSigexchange: ChannelState
DESCRIPTOR: _descriptor.FileDescriptor
DualopendAwaitingLockin: ChannelState
DualopendOpenInit: ChannelState
FundingSpendSeen: ChannelState
IN: ChannelSide
OUT: ChannelSide
Onchain: ChannelState
Openingd: ChannelState

class Amount(_message.Message):
    __slots__ = ["msat"]
    MSAT_FIELD_NUMBER: _ClassVar[int]
    msat: int
    def __init__(self, msat: _Optional[int] = ...) -> None: ...

class AmountOrAll(_message.Message):
    __slots__ = ["all", "amount"]
    ALL_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    all: bool
    amount: Amount
    def __init__(self, amount: _Optional[_Union[Amount, _Mapping]] = ..., all: bool = ...) -> None: ...

class AmountOrAny(_message.Message):
    __slots__ = ["amount", "any"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ANY_FIELD_NUMBER: _ClassVar[int]
    amount: Amount
    any: bool
    def __init__(self, amount: _Optional[_Union[Amount, _Mapping]] = ..., any: bool = ...) -> None: ...

class ChannelStateChangeCause(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Feerate(_message.Message):
    __slots__ = ["normal", "perkb", "perkw", "slow", "urgent"]
    NORMAL_FIELD_NUMBER: _ClassVar[int]
    PERKB_FIELD_NUMBER: _ClassVar[int]
    PERKW_FIELD_NUMBER: _ClassVar[int]
    SLOW_FIELD_NUMBER: _ClassVar[int]
    URGENT_FIELD_NUMBER: _ClassVar[int]
    normal: bool
    perkb: int
    perkw: int
    slow: bool
    urgent: bool
    def __init__(self, slow: bool = ..., normal: bool = ..., urgent: bool = ..., perkb: _Optional[int] = ..., perkw: _Optional[int] = ...) -> None: ...

class Outpoint(_message.Message):
    __slots__ = ["outnum", "txid"]
    OUTNUM_FIELD_NUMBER: _ClassVar[int]
    TXID_FIELD_NUMBER: _ClassVar[int]
    outnum: int
    txid: bytes
    def __init__(self, txid: _Optional[bytes] = ..., outnum: _Optional[int] = ...) -> None: ...

class OutputDesc(_message.Message):
    __slots__ = ["address", "amount"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    address: str
    amount: Amount
    def __init__(self, address: _Optional[str] = ..., amount: _Optional[_Union[Amount, _Mapping]] = ...) -> None: ...

class RouteHop(_message.Message):
    __slots__ = ["expirydelta", "feebase", "feeprop", "id", "short_channel_id"]
    EXPIRYDELTA_FIELD_NUMBER: _ClassVar[int]
    FEEBASE_FIELD_NUMBER: _ClassVar[int]
    FEEPROP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SHORT_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    expirydelta: int
    feebase: Amount
    feeprop: int
    id: bytes
    short_channel_id: str
    def __init__(self, id: _Optional[bytes] = ..., short_channel_id: _Optional[str] = ..., feebase: _Optional[_Union[Amount, _Mapping]] = ..., feeprop: _Optional[int] = ..., expirydelta: _Optional[int] = ...) -> None: ...

class Routehint(_message.Message):
    __slots__ = ["hops"]
    HOPS_FIELD_NUMBER: _ClassVar[int]
    hops: _containers.RepeatedCompositeFieldContainer[RouteHop]
    def __init__(self, hops: _Optional[_Iterable[_Union[RouteHop, _Mapping]]] = ...) -> None: ...

class RoutehintList(_message.Message):
    __slots__ = ["hints"]
    HINTS_FIELD_NUMBER: _ClassVar[int]
    hints: _containers.RepeatedCompositeFieldContainer[Routehint]
    def __init__(self, hints: _Optional[_Iterable[_Union[Routehint, _Mapping]]] = ...) -> None: ...

class TlvEntry(_message.Message):
    __slots__ = ["type", "value"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: int
    value: bytes
    def __init__(self, type: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class TlvStream(_message.Message):
    __slots__ = ["entries"]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[TlvEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[TlvEntry, _Mapping]]] = ...) -> None: ...

class ChannelSide(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ChannelState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
