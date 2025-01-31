"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SendPackedVirtualTouchEventMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    # Corresponds to "phase" in data
    class Phase(_Phase, metaclass=_PhaseEnumTypeWrapper):
        pass
    class _Phase:
        V = typing.NewType('V', builtins.int)
    class _PhaseEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Phase.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        Began = SendPackedVirtualTouchEventMessage.Phase.V(1)
        Moved = SendPackedVirtualTouchEventMessage.Phase.V(2)
        Stationary = SendPackedVirtualTouchEventMessage.Phase.V(3)
        Ended = SendPackedVirtualTouchEventMessage.Phase.V(4)
        Cancelled = SendPackedVirtualTouchEventMessage.Phase.V(5)

    Began = SendPackedVirtualTouchEventMessage.Phase.V(1)
    Moved = SendPackedVirtualTouchEventMessage.Phase.V(2)
    Stationary = SendPackedVirtualTouchEventMessage.Phase.V(3)
    Ended = SendPackedVirtualTouchEventMessage.Phase.V(4)
    Cancelled = SendPackedVirtualTouchEventMessage.Phase.V(5)

    DATA_FIELD_NUMBER: builtins.int
    # The packed version of VirtualTouchEvent contains X, Y, phase, deviceID
    # and finger stored as a byte array. Each value is written as 16bit little
    # endian integers.
    data: builtins.bytes = ...
    def __init__(self,
        *,
        data : typing.Optional[builtins.bytes] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"data",b"data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"data",b"data"]) -> None: ...
global___SendPackedVirtualTouchEventMessage = SendPackedVirtualTouchEventMessage

sendPackedVirtualTouchEventMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___SendPackedVirtualTouchEventMessage] = ...
