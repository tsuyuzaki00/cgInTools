import os
from mainEdit import qt
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import maya.cmds as cmds
import maya.api.OpenMaya as om

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('errorChecker')
        self.resize(450,800)

        widget = OptionWidget()
        self.setCentralWidget(widget)

class SelectionRadio(QWidget):
    def __init__(self, *args, **kwargs):
        super(SelectionRadio,self).__init__(*args, **kwargs)

        selectionLayout = QHBoxLayout(self)

        selectRadio = QRadioButton('Select')
        hierarchyRadio = QRadioButton('Hierarchy')
        allRadio = QRadioButton('All')
        selectRadio.setChecked(True)

        selectionLayout.addWidget(selectRadio, True)
        selectionLayout.addWidget(hierarchyRadio, True)
        selectionLayout.addWidget(allRadio, True)

        self.__selectionLayout = QButtonGroup(self)
        self.__selectionLayout.addButton(selectRadio, 0)
        self.__selectionLayout.addButton(hierarchyRadio, 1)
        self.__selectionLayout.addButton(allRadio, 2)

class Container(QWidget):
    def __init__(self, checkName, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)
        self.checkName = checkName

        containerLayout = QHBoxLayout(self)

        self.hideButton = QPushButton(self.checkName, self)
        self.hideButton.setCheckable(True)
        containerLayout.addWidget(self.hideButton, True)

        self.checkAllButton = QPushButton('Check\n' + self.checkName, self)
        self.checkAllButton.setChecked(True)
        containerLayout.addWidget(self.checkAllButton, True)
        
        self.unCheckAllButton = QPushButton('unCheck\n' + self.checkName, self)
        self.unCheckAllButton.setChecked(True)
        containerLayout.addWidget(self.unCheckAllButton, True)

class CheckBox(QWidget):
    checked = Signal(bool)
    def __init__(self, checkType, *args, **kwargs):
        super(CheckBox, self).__init__(*args, **kwargs)
        self.checkType = checkType
        checkBoxLayout = QHBoxLayout(self)

        self.checkedValue = True

        self.checkBox = QCheckBox(self.checkType, self)
        self.checkBox.setChecked(True)
        self.checkBox.clicked.connect(self.setChecked)
        checkBoxLayout.addWidget(self.checkBox, True)

        self.runButton = QPushButton('Run', self)
        self.runButton.setChecked(True)
        checkBoxLayout.addWidget(self.runButton, True)

    def setChecked(self):
        self.checkedValue = self.checkBox.isChecked()
        #print self.checkedValue

class ScrollBar(QWidget):
    def __init__(self, *args, **kwargs):
        super(ScrollBar, self).__init__(*args, **kwargs)
        mainLayout = QHBoxLayout(self)
         
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setMinimumWidth(250)
        mainLayout.addWidget(scrollArea)
        
        _checkGrp = CheckGrp(self)
        scrollArea.setWidget(_checkGrp)

class CheckGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(CheckGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _objectGrp = ObjectGrp()
        scrollLayout.addWidget(_objectGrp)
        
        _connectGrp = ConnectGrp()
        scrollLayout.addWidget(_connectGrp)
        
        '''
        _namingGrp = NamingGrp()
        scrollLayout.addWidget(_namingGrp)

        _hierarchyGrp = HierarchyGrp()
        scrollLayout.addWidget(_hierarchyGrp)

        _geometryGrp = GeometryGrp()
        scrollLayout.addWidget(_geometryGrp)

        _uvGrp = UVGrp()
        scrollLayout.addWidget(_uvGrp)

        _matrialGrp = MatrialGrp()
        scrollLayout.addWidget(_matrialGrp)
        '''

class ObjectGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(ObjectGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _object = Container('Object')
        scrollLayout.addWidget(_object)
        
        _frozenBox = CheckBox('FrozenTransform')
        _frozenBox.runButton.clicked.connect(lambda: self.setFrozenButton(_frozenBox))

        _unCenteredBox = CheckBox('UnCenteredPivots')
        _unCenteredBox.runButton.clicked.connect(self.setUnCenteredButton)

        _hiddenBox = CheckBox('HiddenObject')
        _hiddenBox.runButton.clicked.connect(self.setHiddenButton)
        
        _frozenBox.checkBox.setChecked(True)
        _unCenteredBox.checkBox.setChecked(True)
        _hiddenBox.checkBox.setChecked(True)

        scrollLayout.addWidget(_frozenBox)
        scrollLayout.addWidget(_unCenteredBox)
        scrollLayout.addWidget(_hiddenBox)

    def setFrozenButton(self, _frozenBox):
        if _frozenBox.checkedValue == True:
            print 'FrozenTransform'

    def setUnCenteredButton(self):
        print 'UnCenteredPivots'

    def setHiddenButton(self):
        print 'HiddenObject'

class ConnectGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(ConnectGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _connect = Container('Connect')
        scrollLayout.addWidget(_connect)
        #_object.hideButton.clicked.connect()

        _historyBox = CheckBox('History')
        scrollLayout.addWidget(_historyBox)
        _historyBox.runButton.clicked.connect(self.setHistoryButton)

        _layerBox = CheckBox('Layer')
        scrollLayout.addWidget(_layerBox)
        _layerBox.runButton.clicked.connect(self.setLayerButton)

        _keyedObjectBox = CheckBox('KeyedObject')
        scrollLayout.addWidget(_keyedObjectBox)
        _keyedObjectBox.runButton.clicked.connect(self.setKeyedObjectButton)

        _constraintBox = CheckBox('Constraint')
        scrollLayout.addWidget(_constraintBox)
        _constraintBox.runButton.clicked.connect(self.setConstraintButton)

        _expressionBox = CheckBox('Expression')
        scrollLayout.addWidget(_expressionBox)
        _expressionBox.runButton.clicked.connect(self.setExpressionButton)

    def setHistoryButton(self):
        print 'History'

    def setLayerButton(self):
        print 'Layer'

    def setKeyedObjectButton(self):
        print 'HiddenObject'

    def setConstraintButton(self):
        print 'HiddenObject'

    def setExpressionButton(self):
        print 'HiddenObject'

class NamingGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(NamingGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _naming = Container('Naming')
        scrollLayout.addWidget(_naming)
        #_object.hideButton.clicked.connect()

        _defaultNameBox = CheckBox('DefaultName')
        scrollLayout.addWidget(_defaultNameBox)
        _defaultNameBox.runButton.clicked.connect(self.setDefaultNameButton)

        _sameNameBox = CheckBox('SameName')
        scrollLayout.addWidget(_sameNameBox)
        _sameNameBox.runButton.clicked.connect(self.setSameNameButton)

        _nameSpacesBox = CheckBox('NameSpaces')
        scrollLayout.addWidget(_nameSpacesBox)
        _nameSpacesBox.runButton.clicked.connect(self.setNameSpacesButton)

    def setDefaultNameButton(self):
        print 'HiddenObject'

    def setSameNameButton(self):
        print 'HiddenObject'

    def setNameSpacesButton(self):
        print 'HiddenObject'

class HierarchyGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(HierarchyGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _hierarchy = Container('Hierarchy')
        scrollLayout.addWidget(_hierarchy)
        #_object.hideButton.clicked.connect()

        _parentGeometryBox = CheckBox('ParentGeometry')
        scrollLayout.addWidget(_parentGeometryBox)
        _parentGeometryBox.runButton.clicked.connect(self.setParentGeometryButton)

        _childNullBox = CheckBox('ChildNull')
        scrollLayout.addWidget(_childNullBox)
        _childNullBox.runButton.clicked.connect(self.setChildNullButton)

    def setParentGeometryButton(self):
        print 'HiddenObject'

    def setChildNullButton(self):
        print 'HiddenObject'

class GeometryGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(GeometryGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _geometry = Container('Geometry')
        scrollLayout.addWidget(_geometry)
        #_object.hideButton.clicked.connect()

        _NgonsBox = CheckBox('N-Gons')
        scrollLayout.addWidget(_NgonsBox)
        _NgonsBox.runButton.clicked.connect(self.setNgonsButton)

        _laminaFaceBox = CheckBox('LaminaFace')
        scrollLayout.addWidget(_laminaFaceBox)
        _laminaFaceBox.runButton.clicked.connect(self.setLaminaFaceButton)

        _concaveFacesBox = CheckBox('ConcaveFaces')
        scrollLayout.addWidget(_concaveFacesBox)
        _concaveFacesBox.runButton.clicked.connect(self.setConcaveFacesButton)

        _zeroEdgeLengthBox = CheckBox('ZeroEdgeLength')
        scrollLayout.addWidget(_zeroEdgeLengthBox)
        _zeroEdgeLengthBox.runButton.clicked.connect(self.setZeroEdgeLengthButton)

        _lockedNormalsBox = CheckBox('LockedNormals')
        scrollLayout.addWidget(_lockedNormalsBox)
        _lockedNormalsBox.runButton.clicked.connect(self.setLockedNormalsButton)

    def setNgonsButton(self):
        print 'HiddenObject'

    def setLaminaFaceButton(self):
        print 'HiddenObject'

    def setConcaveFacesButton(self):
        print 'HiddenObject'

    def setZeroEdgeLengthButton(self):
        print 'HiddenObject'

    def setLockedNormalsButton(self):
        print 'HiddenObject'

class UVGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(UVGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _uv = Container('UV')
        scrollLayout.addWidget(_uv)
        #_uv.hideButton.clicked.connect()

        _legalBox = CheckBox('Legal UV')
        scrollLayout.addWidget(_legalBox)
        _legalBox.runButton.clicked.connect(self.setLegalButton)

        _penetratingBox = CheckBox('PenetratingUV')
        scrollLayout.addWidget(_penetratingBox)
        _penetratingBox.runButton.clicked.connect(self.setPenetratingButton)

        _inversBox = CheckBox('InversUV')
        scrollLayout.addWidget(_inversBox)
        _inversBox.runButton.clicked.connect(self.setInversButton)

        _noUVBox = CheckBox('No UV')
        scrollLayout.addWidget(_noUVBox)
        _noUVBox.runButton.clicked.connect(self.setNoUVButton)

    def setLegalButton(self):
        print 'HiddenObject'

    def setPenetratingButton(self):
        print 'HiddenObject'

    def setInversButton(self):
        print 'HiddenObject'

    def setNoUVButton(self):
        print 'HiddenObject'

class MatrialGrp(QWidget):
    def __init__(self, *args, **kwargs):
        super(MatrialGrp, self).__init__(*args, **kwargs)
        scrollLayout = QVBoxLayout(self)

        _matrial = Container('Matrial')
        scrollLayout.addWidget(_matrial)
        #_matrial.hideButton.clicked.connect()

        _defaultMaterialBox = CheckBox('DefaultMaterial')
        scrollLayout.addWidget(_defaultMaterialBox)
        _defaultMaterialBox.runButton.clicked.connect(self.setDefaultMaterialButton)

    def setDefaultMaterialButton(self):
        print 'HiddenObject'

class ListTree(QWidget):
    def __init__(self, *args, **kwargs):
        super(ListTree, self).__init__(*args, **kwargs)
        listTreeLayout = QVBoxLayout(self)

        OKobject = ['OKType']
        OKlist = ['OKobject']
        listTreeLayout.addWidget(QLabel('OK'))
        OKWidget = QTreeWidget()
        OKItem = QTreeWidgetItem(OKobject)
        OKWidget.addTopLevelItem(OKItem)
        QTreeWidgetItem(OKItem, OKlist)
        OKWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        listTreeLayout.addWidget(OKWidget)
        
        NGobject = ['NGtype']
        NGlist = ['NGobject']
        listTreeLayout.addWidget(QLabel('NG'))
        NGWidget = QTreeWidget()
        NGItem = QTreeWidgetItem(NGobject)
        NGWidget.addTopLevelItem(NGItem)
        QTreeWidgetItem(NGItem, NGlist)
        NGWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        listTreeLayout.addWidget(NGWidget)

    def OKItem(self, parameter_list):
        pass

    def NGItem(self, parameter_list):
        pass

class RunButton(QWidget):
    def __init__(self, *args, **kwargs):
        super(RunButton, self).__init__(*args, **kwargs)
        runLayout = QHBoxLayout(self)

        checkAllButton = QPushButton('checkAll', self)
        checkAllButton.setChecked(True)
        runLayout.addWidget(checkAllButton)
        checkAllButton.clicked.connect(self.setCheckAll)

        checkUnAllButton = QPushButton('checkUnAll', self)
        checkUnAllButton.setChecked(True)
        runLayout.addWidget(checkUnAllButton)
        checkUnAllButton.clicked.connect(self.setCheckUnAll)

        runButton = QPushButton('checkRun', self)
        runButton.setChecked(True)
        runLayout.addWidget(runButton)
        runButton.clicked.connect(self.setCheckRun)
        
        allRunButton = QPushButton('allRun', self)
        allRunButton.setChecked(True)
        runLayout.addWidget(allRunButton)
        allRunButton.clicked.connect(self.setAllRun)

    def setCheckAll(self):
        _run = Run()
        _run.history()

    def setCheckUnAll(self,runLayout):
        _run = Run()
        _run.history()

    def setCheckRun(self,runLayout):
        _run = Run()
        _run.history()

    def setAllRun(self,runLayout):
        _run = Run()
        _run.history()

class OptionWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)

        optionLayout = QGridLayout(self)

        _selectionRadio = SelectionRadio()
        print _selectionRadio
        _scrollBar = ScrollBar()
        _listTree = ListTree()
        _run = RunButton()

        optionLayout.addWidget(_selectionRadio,0,0,1,0)
        optionLayout.addWidget(_scrollBar, 1, 0)
        optionLayout.addWidget(_listTree, 1, 1)
        optionLayout.addWidget(_run, 2, 0, 2, 2)

class Run():
    def __init__(self, *args, **kwargs):
        pass

    def selection(self):
        cmds.ls(sl = True)
        cmds.ls(sl = True, dag = True, tr = True)
        cmds.ls(tr = True, v = True)


    def history(self):
        print 'history'

def main():
    window = MainWindow(qt.getMayaWindow())
    window.show()