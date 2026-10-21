"""Delivers signed webhooks."""

import requests

from app.signing import sign


def deliver(url: str, key, payload: bytes, session=None):
    session = session or requests.Session()
    return session.post(url, data=payload, headers={"X-Signature": sign(key, payload).hex()}, timeout=10)
