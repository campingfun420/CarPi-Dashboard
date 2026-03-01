@dataclass(frozen=True)
class ModuleLayout:
    module_id: str
    x_percent: float
    y_percent: float
    width_percent: float
    height_percent: float

@dataclass(frozen=True)
class LayoutProfile:
    orientation: str  # "portrait" | "landscape"
    modules: Dict[str, ModuleLayout]

@dataclass(frozen=True)
class LayoutState:
    active_orientation: str
    profiles: Dict[str, LayoutProfile]
    move_mode_module: Optional[str] = None
