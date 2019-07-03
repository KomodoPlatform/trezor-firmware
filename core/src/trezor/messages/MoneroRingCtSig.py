# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroRingCtSig(p.MessageType):

    def __init__(
        self,
        txn_fee: int = None,
        message: bytes = None,
        rv_type: int = None,
    ) -> None:
        self.txn_fee = txn_fee
        self.message = message
        self.rv_type = rv_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('txn_fee', p.UVarintType, 0),
            2: ('message', p.BytesType, 0),
            3: ('rv_type', p.UVarintType, 0),
        }
