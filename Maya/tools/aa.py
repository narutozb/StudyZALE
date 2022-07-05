from PySide2 import QtCore,QtWidgets,QtGui
from PySide2.QtWidgets import QLabel,QPushButton,QApplication, QDialog, QLineEdit, QPushButton,QLineEdit, QPushButton, QApplication,QVBoxLayout, QDialog, QHBoxLayout,QTextBrowser,QComboBox
from PySide2.QtCore import Slot

import maya.app.general.mayaMixin as MayaMixin
import maya.OpenMaya as om
import maya.OpenMayaUI
from shiboken2 import wrapInstance



def teee(func):
    def wrapper(*args, **kwargs):
        print (kwargs)
        return func(*args, **kwargs)
    return wrapper

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Add button signal to greetings slot

        self.main_layout = QVBoxLayout()

        self.start_up()

        self.setLayout(self.main_layout)

        self.show()

    def create_preset_edit_line(self):
        # Create widgets
        prefix_edit = QLineEdit("Write my name here")
        suffix_edit = QLineEdit('_Suffix')
        button = QPushButton("Show Greetings")
        type_name_label = QLabel("""object's name""")
        # Create layout and add widgets
        layout = QHBoxLayout()
        layout.setObjectName('a')
        print layout.objectName()
        layout.addWidget(prefix_edit,2)
        layout.addWidget(type_name_label,1)
        layout.addWidget(suffix_edit,3)
        layout.addWidget(button,1)

        button.clicked.connect(self.greetings)

        # Set dialog layout
        self.main_layout.addLayout(layout)

    def start_up(self):
        start_up_layout = QHBoxLayout()
        combobox = QComboBox(self)
        combobox.addItems(['a', 'b', 'c'])
        add_button = QPushButton('+')
        add_button.clicked.connect(self.test)
        start_up_layout.addWidget(combobox)
        start_up_layout.addWidget(add_button)
        self.main_layout.addLayout(start_up_layout)




    # Greets the user
    def greetings(self):
        print 11




    def test(self):
        print ('111')
        self.create_preset_edit_line()




mayaMainWindowPtr = maya.OpenMayaUI.MQtUtil.mainWindow()
mayaMainWindow= wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)


# Create and show the form
form = Form(parent=mayaMainWindow)


class AA(QDialog):
    def __init__(self, parent=None):
        super(AA, self).__init__(parent)
        # Add button signal to greetings slot
        add_button = QPushButton('+')
        add_button.clicked.connect(self.test)
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(add_button)
        self.setLayout(self.main_layout)
        combo_box = QComboBox(self)
        combo_box.addItems(['a', 'b', 'c'])
        self.show()
    def test(self):
        print 1



