from core.state.system_state import SystemState
from core.ipc.dispatcher import Dispatcher

if __name__ == '__main__':
    state = SystemState()
    dispatcher = Dispatcher()
    dispatcher.start()

    print("CarPi-Dashboard Core Running")
