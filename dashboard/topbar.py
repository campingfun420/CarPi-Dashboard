from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, pyqtSignal

class TopBar(QWidget):
    rotate_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QHBoxLayout()
        layout.setContentsMargins(5,5,5,5)

        logo_label = QLabel()
        logo_pixmap = QPixmap("resources/logo.png").scaled(255,60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        layout.addWidget(logo_label, alignment=Qt.AlignLeft)

        self.clock_label = QLabel("12:00")
        self.clock_label.setFont(QFont("Arial",36))
        self.clock_label.setStyleSheet("color:white")
        layout.addWidget(self.clock_label, stretch=1, alignment=Qt.AlignCenter)

        self.volume_label = QLabel("Vol: 50%")
        self.volume_label.setFont(QFont("Arial",28))
        self.volume_label.setStyleSheet("color:white")
        layout.addWidget(self.volume_label, alignment=Qt.AlignRight)

        rotate_button = QPushButton("↻")
        rotate_button.setFont(QFont("Arial",24))
        rotate_button.setFixedSize(60,60)
        rotate_button.clicked.connect(lambda: self.rotate_clicked.emit())
        layout.addWidget(rotate_button, alignment=Qt.AlignRight)

        self.setLayout(layout)