import glob
import json
from core.events.event_factory import event_from_record

def get_latest_log():
    files = glob.glob("logs/session_*.log")
    if not files:
        return None
    return max(files)

def replay_events(initial_state, reducer, effect_engine):
    log_file = get_latest_log()
    if not log_file:
        return initial_state
    effect_engine.set_replay_mode(True)
    state = initial_state
    with open(log_file, "r") as f:
        for line in f:
            record = json.loads(line.strip())
            event = event_from_record(record)
            if event:
                state = reducer(state, event)
    effect_engine.set_replay_mode(False)
    return state
