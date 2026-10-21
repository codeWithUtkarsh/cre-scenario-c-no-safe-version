from app.client import deliver
from app.signing import new_key, sign, verify


def test_round_trip():
    key = new_key()
    assert verify(key, b"payload", sign(key, b"payload"))


def test_tampered_payload_rejected():
    key = new_key()
    assert not verify(key, b"other", sign(key, b"payload"))


def test_deliver_sets_signature_header():
    sent = {}

    class FakeSession:
        def post(self, url, data, headers, timeout):
            sent.update(url=url, headers=headers)
            return "ok"

    assert deliver("https://hooks.example/x", new_key(), b"{}", session=FakeSession()) == "ok"
    assert len(sent["headers"]["X-Signature"]) == 128
