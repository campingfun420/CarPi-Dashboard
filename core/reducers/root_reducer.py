from core.state.system_state import SystemState
from core.reducers.gear_reducer import gear_reducer
from core.reducers.layout_reducer import layout_reducer

def root_reducer(state: SystemState, event) -> SystemState:
    new_gear = gear_reducer(state.gear, event)
    new_layout = layout_reducer(state.layout, event, new_gear.gear)
    return SystemState(gear=new_gear, layout=new_layout)
