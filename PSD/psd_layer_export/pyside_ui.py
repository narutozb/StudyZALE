import sys

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):
        btn_quick = QPushButton('Force Quite', self)
        btn_quick.clicked.connect(QApplication.instance().quit)
        btn_quick.resize(btn_quick.sizeHint())
        btn_quick.move(90, 100)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('WindExampleTitle')

        self.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, 'Message', 'Are you sore you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def run():
    app = QApplication([])
    ex = Example()
    app.exec_()


if __name__ == '__main__':
    run()
