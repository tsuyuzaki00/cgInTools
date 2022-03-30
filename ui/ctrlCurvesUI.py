#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class CtrlCurvesWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(CtrlCurvesWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_layout = QFormLayout(self)
        scale_layout = QHBoxLayout(self)
        direction_layout = QGridLayout(self)
        constraint_layout = QGridLayout(self)
        snap_layout = QHBoxLayout(self)
        child_layout = QHBoxLayout(self)
        parent_layout = QVBoxLayout(self)
        
        ctrls_layout = QHBoxLayout(self)
        plane_layout = QVBoxLayout(self)
        solid_layout = QVBoxLayout(self)
        arrow_layout = QVBoxLayout(self)
        other_layout = QVBoxLayout(self)

        main_layout.addRow(scale_layout)
        main_layout.addRow(direction_layout)
        main_layout.addRow(snap_layout)
        main_layout.addRow(constraint_layout)
        main_layout.addRow(child_layout)
        main_layout.addRow(parent_layout)
        main_layout.addRow(ctrls_layout)

        self.scale_line = QFrame
        self.scale_label = QLabel("Scale:",self)
        self.scale_text = QLineEdit(self)
        self.scale_slider = QSlider(Qt.Horizontal,self)
        scale_layout.addWidget(self.scale_label)
        scale_layout.addWidget(self.scale_text)
        scale_layout.addWidget(self.scale_slider)

        self.direction_label = QLabel("Direction:",self)
        self.plusX_radio = QRadioButton("+X",self)
        self.plusY_radio = QRadioButton("+Y",self)
        self.plusZ_radio = QRadioButton("+Z",self)
        self.minusX_radio = QRadioButton("-X",self)
        self.minusY_radio = QRadioButton("-Y",self)
        self.minusZ_radio = QRadioButton("-Z",self)

        self.direction_group = QButtonGroup()
        self.direction_group.addButton(self.plusX_radio,1)
        self.direction_group.addButton(self.plusY_radio,2)
        self.direction_group.addButton(self.plusZ_radio,3)
        self.direction_group.addButton(self.minusX_radio,4)
        self.direction_group.addButton(self.minusY_radio,5)
        self.direction_group.addButton(self.minusZ_radio,6)
        self.plusY_radio.toggle()

        direction_layout.addWidget(self.direction_label,0,0)
        direction_layout.addWidget(self.plusX_radio,0,1)
        direction_layout.addWidget(self.plusY_radio,0,2)
        direction_layout.addWidget(self.plusZ_radio,0,3)
        direction_layout.addWidget(self.minusX_radio,1,1)
        direction_layout.addWidget(self.minusY_radio,1,2)
        direction_layout.addWidget(self.minusZ_radio,1,3)
        

        self.constraint_label = QLabel("Constraint:",self)
        self.off_constraint_radio = QRadioButton("off",self)
        self.parent_constraint_radio = QRadioButton("parent",self)
        self.matrix_constraint_radio = QRadioButton("matrix",self)
        self.point_constraint_radio = QRadioButton("point",self)
        self.rotate_constraint_radio = QRadioButton("rotate",self)
        self.scale_constraint_radio = QRadioButton("scale",self)

        self.constraint_group = QButtonGroup()
        self.constraint_group.addButton(self.off_constraint_radio,1)
        self.constraint_group.addButton(self.parent_constraint_radio,2)
        self.constraint_group.addButton(self.matrix_constraint_radio,3)
        self.constraint_group.addButton(self.point_constraint_radio,4)
        self.constraint_group.addButton(self.rotate_constraint_radio,5)
        self.constraint_group.addButton(self.scale_constraint_radio,6)
        self.off_constraint_radio.toggle()

        constraint_layout.addWidget(self.constraint_label,0,0)
        constraint_layout.addWidget(self.off_constraint_radio,0,1)
        constraint_layout.addWidget(self.parent_constraint_radio,0,2)
        constraint_layout.addWidget(self.matrix_constraint_radio,0,3)
        constraint_layout.addWidget(self.point_constraint_radio,1,1)
        constraint_layout.addWidget(self.rotate_constraint_radio,1,2)
        constraint_layout.addWidget(self.scale_constraint_radio,1,3)
        
        self.snap_label = QLabel("Snap:",self)
        self.snap_check = QCheckBox(self)
        snap_layout.addWidget(self.snap_label)
        snap_layout.addWidget(self.snap_check)

        self.child_null_label = QLabel("Child null:",self)
        self.child_null_check = QCheckBox(self)
        self.child_null_text = QLineEdit(self)
        child_layout.addWidget(self.child_null_label)
        child_layout.addWidget(self.child_null_check)
        child_layout.addWidget(self.child_null_text)

        self.parent_null_label = QLabel("Parent null:",self)
        self.parent_null_text = QLineEdit(self)
        self.parent1_null_text = QLineEdit(self)
        self.parent2_null_text = QLineEdit(self)
        self.parent3_null_text = QLineEdit(self)
        self.parent4_null_text = QLineEdit(self)
        self.parent5_null_text = QLineEdit(self)
        self.parent_slider = QSlider(Qt.Horizontal,self)

        parent_layout.addWidget(self.parent_null_label)
        parent_layout.addWidget(self.parent_null_text)
        parent_layout.addWidget(self.parent_slider)
        parent_layout.addWidget(self.parent1_null_text)
        parent_layout.addWidget(self.parent2_null_text)
        parent_layout.addWidget(self.parent3_null_text)
        parent_layout.addWidget(self.parent4_null_text)
        parent_layout.addWidget(self.parent5_null_text)

        """
        tab_widget = QTabWidget(self)
        tab_widget.addTab(plane_layout,"Plane")
        tab_widget.addTab(solid_layout,"Solid")
        tab_widget.addTab(arrow_layout,"Arrow")
        tab_widget.addTab(other_layout,"Other")

        ctrls_layout.addWidget(tab_widget)
        """



window_instance = CtrlCurvesWindowBase()
window_instance.show()