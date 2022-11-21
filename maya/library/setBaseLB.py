# -*- coding: iso-8859-15 -*-

class BaseName():
    def __init__(self):
        self._object=""
        self._name=""
        self._title=""
        self._node=""
        self._side=""
        self._hierarchy=""
        self._number=00
        self._orders=[]
        self._switch=""
        self._replace=None #(beforeName,aftarName)

    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object

    def setName(self,variable):
        self._name=variable
        return self._name
    def getName(self):
        return self._name
    
    def setTitle(self,variable):
        self._title=variable
        return self._title
    def getTitle(self):
        return self._title

    def setNode(self,variable):
        self._node=variable
        return self._node
    def getNode(self):
        return self._node

    def setSide(self,variable):
        self._side=variable
        return self._side
    def getSide(self):
        return self._side

    def setHierarchy(self,variable):
        self._hierarchy=variable
        return self._hierarchy
    def getSide(self):
        return self._hierarchy

    def setNumber(self,variable):
        self._number=variable
        return self._number
    def getNumber(self):
        return self._number

    def setOrders(self,variable):
        self._orders=variable
        return self._orders
    def getOrders(self):
        return self._orders

    def setSwitch(self,variable):
        self._switch=variable
        return self._switch
    def getSwitch(self):
        return self._switch

    def setReplace(self,variable1,variable2):
        self._replace=(variable1,variable2)
        return self._replace
    def getReplace(self):
        return self._replace

    def setCurveType(self,variable):
        self._curveType=variable
        return self._curveType
    def getCurveType(self):
        return self._curveType

class BaseObject():
    def __init__(self):
        self._object=""
        self._parent=""
        self._childs=[]
        self._shape=""
        self._component=""
        self._attr=""
        self._value=0
        self._joint=""
        self._aimVector="+X"
        self._upVector="+Y"

    def setObject(self,variable):
        self._object=variable
        return self._object
    def getObject(self):
        return self._object

    def setParent(self,variable):
        self._parent=variable
        return self._parent
    def getParent(self):
        return self._parent
    
    def setChilds(self,variable):
        self._childs=variable
        return self._childs
    def getChilds(self):
        return self._childs

    def setShape(self,variable):
        self._shape=variable
        return self._shape
    def getShape(self):
        return self._shape

    def setComponent(self,variable):
        self._component=variable
        return self._component
    def getComponent(self):
        return self._component

    def setAttr(self,variable):
        self._attr=variable
        return self._attr
    def getAttr(self):
        return self._attr

    def setValue(self,variable):
        self._value=variable
        return self._value
    def getValue(self):
        return self._value

    def setJoint(self,variable):
        self._joint=variable
        return self._joint
    def getJoint(self):
        return self._joint
    
    def setAimVector(self,variable):
        self._aimVector=variable
        return self._aimVector
    def getAimVector(self):
        return self._aimVector
    
    def setUpVector(self,variable):
        self._upVector=variable
        return self._upVector
    def getUpVector(self):
        return self._upVector

class BasePair():
    def __init__(self):
        self._sourceNode="" # string
        self._targetNode="" # string
        self._sourceAttr="" # string
        self._targetAttr="" # string
        self._sourceComponent=0 # int only
        self._targetComponent=0 # int only
        self._sourceValue="" # float or string
        self._targetValue="" # float or string
        self._sourceJoint="" # string
        self._targetJoint="" # string
        
    def setSourceNode(self,variable):
        self._sourceNode=variable
        return self._sourceNode
    def getSourceNode(self):
        return self._sourceNode

    def setTargetNode(self,variable):
        self._targetNode=variable
        return self._targetNode
    def getTargetNode(self):
        return self._targetNode

    def setSourceAttr(self,variable):
        self._sourceAttr=variable
        return self._sourceAttr
    def getSourceAttr(self):
        return self._sourceAttr

    def setTargetAttr(self,variable):
        self._targetAttr=variable
        return self._targetAttr
    def getTargetAttr(self):
        return self._targetAttr

    def setSourceComponent(self,variable):
        self._sourceComponent=variable
        return self._sourceComponent
    def getSourceComponent(self):
        return self._sourceComponent

    def setTargetComponent(self,variable):
        self._targetComponent=variable
        return self._targetComponent
    def getTargetComponent(self):
        return self._targetComponent

    def setSourceValue(self,variable):
        self._sourceValue=variable
        return self._sourceValue
    def getSourceValue(self):
        return self._sourceValue

    def setTargetValue(self,variable):
        self._targetValue=variable
        return self._targetValue
    def getTargetValue(self):
        return self._targetValue

    def setSourceJoint(self,variable):
        self._sourceJoint=variable
        return self._sourceJoint
    def getSourceJoint(self):
        return self._sourceJoint

    def setTargetJoint(self,variable):
        self._targetJoint=variable
        return self._targetJoint
    def getTargetJoint(self):
        return self._targetJoint

