import sys
import pandas as pd
from PySide6.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QApplication, QHeaderView, \
    QListWidget, QAbstractItemView, QMainWindow, QVBoxLayout, QGroupBox, QFormLayout, QGridLayout, QLabel, QComboBox, \
    QLineEdit, QSpinBox, QPushButton, QFileDialog
from PySide6.QtCore import QItemSelection, QLocale, Qt, Slot

# from typing import Optional
from numbers import Number

#
LAYER_DETAIL_INFO_LIST = ['Name', 'IsVisible', 'Type?', 'Size?', 'ParentName?', 'HasMask?', 'HasEffect?']

LAYER_INFOS_REFERENCE = {
    'Name': ['GroupA', 'GroupB'],
    'IsVisible': [True, False],
    'Type?': ['Group', 'Group'],
    'Size?': ['1000*1000', '1000*1000'],
    'ParentName?': ['Root', 'Root'],
    'HasMask?': [False, False],
    'HasEffect?': [False, False],
}
df = pd.DataFrame(data=LAYER_INFOS_REFERENCE)
df_t = df.T


class LayertableWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()
        self.set_file_list_ui()
        self.set_layers_ui(2, 7)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self._form_group_box)
        main_layout.addWidget(self.layer_table_widget)
        self.setLayout(main_layout)

    def init_ui(self):
        # 设置标题
        self.setWindowTitle('LayerInfos')

    def set_layers_ui(self, rows, cols):
        layer_detail_layout = QHBoxLayout()
        # 建立QTabWidget布局
        self.layer_table_widget = QTableWidget(rows, cols)

        layer_detail_layout.addWidget(self.layer_table_widget)
        self.layer_table_widget.width = 2000
        self.layer_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.layer_table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.layer_table_widget.setHorizontalHeaderLabels(LAYER_DETAIL_INFO_LIST)  # set
        self.layer_table_widget.verticalHeader().hide()  # 隐藏index0

        for i in df_t:
            row = 0
            for j in df_t[i]:
                print(f'({i}, {row}, QTableWidgetItem("{j}"))')
                item = QTableWidgetItem(str(j))
                # 如果列数大于某一行时，不可编辑
                if row > 1:
                    item.setFlags(Qt.ItemIsEditable)
                self.layer_table_widget.setItem(i, row, item)
                row += 1

    def set_file_list_ui(self):

        self._form_group_box = QGroupBox("Form layout")
        layout = QVBoxLayout()
        bt_layout = QHBoxLayout()

        layout.addLayout(bt_layout)
        button = QPushButton('AAA')
        button2 = QPushButton('BBB')
        _list_widget = QListWidget()
        _list_widget.addItem("C++")
        _list_widget.addItem("Java")
        _list_widget.addItem("Python")
        bt_layout.addWidget(button)
        bt_layout.addWidget(button2)
        layout.addWidget(_list_widget)

        self._form_group_box.setLayout(layout)

def get_files(parent):
    file_name, selected_filter = \
    QFileDialog.getOpenFileNames(parent, caption='Open File', dir=os.path.expanduser('~'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LayertableWidget()
    main.show()

    sys.exit(app.exec())
