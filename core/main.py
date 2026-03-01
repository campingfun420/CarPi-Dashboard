from core.state.system_state import SystemState, GearState, LayoutState, LayoutProfile
from core.reducers.root_reducer import root_reducer
from core.effects.effect_engine import EffectEngine
from core.events.event_logger import EventLogger
from core.replay import replay_events

def create_initial_state():
    portrait = LayoutProfile("portrait", ["row1", "row2", "row3", "row4"])
    landscape = LayoutProfile("landscape", ["rowA", "rowB"])
    layout = LayoutState("portrait", {"portrait": portrait, "landscape": landscape})
    return SystemState(GearState(), layout)

def boot_system():
    state = create_initial_state()
    effects = EffectEngine()
    state = replay_events(state, root_reducer, effects)
    logger = EventLogger()
    return state, effects, logger
