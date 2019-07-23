from trezor.crypto import hashlib, hmac, random

from apps.common import storage

_cached_seed = None
_cached_passphrase = None
_cached_passphrase_fprint = b"\x00\x00\x00\x00"


def get_state(prev_state: bytes = None, passphrase: str = None) -> bytes:
    if prev_state is None:
        salt = random.bytes(32)  # generate a random salt if no state provided
    else:
        salt = prev_state[:32]  # use salt from provided state
        if len(salt) != 32:
            return None  # invalid state
    if passphrase is None:
        if _cached_passphrase is None:
            return None  # we don't have any passphrase to compute the state
        else:
            passphrase = _cached_passphrase  # use cached passphrase
    return _compute_state(salt, passphrase)


def _compute_state(salt: bytes, passphrase: str) -> bytes:
    # state = HMAC(passphrase, salt || device_id)
    message = salt + storage.device.get_device_id().encode()
    state = hmac.new(passphrase.encode(), message, hashlib.sha256).digest()
    return salt + state


def get_seed():
    return _cached_seed


def get_passphrase():
    return _cached_passphrase


def get_passphrase_fprint():
    return _cached_passphrase_fprint


def has_passphrase():
    return _cached_passphrase is not None


def set_seed(seed):
    global _cached_seed
    _cached_seed = seed


def set_passphrase(passphrase):
    global _cached_passphrase, _cached_passphrase_fprint
    _cached_passphrase = passphrase
    _cached_passphrase_fprint = _compute_state(b"FPRINT", passphrase or "")[:4]


def clear(keep_passphrase: bool = False):
    set_seed(None)
    if not keep_passphrase:
        set_passphrase(None)
