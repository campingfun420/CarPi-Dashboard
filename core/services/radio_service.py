import sys
import json
import time

SERVICE_NAME = "radio"

state = {"volume": 50, "station": "101.1", "muted": False}

def send_event(event_type, payload):
    msg = {"version": 1, "source": SERVICE_NAME, "type": event_type,
           "timestamp": int(time.time()), "payload": payload}
    print(json.dumps(msg), flush=True)

def handle_command(command):
    try:
        cmd_type = command.get("type")
        payload = command.get("payload", {})
        if cmd_type == "SetGear":
            gear = payload.get("gear", "PARK")
            state["muted"] = gear != "PARK"
            send_event("RadioMuted", {"muted": state["muted"]})
        elif cmd_type == "SetVolume":
            vol = payload.get("volume", 50)
            state["volume"] = max(0, min(100, vol))
            send_event("VolumeChanged", {"volume": state["volume"]})
        elif cmd_type == "SetStation":
            station = payload.get("station", "101.1")
            state["station"] = station
            send_event("StationChanged", {"station": state["station"]})
        elif cmd_type == "Mute":
            muted = payload.get("muted", False)
            state["muted"] = muted
            send_event("RadioMuted", {"muted": state["muted"]})
        else:
            send_event("Error", {"message": f"Unknown command {cmd_type}"})
    except Exception as e:
        send_event("Error", {"message": str(e)})

for line in sys.stdin:
    if not line.strip():
        continue
    try:
        command = json.loads(line.strip())
        handle_command(command)
    except Exception as e:
        send_event("Error", {"message": f"Invalid JSON: {e}"})