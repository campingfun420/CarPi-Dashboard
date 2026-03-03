from PyQt5.QtWidgets import QFrame, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QPoint
from PyQt5.QtGui import QColor, QPainter, QTransform

class ModuleContainer(QFrame):
    move_started = pyqtSignal(object)
    move_finished = pyqtSignal(object, int, int)

    HOLD_DURATION_MS = 3000
    MOVE_BORDER_COLOR = QColor(255,0,0)
    OUTLINE_COLOR = QColor(255,255,255)
    FLOAT_SCALE = 1.03

    def __init__(self, widget, grid_w=1, grid_h=1, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Box)
        self.setLineWidth(2)
        self.grid_x = 0
        self.grid_y = 0
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.feature_widget = widget
        self.is_moving = False
        self._hold_timer = QTimer(self)
        self._hold_timer.setSingleShot(True)
        self._hold_timer.timeout.connect(self._enter_move_mode)
        self._drag_offset = QPoint()
        self._parking_locked = False

        # Floating shadow
        self._shadow_effect = QGraphicsDropShadowEffect()
        self._shadow_effect.setColor(QColor(0,0,0,160))
        self._shadow_effect.setOffset(5,5)
        self._shadow_effect.setBlurRadius(15)
        self.setGraphicsEffect(None)

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(widget)
        self.setLayout(layout)

    def set_parking_lock(self, locked: bool):
        self._parking_locked = locked

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            child = self.childAt(event.pos())
            if child and getattr(child, "isButton", False):
                return
            self._press_pos = event.pos()
            self._hold_timer.start(self.HOLD_DURATION_MS)

    def mouseMoveEvent(self, event):
        if not self.is_moving:
            if (event.pos() - self._press_pos).manhattanLength() > 10:
                self._hold_timer.stop()
        else:
            self.move(self.mapToParent(event.pos() - self._drag_offset))

    def mouseReleaseEvent(self, event):
        self._hold_timer.stop()
        if self.is_moving:
            self.is_moving = False
            self.setGraphicsEffect(None)
            self._apply_scale(1.0)
            self.move_finished.emit(self, self.grid_x, self.grid_y)
            self.update()

    def _enter_move_mode(self):
        if self._parking_locked:
            return
        self.is_moving = True
        self._drag_offset = self._press_pos
        self.move_started.emit(self)
        self.setGraphicsEffect(self._shadow_effect)
        self._apply_scale(self.FLOAT_SCALE)
        self.update()

    def _apply_scale(self, scale_factor):
        transform = QTransform()
        transform.scale(scale_factor, scale_factor)
        self.setTransform(transform)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pen_color = self.MOVE_BORDER_COLOR if self.is_moving else self.OUTLINE_COLOR
        painter.setPen(pen_color)
        painter.drawRect(0, 0, self.width()-1, self.height()-1)
