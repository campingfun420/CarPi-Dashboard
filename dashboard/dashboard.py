import json
import os
from PyQt5.QtWidgets import QWidget
from math import floor

class DashboardLayoutEngine(QWidget):
    LAYOUT_FILE = "dashboard_layout.json"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.modules = []
        self.rows = 2  # default landscape
        self.columns = 3
        self.cell_width = 0
        self.cell_height = 0
        self.orientation = "landscape"

    def add_module(self, module, grid_x=0, grid_y=0):
        module.grid_x = grid_x
        module.grid_y = grid_y
        module.move_started.connect(self.on_module_move_started)
        module.move_finished.connect(self.on_module_move_finished)
        self.modules.append(module)
        module.setParent(self)
        module.show()
        self.update_layout()

    def set_orientation(self, orientation):
        self.orientation = orientation
        self.rows = 4 if orientation == "portrait" else 2
        self.update_layout()

    def resizeEvent(self, event):
        self.update_layout()

    def update_layout(self):
        self.cell_height = self.height() / self.rows
        self.cell_width = self.cell_height
        self.columns = floor(self.width() / self.cell_width)

        for module in self.modules:
            x = module.grid_x * self.cell_width
            y = module.grid_y * self.cell_height
            w = module.grid_w * self.cell_width
            h = module.grid_h * self.cell_height
            module.setGeometry(int(x), int(y), int(w), int(h))

    def on_module_move_started(self, module):
        module.raise_()

    def on_module_move_finished(self, module, _, __):
        x = module.x()
        y = module.y()
        new_grid_x = max(0, min(self.columns - module.grid_w, round(x / self.cell_width)))
        new_grid_y = max(0, min(self.rows - module.grid_h, round(y / self.cell_height)))
        module.grid_x = new_grid_x
        module.grid_y = new_grid_y
        self.update_layout()
        self.save_layout()

    def save_layout(self):
        layout_data = []
        for module in self.modules:
            layout_data.append({
                "id": id(module),
                "grid_x": module.grid_x,
                "grid_y": module.grid_y,
                "grid_w": module.grid_w,
                "grid_h": module.grid_h,
                "title": getattr(module.feature_widget, "text", "")
            })
        try:
            with open(self.LAYOUT_FILE, "w") as f:
                json.dump(layout_data, f, indent=2)
        except Exception as e:
            print("Error saving layout:", e)

    def load_layout(self):
        if not os.path.exists(self.LAYOUT_FILE):
            return
        try:
            with open(self.LAYOUT_FILE, "r") as f:
                layout_data = json.load(f)
            for data in layout_data:
                for module in self.modules:
                    if getattr(module.feature_widget, "text", "") == data.get("title"):
                        module.grid_x = data["grid_x"]
                        module.grid_y = data["grid_y"]
                        module.grid_w = data["grid_w"]
                        module.grid_h = data["grid_h"]
            self.update_layout()
        except Exception as e:
            print("Error loading layout:", e)
