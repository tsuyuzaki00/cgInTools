from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWindowBase(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        menuBar = self.menuBar()
        statusBar = self.statusBar()
        file_menu = menuBar.addMenu("File")
        self.centerWidget = QWidget()

        import_action = QAction("Import Settings", self)
        export_action = QAction("Export Settings", self)
        reset_action = QAction("Reset Settings", self)

        file_menu.addAction(import_action)
        file_menu.addAction(export_action)
        file_menu.addAction(reset_action)

        #centralWidget.setLayout(layout) Widgetizing a layout
        self.setCentralWidget(self.centerWidget)

        statusBar.showMessage("")
        
"""
window_instance = MainWindowBase()
window_instance.show()
"""
