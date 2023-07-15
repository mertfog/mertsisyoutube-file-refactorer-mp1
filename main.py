import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import *
from refactorer import FileRefactorer


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = self.create_and_get_central_widget()

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def set_button_state(self):
        if self.folder_path.text():
            self.refactor_button.setDisabled(False)
        else:
            self.refactor_button.setDisabled(True)

    def select_folder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.folder_path.setText(folder)

    def refactor_files(self):
        rfc = FileRefactorer(self.folder_path.text())
        rfc.refactor()

    def create_and_get_central_widget(self):
        widget = QWidget(self)

        # Layout
        layout = QVBoxLayout()

        folder_layout = QHBoxLayout()

        # Buttons
        folder_selection_button = QPushButton()
        folder_selection_button.setText('>')
        folder_selection_button.clicked.connect(self.select_folder)

        self.refactor_button = QPushButton()
        self.refactor_button.setText('Refactor')
        self.refactor_button.clicked.connect(self.refactor_files)
        self.refactor_button.setDisabled(True)

        # Input
        self.folder_path = QLineEdit()
        self.folder_path.setReadOnly(True)
        self.folder_path.textChanged.connect(self.set_button_state)

        folder_layout.addWidget(folder_selection_button)
        folder_layout.addWidget(self.folder_path)

        layout.addLayout(folder_layout)
        layout.addWidget(self.refactor_button)

        widget.setLayout(layout)

        return widget


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
