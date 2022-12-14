# -*- coding: iso-8859-15 -*-

class BaseName(object):
    def __init__(self):
        self._object=""
        self._name=""
        self._title=""
        self._node=""
        self._side=""
        self._hierarchy="A"
        self._number=00
        self._none="none"
        self._custom=""
        # fullAuto setAuto mark replace
        self._switch="fullAuto"
        # title node side num titleNum nodeNum sideNum titleHie scene custom
        self._orders=[]
        self._find=None
        self._replace=None

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
    
    def setCustom(self,variable):
        self._custom=variable
        return self._custom
    def getCustom(self):
        return self._custom

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

    def setFind(self,variable):
        self._find=(variable)
        return self._find
    def getFind(self):
        return self._find
    
    def setReplace(self,variable):
        self._replace=(variable)
        return self._replace
    def getReplace(self):
        return self._replace

    def setCurveType(self,variable):
        self._curveType=variable
        return self._curveType
    def getCurveType(self):
        return self._curveType
class BaseObject(object):
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
class BasePair(object):
    def __init__(self):
        self._sourceNode="" # string
        self._targetNode="" # string
        self._thirdNode="" # string

        self._sourceAttr="" # string
        self._targetAttr="" # string
        self._thirdAttr="" # string
        
        self._sourceComponent=0 # int only
        self._targetComponent=0 # int only
        self._thirdComponent=0 # int only
        
        self._sourceValue="" # float or string
        self._targetValue="" # float or string
        self._thirdValue="" # float or string
        
        self._sourceJoint="" # string
        self._targetJoint="" # string
        self._thirdJoint="" # string

        self._ui=""
        
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
    
    def setThirdNode(self,variable):
        self._thirdNode=variable
        return self._thirdNode
    def getThirdNode(self):
        return self._thirdNode

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
    
    def setThirdAttr(self,variable):
        self._thirdAttr=variable
        return self._thirdAttr
    def getThirdAttr(self):
        return self._thirdAttr

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
    
    def setThirdComponent(self,variable):
        self._thirdComponent=variable
        return self._thirdComponent
    def getThirdComponent(self):
        return self._thirdComponent

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
    
    def setThirdValue(self,variable):
        self._thirdValue=variable
        return self._thirdValue
    def getThirdValue(self):
        return self._thirdValue

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
    
    def setThirdJoint(self,variable):
        self._thirdJoint=variable
        return self._thirdJoint
    def getThirdJoint(self):
        return self._thirdJoint
    
    def setUI(self,variable):
        self._ui=variable
        return self._ui
    def getUI(self):
        return self._ui
    
    def setFKCtrls(self,variable):
        self._fkCtrls=variable
        return self._fkCtrls
    def getFKCtrls(self):
        return self._fkCtrls
        
    def setIKCtrls(self,variable):
        self._ikCtrls=variable
        return self._ikCtrls
    def getIKCtrls(self):
        return self._ikCtrls
class BaseFile(object):
    def __init__(self):
        self._path=""
        self._file=""
        self._extension="json"
        self._read_dict={}
        self._readPack_dicts=[]
        self._write_dict={}
        self._writePack_dicts=[]# {"dataDict":{},"fileName":""}
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

    def setReadDict(self,variable):
        self._read_dict=variable
        return self._read_dict
    def getReadDict(self):
        return self._read_dict

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
class BasePath(object):
    def __init__(self):
        self._path=""
        self._name=""
        self._split=""
        self._index=0
        self._work_path=""
        self._def_path=""
        self._projectName_path=""

    def setPath(self,variable):
        self._path=variable
        return self._path
    def getPath(self):
        return self._path

    def setName(self,variable):
        self._name=variable
        return self._name
    def getName(self):
        return self._name

    def setSplit(self,variable):
        self._split=variable
        return self._split
    def getSplit(self):
        return self._split

    def setIndex(self,variable):
        self._index=variable
        return self._index
    def getIndex(self):
        return self._index

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
class BaseCheck(object):
    def __init__(self):
        self._relation=""
        self._same=""
        self._same_list=[]
        self._maxLimit=100
        self._minLimit=0
        self._highLimit=100
        self._lowLimit=0
        self._edit=False
        self._path=""
        self._node=""
        self._attr=""
        self._value=0

    def setRelation(self,variable):
        self._relation=variable
        return self._relation
    def getRelation(self):
        return self._relation

    def setSame(self,variable):
        self._same=variable
        return self._same
    def getSame(self):
        return self._same

    def setSameList(self,variable):
        self._same_list=variable
        return self._same_list
    def getSameList(self):
        return self._same_list

    def setMaxLimit(self,variable):
        self._maxLimit=variable
        return self._maxLimit
    def getMaxLimit(self):
        return self._maxLimit

    def setMinLimit(self,variable):
        self._minLimit=variable
        return self._minLimit
    def getMinLimit(self):
        return self._minLimit

    def setHighLimit(self,variable):
        self._highLimit=variable
        return self._highLimit
    def getHighLimit(self):
        return self._highLimit

    def setLowLimit(self,variable):
        self._lowLimit=variable
        return self._lowLimit
    def getLowLimit(self):
        return self._lowLimit

    def setEdit(self,variable):
        self._edit=variable
        return self._edit
    def getEdit(self):
        return self._edit

    def setPath(self,variable):
        self._path=variable
        return self._path
    def getPath(self):
        return self._path

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