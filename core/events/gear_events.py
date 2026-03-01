from core.events.base import Event

class SetGear(Event):
    def __init__(self, gear: str):
        self.gear = gear
