# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class TezosGetAddress(p.MessageType):
    MESSAGE_WIRE_TYPE = 150

    def __init__(
        self,
        address_n: List[int] = None,
        show_display: bool = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.show_display = show_display

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('show_display', p.BoolType, 0),
        }
