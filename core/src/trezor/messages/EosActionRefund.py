# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class EosActionRefund(p.MessageType):

    def __init__(
        self,
        owner: int = None,
    ) -> None:
        self.owner = owner

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('owner', p.UVarintType, 0),
        }
