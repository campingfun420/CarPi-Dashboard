import os
import json

LAYOUT_DIR = "layout_profiles"

def save_layout_profile(layout_state):
    profile = layout_state.profiles[layout_state.active_orientation]
    os.makedirs(LAYOUT_DIR, exist_ok=True)
    file_path = os.path.join(LAYOUT_DIR, f"{profile.orientation}.json")
    with open(file_path, "w") as f:
        json.dump({"orientation": profile.orientation, "row_order": profile.row_order}, f, indent=2)
