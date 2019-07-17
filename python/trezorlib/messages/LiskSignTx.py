# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .LiskTransactionCommon import LiskTransactionCommon

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class LiskSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 116

    def __init__(
        self,
        address_n: List[int] = None,
        transaction: LiskTransactionCommon = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.transaction = transaction

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('transaction', LiskTransactionCommon, 0),
        }
