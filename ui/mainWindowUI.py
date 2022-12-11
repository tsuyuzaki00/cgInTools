from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class MainWindowBase(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindowBase,self).__init__(*args,**kwargs)
        self.setWindowFlags(Qt.Window)

        menuBar_QMenuBar=self.menuBar()
        statusBar_QStatusBar=self.statusBar()
        menuBar_QMenu=menuBar_QMenuBar.addMenu("File")

        refresh_QAction=QAction("Refresh Settings",self)
        menuBar_QMenu.addAction(refresh_QAction)

        restore_QAction=QAction("Restore Settings",self)
        menuBar_QMenu.addAction(restore_QAction)
        
        save_QAction=QAction("Save Settings",self)
        menuBar_QMenu.addAction(save_QAction)
        
        menuBar_QMenu.addSeparator()
        
        import_QAction=QAction("Import Settings",self)
        menuBar_QMenu.addAction(import_QAction)
        
        export_QAction=QAction("Export Settings",self)
        menuBar_QMenu.addAction(export_QAction)

        self.center_QWidget=QWidget()
        self.setCentralWidget(self.center_QWidget)
        statusBar_QStatusBar.showMessage("")
        

#window_instance = MainWindowBase()
#window_instance.show()

