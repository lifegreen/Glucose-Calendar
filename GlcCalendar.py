import sys
from PySide2.QtWidgets import QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog, QMainWindow

import GlcLog
import pandas as pd


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.name = QLineEdit('Enter your name')
        # self.name.show()
        self.button = QPushButton('Greet')
        self.button.clicked.connect(self.greet)
        # self.button.show()

        layout = QVBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def greet(self):
        print('Greetings {}'.format(self.name.text()))



if __name__ == "__main__":
    # Create the application object
    app = QApplication(sys.argv)

    f = Form()
    f.show( )

    app.exec_()


