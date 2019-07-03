# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroTransactionSetInputAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 504

    def __init__(
        self,
        vini: bytes = None,
        vini_hmac: bytes = None,
        pseudo_out: bytes = None,
        pseudo_out_hmac: bytes = None,
        pseudo_out_alpha: bytes = None,
        spend_key: bytes = None,
    ) -> None:
        self.vini = vini
        self.vini_hmac = vini_hmac
        self.pseudo_out = pseudo_out
        self.pseudo_out_hmac = pseudo_out_hmac
        self.pseudo_out_alpha = pseudo_out_alpha
        self.spend_key = spend_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('vini', p.BytesType, 0),
            2: ('vini_hmac', p.BytesType, 0),
            3: ('pseudo_out', p.BytesType, 0),
            4: ('pseudo_out_hmac', p.BytesType, 0),
            5: ('pseudo_out_alpha', p.BytesType, 0),
            6: ('spend_key', p.BytesType, 0),
        }
