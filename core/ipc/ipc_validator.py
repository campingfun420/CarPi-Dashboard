import json
from core.events.event_factory import EVENT_MAP

PROTOCOL_VERSION = 1
REGISTERED_SERVICES = {"radio", "video", "network"}

class IPCValidator:
    @staticmethod
    def validate(raw_message: str):
        try:
            msg = json.loads(raw_message)
        except json.JSONDecodeError:
            raise ValueError("Malformed JSON")
        if msg.get("version") != PROTOCOL_VERSION:
            raise ValueError("Protocol version mismatch")
        if msg.get("source") not in REGISTERED_SERVICES:
            raise ValueError("Unknown service source")
        event_type = msg.get("type")
        if event_type not in EVENT_MAP:
            raise ValueError(f"Unknown event type: {event_type}")
        payload = msg.get("payload")
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dict")
        event_cls = EVENT_MAP[event_type]
        try:
            event_cls(**payload)
        except TypeError as e:
            raise ValueError(f"Payload does not match event signature: {e}")
        return True