from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass(frozen=True)
class GearState:
    gear: str = "PARK"

@dataclass(frozen=True)
class LayoutProfile:
    orientation: str
    row_order: List[str]

@dataclass(frozen=True)
class LayoutState:
    active_orientation: str
    profiles: Dict[str, LayoutProfile]
    move_mode_row: Optional[str] = None

@dataclass(frozen=True)
class SystemState:
    gear: GearState
    layout: LayoutState
