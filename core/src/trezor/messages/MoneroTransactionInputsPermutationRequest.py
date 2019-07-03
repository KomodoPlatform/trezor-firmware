# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroTransactionInputsPermutationRequest(p.MessageType):
    MESSAGE_WIRE_TYPE = 505

    def __init__(
        self,
        perm: List[int] = None,
    ) -> None:
        self.perm = perm if perm is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('perm', p.UVarintType, p.FLAG_REPEATED),
        }
