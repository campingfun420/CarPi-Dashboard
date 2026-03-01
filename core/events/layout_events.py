from core.events.base import Event

class SetOrientation(Event):
    def __init__(self, orientation: str):
        self.orientation = orientation

class EnterMoveMode(Event):
    def __init__(self, row_id: str):
        self.row_id = row_id

class SwapRows(Event):
    def __init__(self, row_a: str, row_b: str):
        self.row_a = row_a
        self.row_b = row_b

class ExitMoveMode(Event):
    def __init__(self, row_id: str):
        self.row_id = row_id
