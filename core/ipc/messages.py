class IPCMessage:
    def __init__(self, message_type: str, payload: dict, version: int = 1):
        self.message_type = message_type
        self.payload = payload
        self.version = version

    def to_json(self):
        import json
        return json.dumps({
            'message_type': self.message_type,
            'payload': self.payload,
            'version': self.version
        })

    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(data['message_type'], data['payload'], data.get('version', 1))
