import subprocess
import json
import time

# Path to the radio service script
RADIO_SERVICE_PATH = 'core/services/radio_service.py'

# Start Radio service subprocess
radio_proc = subprocess.Popen(
    ['python3', RADIO_SERVICE_PATH],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

def send_command(cmd_type, payload):
    msg = {
        'version': 1,
        'source': 'core',
        'type': cmd_type,
        'timestamp': int(time.time()),
        'payload': payload
    }
    radio_proc.stdin.write(json.dumps(msg) + "\n")
    radio_proc.stdin.flush()

def read_event(timeout=0.5):
    """Read a line from Radio service stdout"""
    start = time.time()
    while True:
        line = radio_proc.stdout.readline()
        if line:
            return json.loads(line.strip())
        if time.time() - start > timeout:
            return None

# === Example: Test sequence ===
send_command('SetGear', {'gear': 'DRIVE'})
event = read_event()
print("Received Event:", event)

send_command('SetGear', {'gear': 'PARK'})
event = read_event()
print("Received Event:", event)

# Close subprocess
radio_proc.terminate()
radio_proc.wait()
