import json
import os
from datetime import datetime

LOG_DIR = "logs"

class EventLogger:
    def __init__(self):
        os.makedirs(LOG_DIR, exist_ok=True)
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        self.file_path = os.path.join(LOG_DIR, f"session_{timestamp}.log")
        self.file = open(self.file_path, "a")

    def log(self, event):
        record = {
            "type": event.__class__.__name__,
            "data": event.__dict__,
        }
        self.file.write(json.dumps(record) + "\n")
        self.file.flush()

    def close(self):
        self.file.close()
