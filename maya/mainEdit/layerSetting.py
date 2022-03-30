import os, json
from PySide2 import QtWidgets, QtGui
from mainEdit import qt
import pymel.core as pm

class Settings(object):
    def __init__(self):
        temp = __name__.split('.')
        self.__filename = os.path.join(
			os.getenv('MAYA_APP_DIR'),
			temp[0],
			temp[-1]+'.json'
			)
        self.reset()
        self.read()
        
    def read(self):
        if os.path.exists(self.__filename):
            with open(self.__filename, 'r') as f:
                saveData = json.load(f)
                #self.guide = saveData['guide']
                #self.geometry = saveData['geometry']
                #self.joint = saveData['joint']
                #self.ctrl = saveData['ctrl']
                #self.camera = saveData['camera']
                #self.light = saveData['light']
    
    def reset(self):
        self.guide = False
        self.geometry = True
        self.joint = False
        self.ctrl = False
        self.camera = False
        self.light = False
        
    def save(self):
        saveData = { #'guide':self.guide,
                    #'geometry':self.geometry
                    #'joint':self.joint
                    #'ctrl':self.ctrl
                    #'camera':self.camera
                    #'light':self.light
                    }
        if not os.path.exists(self.__filename):
            os.makedirs(os.path.dirname(self.__filename))
        with open(self.__filename, 'w') as f:
            json.dump(saveData, f)

settings = Settings()

class OptionWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(OptionWidget, self).__init__(*args, **kwargs)
        mainLayout = QtWidgets.QFormLayout(self)

        self.__guide = QtWidgets.QCheckBox('guide', self)
        mainLayout.addRow('', self.__guide)

        self.__geometry = QtWidgets.QCheckBox('geometry', self)
        mainLayout.addRow('', self.__geometry)

        self.__joint = QtWidgets.QCheckBox('joint', self)
        mainLayout.addRow('', self.__joint)

        self.__ctrl = QtWidgets.QCheckBox('ctrl', self)
        mainLayout.addRow('', self.__ctrl)

        self.__camera = QtWidgets.QCheckBox('camera', self)
        mainLayout.addRow('', self.__camera)

        self.__light = QtWidgets.QCheckBox('light', self)
        mainLayout.addRow('', self.__light)

        self.initialize()

    def initialize(self):
        self.__guide.setChecked(settings.guide)
        self.__geometry.setChecked(settings.geometry)
        self.__joint.setChecked(settings.joint)
        self.__ctrl.setChecked(settings.ctrl)
        self.__camera.setChecked(settings.camera)
        self.__light.setChecked(settings.light)

    def resetSettings(self):
        settings.reset()
        self.initialize()

    def saveSettings(self):
        settings.guide = self.__guide.isChecked()
        settings.geometry = self.__geometry.isChecked()
        settings.joint = self.__joint.isChecked()
        settings.ctrl = self.__ctrl.isChecked()
        settings.camera = self.__camera.isChecked()
        settings.light = self.__light.isChecked()
        settings.save()

    def apply(self):
        self.saveSettings()
        main()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle('layerSetting')
        self.resize(400, 210)

        toolWidget = qt.ToolWidget(self)
        self.setCentralWidget(toolWidget)

        optionWidget = OptionWidget(self)
        toolWidget.setOptionWidget(optionWidget)

        toolWidget.setActionName(self.windowTitle())
        toolWidget.applied.connect(qt.Callback(optionWidget.apply))
        toolWidget.closed.connect(self.close)

        menuBar = self.menuBar()
        menu = menuBar.addMenu('File')
        action = menu.addAction('Save Settings')
        action.triggered.connect(optionWidget.saveSettings)

        action = menu.addAction('Reset Settings')
        action.triggered.connect(optionWidget.resetSettings)
		
