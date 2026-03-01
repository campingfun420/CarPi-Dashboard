from core.state.system_state import LayoutState, LayoutProfile
from core.events.layout_events import SetOrientation, EnterMoveMode, SwapRows, ExitMoveMode

def layout_reducer(state: LayoutState, event, gear: str):
    if isinstance(event, SetOrientation):
        if event.orientation in state.profiles:
            return LayoutState(
                active_orientation=event.orientation,
                profiles=state.profiles,
                move_mode_row=None,
            )

    if gear != "PARK":
        return state

    if isinstance(event, EnterMoveMode):
        return LayoutState(
            active_orientation=state.active_orientation,
            profiles=state.profiles,
            move_mode_row=event.row_id,
        )

    if isinstance(event, SwapRows):
        profile = state.profiles[state.active_orientation]
        order = profile.row_order.copy()
        if event.row_a in order and event.row_b in order:
            idx_a, idx_b = order.index(event.row_a), order.index(event.row_b)
            order[idx_a], order[idx_b] = order[idx_b], order[idx_a]
            updated_profile = LayoutProfile(profile.orientation, order)
            updated_profiles = state.profiles.copy()
            updated_profiles[state.active_orientation] = updated_profile
            return LayoutState(state.active_orientation, updated_profiles, state.move_mode_row)

    if isinstance(event, ExitMoveMode):
        return LayoutState(state.active_orientation, state.profiles, None)

    return state
