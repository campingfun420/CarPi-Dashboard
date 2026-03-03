import sys
from PyQt5.QtWidgets import QApplication
from dashboard import DashboardLayoutEngine
from module_container import ModuleContainer
from topbar import TopBar
from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget

class DemoMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Radio Dashboard Demo")
        self.resize(1920, 1080)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        central.setLayout(main_layout)

        # Top Bar
        self.top_bar = TopBar()
        self.top_bar.rotate_clicked.connect(self.rotate_screen)
        main_layout.addWidget(self.top_bar)

        # Dashboard
        self.dashboard = DashboardLayoutEngine()
        main_layout.addWidget(self.dashboard, stretch=1)

        # Sample modules
        self.create_sample_modules()

        # Load saved layout
        self.dashboard.load_layout()

    def create_sample_modules(self):
        radio = ModuleContainer(QLabel("Radio"), grid_w=2, grid_h=1)
        self.dashboard.add_module(radio, 0, 0)

        maps = ModuleContainer(QLabel("Maps"), grid_w=2, grid_h=1)
        self.dashboard.add_module(maps, 2, 0)

        video = ModuleContainer(QLabel("Video"), grid_w=2, grid_h=1)
        self.dashboard.add_module(video, 0, 1)

        volume = ModuleContainer(QLabel("Volume"), grid_w=1, grid_h=1)
        self.dashboard.add_module(volume, 2, 1)

        audio_vis = ModuleContainer(QLabel("Audio Visualizer"), grid_w=1, grid_h=1)
        self.dashboard.add_module(audio_vis, 3, 1)

    def rotate_screen(self):
        new_orientation = "portrait" if self.dashboard.orientation=="landscape" else "landscape"
        self.dashboard.set_orientation(new_orientation)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DemoMainWindow()
    window.show()
    sys.exit(app.exec_())