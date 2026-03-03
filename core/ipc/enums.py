ALLOWED_GEARS = ['PARK', 'REVERSE', 'NEUTRAL', 'DRIVE']
VOLUME_RANGE = (0, 100)

def validate_enum(value, allowed):
    if value not in allowed:
        raise ValueError(f"Invalid value: {value}. Allowed: {allowed}")

def validate_range(value, min_max):
    min_val, max_val = min_max
    if not (min_val <= value <= max_val):
        raise ValueError(f"Value {value} out of range: {min_val}-{max_val}")
