from core.events.layout_events import ExitMoveMode
from core.effects.layout_effects import save_layout_profile

class EffectEngine:
    def __init__(self):
        self.replay_mode = False

    def set_replay_mode(self, mode: bool):
        self.replay_mode = mode

    def handle(self, old_state, new_state, event):
        if self.replay_mode:
            return
        if isinstance(event, ExitMoveMode):
            save_layout_profile(new_state.layout)
