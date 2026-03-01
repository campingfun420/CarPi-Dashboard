from core.events.gear_events import SetGear
from core.events.layout_events import SetOrientation, EnterMoveMode, SwapRows, ExitMoveMode

EVENT_MAP = {
    "SetGear": SetGear,
    "SetOrientation": SetOrientation,
    "EnterMoveMode": EnterMoveMode,
    "SwapRows": SwapRows,
    "ExitMoveMode": ExitMoveMode,
}

def event_from_record(record):
    event_type = record["type"]
    data = record["data"]
    if event_type in EVENT_MAP:
        return EVENT_MAP[event_type](**data)
    return None