class BaseFile():
    def __init__(self):
        self._path=""
        self._file=""
        self._extension="json"
        self._write_dict={}
        self._writePack_dicts=[]
        self._read_dict={}
        self._readPack_dicts=[]
        self._objs=[]
        self._fileType_dict={
            "ma":"mayaAscii",
            "mb":"mayaBinary",
            "obj":"OBJ export",
            "fbx":"FBX export"
            }

    def setPath(self,variable):
        self._path=variable
        return self._path
    def getPath(self):
        return self._path

    def setFile(self,variable):
        self._file=variable
        return self._file
    def getFile(self):
        return self._file

    def setExtension(self,variable):
        self._extension=variable
        return self._extension
    def getExtension(self):
        return self._extension

    def setWriteDict(self,variable):
        self._write_dict=variable
        return self._write_dict
    def getWriteDict(self):
        return self._write_dict

    def setDictInPack(self,variable,file=None):
        file=file or self._file
        self._writePack_dicts=[{"fileName":file,"dataDict":variable}]
        return self._writePack_dicts
    def addDictInPack(self,variable,file=None):
        file=file or self._file
        self._writePack_dicts.append({"fileName":file,"dataDict":variable})
        return self._writePack_dicts
    def getPackDicts(self):
        return self._writePack_dicts

    def setFileType(self,variable):
        self._fileType=variable,self._fileType_dict[variable]
        return self._fileType
    def getFileType(self):
        return self._fileType

    def setObjs(self,variable):
        self._objs=variable
        return self._objs
    def addObjs(self,variable):
        self._objs.append(variable)
        return self._objs
    def getObjs(self):
        return self._objs

class BasePath():
    def __init__(self):
        self._absolute_path=""
        self._relative_path=""
        self._work_path=""
        self._def_path=""
        self._projectName_path=""

    def setAbsolutePath(self,variable):
        self._absolute_path=variable
        return self._absolute_path
    def getAbsolutePath(self):
        return self._absolute_path

    def setRelativePath(self,variable):
        self._relative_path=variable
        return self._relative_path
    def getRelativePath(self):
        return self._relative_path

    def setWorkPath(self,variable):
        self._work_path=variable
        return self._work_path
    def getWorkPath(self):
        return self._work_path

    def setDefPath(self,variable):
        self._def_path=variable
        return self._def_path
    def getDefPath(self):
        return self._def_path

    def setProjectName(self,variable):
        self._projectName_path=variable
        return self._projectName_path
    def getProjectName(self):
        return self._projectName_path

class BaseCheck():
    def __init__(self):
        self._same=""
        self._max=1
        self._min=0
        self._relation=""
        self._edit=False
        self._node=""
        self._attr=""
        self._value=0

    def setSame(self,variable):
        self._same=variable
        return self._same
    def getSame(self):
        return self._same

    def setMax(self,variable):
        self._max=variable
        return self._max
    def getMax(self):
        return self._max

    def setMin(self,variable):
        self._min=variable
        return self._min
    def getMin(self):
        return self._min

    def setRelation(self,variable):
        self._relation=variable
        return self._relation
    def getRelation(self):
        return self._relation

    def setEdit(self,variable):
        self._edit=variable
        return self._edit
    def getEdit(self):
        return self._edit

    def setNode(self,variable):
        self._node=variable
        return self._node
    def getNode(self):
        return self._node

    def setAttr(self,variable):
        self._attr=variable
        return self._attr
    def getAttr(self):
        return self._attr