# Simple test harness for IPC messages
from core.ipc.messages import IPCMessage

def test_set_gear():
    msg = IPCMessage('SetGear', {'gear': 'DRIVE'})
    print(msg.to_json())

if __name__ == '__main__':
    test_set_gear()
