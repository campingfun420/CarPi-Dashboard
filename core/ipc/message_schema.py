from core.ipc.enums import validate_enum, validate_range, ALLOWED_GEARS, VOLUME_RANGE

class SetGearPayload:
    def __init__(self, gear: str):
        validate_enum(gear, ALLOWED_GEARS)
        self.gear = gear

class RadioMutedPayload:
    def __init__(self, muted: bool):
        if not isinstance(muted, bool):
            raise ValueError(f"muted must be bool, got {type(muted)}")
        self.muted = muted
