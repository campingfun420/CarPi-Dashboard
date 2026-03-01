from core.state.system_state import GearState
from core.events.gear_events import SetGear

def gear_reducer(state: GearState, event):
    if isinstance(event, SetGear):
        return GearState(gear=event.gear)
    return state
