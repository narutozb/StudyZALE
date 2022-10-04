import os
import sys
import time

import pandas as pd
from PySide6 import QtCore
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem, QApplication, QHeaderView, \
    QListWidget, QAbstractItemView, QMainWindow, QVBoxLayout, QGroupBox, QFormLayout, QGridLayout, QLabel, QComboBox, \
    QLineEdit, QSpinBox, QPushButton, QFileDialog, QTextEdit, QMessageBox, QProgressBar, QProgressDialog
from PySide6.QtCore import QItemSelection, QLocale, Qt, Slot, QTimer

from export import get_psd_infos, export_psd_group_to

#
LAYER_DETAIL_INFO_LIST = ['Name', 'IsVisible', 'Type?', 'Size?', 'ParentName?', 'HasMask?', 'HasEffect?']


class LayertableWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # self.setFixedSize(800,500)
        self.resize(800, 500)

        self.init_ui()
        self.set_file_list_ui()
        self.set_layers_ui()
        self.create_grid_group_box()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self._form_group_box)
        main_layout.addWidget(self._gb_layer_detail_box)
        main_layout.addWidget(self._grid_group_box)
        self.setLayout(main_layout)
        self.worker = Worker()
        self.worker.update_progress.connect(self.set_progress_value)

    def init_ui(self):
        # 设置标题
        self.setWindowTitle('LayerInfos')

    def set_layers_ui(self):
        self._gb_layer_detail_box = QGroupBox('Layer Details')
        layout = QVBoxLayout()

        # 建立QTabWidget布局
        self.layer_table_widget = QTableWidget(0, len(LAYER_DETAIL_INFO_LIST))

        self._gb_layer_detail_box.setLayout(layout)
        self.layer_table_widget.width = 2000
        self.layer_table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layer_table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.layer_table_widget.setHorizontalHeaderLabels(LAYER_DETAIL_INFO_LIST)  # set
        self.layer_table_widget.verticalHeader().hide()  # 隐藏index0

        # 保存信息按钮
        details_func_layout = QHBoxLayout()

        # layout
        layout.addWidget(self.layer_table_widget)
        layout.addLayout(details_func_layout)

    def set_file_list_ui(self):

        self._form_group_box = QGroupBox("File list")
        layout = QVBoxLayout()
        bt_layout = QHBoxLayout()

        bt_add_file_to_list = QPushButton('Add PSD Files')
        # 绑定 添加文件名到文件列表
        bt_add_file_to_list.clicked.connect(self.add_file_to_list_func)

        # 移除文件按钮
        bt_remove_file = QPushButton('Remove File')
        # 绑定 在文件列表中移除文件 按钮
        bt_remove_file.clicked.connect(self.remove_file_from_list_func)

        # 导出按钮
        bt_export_all_list_file = QPushButton('Export All To')
        bt_export_all_list_file.clicked.connect(self.export_all_file_to_func)

        self._list_widget = QListWidget()
        self._list_widget.doubleClicked.connect(self.double_clicked_file_item_func)

        export_layout = QHBoxLayout()

        #
        bt_layout.addWidget(bt_add_file_to_list)
        bt_layout.addWidget(bt_remove_file)

        export_layout.addWidget(bt_export_all_list_file)
        # Layout
        layout.addLayout(bt_layout)
        layout.addWidget(self._list_widget)

        layout.addLayout(export_layout)
        self._form_group_box.setLayout(layout)

    def remove_file_from_list_func(self) -> None:
        if not self._list_widget.currentItem():
            return
        if self._gb_layer_detail_box.title() == self._list_widget.currentItem().text():
            self.layer_table_widget.setRowCount(0)
            self._gb_layer_detail_box.setTitle('Select a file for Layer Details')
        # remove func
        self._list_widget.takeItem(self._list_widget.currentRow())

    def add_file_to_list_func(self):
        """
        获取所选择的文件列表，并且更新列表到相关UI
        :return:
        """
        file_names, selected_filter = \
            QFileDialog.getOpenFileNames(self, caption='Open File', dir=os.path.expanduser('~'),
                                         filter='psd files(*.psd *.psb)')

        # 获取当前文件列表中列表
        items_text = self.current_file_list

        # 对比，并且更新列表
        add_to = [i for i in file_names if i not in items_text]

        self._list_widget.addItems(add_to)

    def double_clicked_file_item_func(self):
        current_file_name = self._list_widget.currentItem().text()
        self._gb_layer_detail_box.setTitle('%s' % current_file_name)
        dict1 = get_psd_infos(current_file_name)

        # 将字典转化为 DataFrame. 需要numpy
        df = pd.DataFrame(data=dict1)
        df_t = df.T
        # 初始化行
        self.layer_table_widget.setRowCount(0)
        self.layer_table_widget.setRowCount(len(dict1[list(dict1.keys())[0]]))

        for i in df_t:
            row = 0
            for j in df_t[i]:
                item = QTableWidgetItem(str(j))
                # 如果列数大于某一行时，不可编辑
                if row > 1:
                    item.setFlags(Qt.ItemIsEditable)
                self.layer_table_widget.setItem(i, row, item)
                row += 1

    def export_all_file_to_func(self) -> None:

        if not self.continue_dialog(message='Do you want export all?'):
            return

        if len(self.current_file_list) < 1:
            return
        self.worker.file_list = self.current_file_list
        self.progressbar.setRange(0, len(self.current_file_list) - 1)

        # progressing
        self.worker.start()

    def create_grid_group_box(self):
        self._grid_group_box = QGroupBox("Progress")
        layout = QVBoxLayout()

        # progress bar
        self.progressbar = QProgressBar(self)
        layout.addWidget(self.progressbar)

        self._grid_group_box.setLayout(layout)

    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, 'Confirm', 'Quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @property
    def current_file_list(self):
        return [self._list_widget.item(num).text() for num in range(self._list_widget.count())]

    def continue_dialog(self, message=''):
        reply = QMessageBox.question(self, 'Confirm', f'{message}', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        else:
            return

    def set_progress_value(self, progress):
        self.progressbar.setValue(progress)


class ExportFileNameGroup():
    def __init__(self):
        self.create_group()

    def create_group(self):
        # self.group_for_form_group = QGroupBox()
        self.layout = QHBoxLayout()

        self.prefix = QLineEdit()
        self.middle = QLabel()
        self.suffix = QLineEdit()

        self.layout.addWidget(self.prefix)
        self.layout.addWidget(self.middle)
        self.layout.addWidget(self.suffix)

        # self.group_for_form_group.setLayout(layout)


class Worker(QtCore.QThread):
    update_progress = QtCore.Signal(int)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.file_list = []

    def run(self):
        num = 0
        for i in self.file_list:
            export_psd_group_to(orig_=i)
            self.update_progress.emit(num)
            num += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LayertableWidget()
    main.show()
    sys.exit(app.exec())
