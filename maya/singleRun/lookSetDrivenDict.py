from ..library import qt
from PySide2 import QtWidgets, QtCore, QtGui
import pymel.core as pm

def lookSetDrivenAttrs(drivenName = '', driverName = '', ctrlName = ''):
    window = QtWidgets.QWidget(qt.getMayaWindow())
    window.setWindowFlags(QtCore.Qt.Window)
    window.resize(300,500)
    layout = QtWidgets.QVBoxLayout(window)
    
    widget = QtWidgets.QPlainTextEdit(window)

    drivenTrs = pm.getAttr(drivenName + '.translate')
    drivenRot = pm.getAttr(drivenName + '.rotate')
    drivenScl = pm.getAttr(drivenName + '.scale')
    widget.insertPlainText('[ ' + drivenName + ' ]' + "\n")
    widget.insertPlainText('{' + "\n")
    widget.insertPlainText("'drivenName':'" + drivenName + "'," + "\n")
    widget.insertPlainText("'drivenTrs':" + str(tuple(drivenTrs)) + "," + "\n")
    widget.insertPlainText("'drivenRot':" + str(tuple(drivenRot)) + "," + "\n")
    widget.insertPlainText("'drivenScl':" + str(tuple(drivenScl)) + "," + "\n")

    driverTrs = pm.getAttr(driverName + '.translate')
    driverRot = pm.getAttr(driverName + '.rotate')
    driverScl = pm.getAttr(driverName + '.scale')
    widget.insertPlainText("'driverName':'" + driverName + "'," + "\n")
    widget.insertPlainText("'driverTrs':" + str(tuple(driverTrs)) + "," + "\n")
    widget.insertPlainText("'driverRot':" + str(tuple(driverRot)) + "," + "\n")
    widget.insertPlainText("'driverScl':" + str(tuple(driverScl)) + "," + "\n")

    ctrlTrs = pm.getAttr(ctrlName + '.translate')
    ctrlRot = pm.getAttr(ctrlName + '.rotate')
    ctrlScl = pm.getAttr(ctrlName + '.scale')
    widget.insertPlainText("'ctrlName':'" + ctrlName + "'," + "\n")
    widget.insertPlainText("'ctrlTrs':" + str(tuple(ctrlTrs)) + "," + "\n")
    widget.insertPlainText("'ctrlRot':" + str(tuple(ctrlRot)) + "," + "\n")
    widget.insertPlainText("'ctrlScl':" + str(tuple(ctrlScl)) + "," + "\n")
    widget.insertPlainText('},' + "\n")
            
    layout.addWidget(widget)

    button = QtWidgets.QPushButton('print',window)
    layout.addWidget(button)

    button.clicked.connect(main)

    window.show()

def main():
    sels = pm.selected()
    for sel in sels:
        lookSetDrivenAttrs(drivenName = sel, driverName = 'arm_L0_5_jnt', ctrlName = 'arm_L0_fk1_ctl')

main()