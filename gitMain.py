import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QListWidget, QPushButton
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        vertical_layout = QVBoxLayout()

        self.lbl_mouse_coords = QLabel("Mouse Coords")
        self.lbl_current_endpoint = QLabel("Current Endpoint")
        self.btn_get_image = QPushButton("Open Image")

        vertical_layout.addWidget(self.lbl_mouse_coords)
        vertical_layout.addWidget(self.lbl_current_endpoint)
        vertical_layout.addWidget(self.btn_get_image)

        widget = QWidget()
        widget.setLayout(vertical_layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
