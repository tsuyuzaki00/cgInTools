from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MNamingWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MNamingWindow, self).__init__(*args, **kwargs)
        main_layout = QFormLayout(self)

        # create buttons
        auto_button = QRadioButton("Auto", self)
        center_button = QRadioButton("Center", self)
        left_button = QRadioButton("Left", self)
        right_button = QRadioButton("Right", self)
        auto_button.setChecked(True)
        select_label = QLabel("SelectList",self)
        select_list = QLineEdit(self)
        asset_label = QLabel("AssetName",self)
        asset_name = QLineEdit(self)
        variant_label = QLabel("VariantName",self)
        variant_name = QLineEdit(self)
        num_switch = QCheckBox("", self)
        add_select_button = QPushButton("Add")
        rename_button = QPushButton("Rename")

        #setting buttons
        label_layout = QHBoxLayout(self)
        label_layout.addWidget(select_label)
        label_layout.addWidget(asset_label)
        label_layout.addWidget(variant_label)
        main_layout.addRow(label_layout)

        rename_layout = QHBoxLayout(self)
        rename_layout.addWidget(select_list)
        rename_layout.addWidget(asset_name)
        rename_layout.addWidget(variant_name)
        main_layout.addRow(rename_layout)

        side_layout = QHBoxLayout(self)
        side_layout.addWidget(auto_button)
        side_layout.addWidget(left_button)
        side_layout.addWidget(center_button)
        side_layout.addWidget(right_button)
        main_layout.addRow("side", side_layout)

        num_switch_layout = QVBoxLayout(self)
        num_switch_layout.addWidget(num_switch, True)
        main_layout.addRow("number",num_switch_layout)

        run_layout = QHBoxLayout(self)
        run_layout.addWidget(add_select_button, True)
        run_layout.addWidget(rename_button, True)
        main_layout.addRow(run_layout)

