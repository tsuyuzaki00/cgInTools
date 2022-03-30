from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class PathTextWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(PathTextWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        path_line_layout = QFormLayout(self)

        self.path_line = QLineEdit(self)
        self.json_line = QLineEdit(self)

        path_line_layout.addRow("path",self.path_line)
        path_line_layout.addRow(".json",self.json_line)

#window_instance = PathTextWindowBase()
#window_instance.show()