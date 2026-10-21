"""Signs and verifies webhook payloads with ECDSA (P-256)."""

import hashlib

from ecdsa import NIST256p, BadSignatureError, SigningKey


def new_key() -> SigningKey:
    return SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha256)


def sign(key: SigningKey, payload: bytes) -> bytes:
    return key.sign(payload)


def verify(key: SigningKey, payload: bytes, signature: bytes) -> bool:
    try:
        return key.get_verifying_key().verify(signature, payload)
    except BadSignatureError:
        return False
