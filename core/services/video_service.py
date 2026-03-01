import sys
import json
import time

SERVICE_NAME = "video"

def send_event(event_type, payload):
    msg = {"version": 1, "source": SERVICE_NAME, "type": event_type,
           "timestamp": int(time.time()), "payload": payload}
    print(json.dumps(msg), flush=True)

for line in sys.stdin:
    if not line.strip():
        continue
    try:
        command = json.loads(line.strip())
        if command['type'] == 'SetOrientation':
            orientation = command['payload'].get('orientation','portrait')
            send_event('VideoOrientationChanged', {'orientation': orientation})
    except Exception as e:
        send_event("Error", {"message": str(e)})