def layerSetting(guide = True, geometry = True, joint = True, ctrl = True, camera = True, light = True):
    sceneName = pm.sceneName().basename()
    part = sceneName.split("_")
    
    if part[0].endswith('.ma') or part[0].endswith('.mb'):
        name = part[0][:-3]
    elif part[0] == '':
        name = 'scene'
    else:
        name = part[0]
    
    if guide == True or geometry == True or joint == True or ctrl == True or camera == True or light == True:
        if pm.objExists(name) == False:
            allGrp = pm.createNode('transform', n = name)
        else :
            allGrp = name

        if guide:
            if pm.objExists( '_'.join(['grp','gud',name]) ):
                pm.warning( "Group already exists" )
                return
            guideGrp = pm.createNode( 'transform', n = '_'.join(['grp','gud',name]) )
            pm.parent(guideGrp, allGrp)

            pm.select(all = True)
            getimage = pm.listRelatives(type='imagePlane')
            getTrs = pm.listRelatives(getimage, p = True)
            pm.select(cl = True)
            for i in getTrs:
                pm.parent(i, guideGrp)

            if pm.objExists( '_'.join(['gud',name,'layer']) ):
                guideLayer = '_'.join( ['gud',name,'layer'] )
                pm.editDisplayLayerMembers(guideLayer, guideGrp)
            else :
                guideLayer = pm.createDisplayLayer(n = '_'.join( ['gud',name,'layer'] ))
                pm.editDisplayLayerMembers(guideLayer, guideGrp)
        
        if geometry:
            if pm.objExists( '_'.join(['grp','geo',name]) ):
                pm.warning( "Group already exists" )
                return
            geoGrp = pm.createNode( 'transform', n = '_'.join(['grp','geo',name]) )
            pm.setAttr('grp_geo_' + name + '.inheritsTransform', 0)
            pm.parent(geoGrp, allGrp)

            pm.select(all = True)
            getMesh = pm.listRelatives(type='mesh')
            getTrs = pm.listRelatives(getMesh, p = True)
            pm.select(cl = True)
            for i in getTrs:
                pm.parent(i, geoGrp)

            if pm.objExists( '_'.join(['geo',name,'layer']) ):
                geometryLayer = '_'.join( ['geo',name,'layer'] )
                pm.editDisplayLayerMembers(geometryLayer, geoGrp)
            else :
                geometryLayer = pm.createDisplayLayer(n = '_'.join(['geo',name,'layer'] ))
                pm.editDisplayLayerMembers(geometryLayer, geoGrp)

        if joint:
            if pm.objExists( '_'.join(['grp','jnt',name]) ):
                pm.warning( "Group already exists" )
                return
            jointGrp = pm.createNode( 'transform', n = '_'.join( ['grp','jnt',name]) )
            pm.parent(jointGrp, allGrp)

            if pm.objExists( '_'.join(['jnt',name,'layer']) ):
                jointLayer = '_'.join( ['jnt',name,'layer'] )
                pm.editDisplayLayerMembers(jointLayer, jointGrp)
            else :
                jointLayer = pm.createDisplayLayer(n = '_'.join(['jnt',name,'layer']) )
                pm.editDisplayLayerMembers( jointLayer, jointGrp )

        if ctrl:
            if pm.objExists( '_'.join(['grp','ctrl',name]) ):
                pm.warning( "Group already exists" )
                return
            ctrlGrp = pm.createNode( 'transform', n = '_'.join( ['grp','ctrl',name]) )
            pm.parent(ctrlGrp, allGrp)

            if pm.objExists( '_'.join(['ctrl',name,'layer']) ):
                ctrlLayer = '_'.join( ['ctrl',name,'layer'] )
                pm.editDisplayLayerMembers(ctrlLayer, jointGrp)
            else :
                ctrlLayer = pm.createDisplayLayer( n = '_'.join(['ctrl',name,'layer']) )
                pm.editDisplayLayerMembers( ctrlLayer, ctrlGrp )

        if camera:
            if pm.objExists( '_'.join(['grp','cam',name]) ):
                pm.warning( "Group already exists" )
                return
            cameraGrp = pm.createNode( 'transform', n = '_'.join( ['grp','cam',name]) )
            pm.parent( cameraGrp, allGrp )

            pm.select(all = True)
            getCam = pm.listRelatives(type='camera')
            getTrs = pm.listRelatives(getCam, p = True)
            pm.select(cl = True)
            for i in getTrs:
                pm.parent(i, cameraGrp)

            if pm.objExists( '_'.join(['cam',name,'layer']) ):
                cameraLayer = '_'.join( ['cam',name,'layer'] )
                pm.editDisplayLayerMembers(cameraLayer, cameraGrp)
            else :
                cameraLayer = pm.createDisplayLayer( n = '_'.join(['cam',name,'layer']) )
                pm.editDisplayLayerMembers( cameraLayer, cameraGrp )

        if light:
            if pm.objExists( '_'.join(['grp','lit',name]) ):
                pm.warning( "Group already exists" )
                return
            lightGrp = pm.createNode( 'transform', n = '_'.join( ['grp','lit',name]) )
            pm.parent( lightGrp, allGrp )

            pm.select(all = True)
            getSlt = pm.listRelatives(type = 'spotLight')
            getTrs = pm.listRelatives(getSlt, p = True)
            pm.select(cl = True)
            for i in getTrs:
                pm.parent(i, lightGrp)

            pm.select(all = True)
            getSlt = pm.listRelatives(type = 'ambientLight')
            getTrs = pm.listRelatives(getSlt, p = True)
            pm.select(cl = True)
            for i in getTrs:
                pm.parent(i, lightGrp)

            pm.select(all = True)
            getSlt = pm.listRelatives(type = 'pointLight')
            getTrs = pm.listRelatives(getSlt, p = True)
            pm.select(cl = True)
            for i in getTrs:
                pm.parent(i, lightGrp)

            pm.select(all = True)
            getSlt = pm.listRelatives(type = 'directionalLight')
            getTrs = pm.listRelatives(getSlt, p = True)
            pm.select(cl = True)
            for i in getTrs:
                pm.parent(i, lightGrp)

            if pm.objExists( '_'.join(['lit',name,'layer']) ):
                lightLayer = '_'.join(['lit',name,'layer'] )
                pm.editDisplayLayerMembers( lightLayer, lightGrp )
            else :
                lightLayer = pm.createDisplayLayer(n = '_'.join(['lit',name,'layer'] ))
                pm.editDisplayLayerMembers( lightLayer, lightGrp )

def option():
    window = MainWindow(qt.getMayaWindow())
    window.show()
    
def main():
	layerSetting(
        settings.guide,
        settings.geometry,
        settings.joint,
        settings.ctrl,
        settings.camera,
        settings.light
        )