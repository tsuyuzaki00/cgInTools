import maya.cmds as cmds
import pymel.core as pm
import json
import os
import pprint

class MayaJsonMake():
    def __init__(self, jsonName):
        self.jsonName = jsonName + ".json"
        self.projectDir = cmds.workspace(q=True,rootDirectory=1)
        self.scenePath = cmds.file(q=True, sn=True)
        self.sceneDir = os.path.dirname(self.scenePath)

#create---------------------------------
    # createFolder & jsonFolderPass
    def homeJsonFolder(self):
        dataDir = self.projectDir + 'data/'
        dataFiles = os.listdir(dataDir)
        if 'json' in dataFiles:
            jsonDir = dataDir + 'json/'
        else:
            os.mkdir(dataDir + 'json')
            jsonDir = dataDir + 'json/'

        jsonFiles = os.listdir(jsonDir)
        maName = os.path.basename(self.scenePath)
        raw_name = os.path.splitext(maName)[0]
        if raw_name in jsonFiles:
            getJsons = jsonDir + raw_name + '/'
        else:
            os.mkdir(jsonDir + raw_name)
            getJsons = jsonDir + raw_name + '/'
        return getJsons

    def nullJsonCreate(self):
        loadJson = self.homeJsonFolder() + self.jsonName
        s = []
        with open(loadJson, 'w') as f:
            json.dumps(s, f, indent = 4, ensure_ascii = False)

    # load json string
    def loadJsonFolder(self):
        loadJson = self.homeJsonFolder() + self.jsonName
        with open(loadJson, 'r') as f:
            roots = json.load(f)
            return roots

#edit-----------------------------------
    # select delete list up 
    def selDelLists(self, sels = []):
        loadJson = self.homeJsonFolder() + self.jsonName
        with open(loadJson, 'r') as f:
            roots = json.load(f)
            addDel = list(set(roots[0] + sels))
            s = [addDel, roots[1]]
            with open(loadJson, 'w') as f:
                json.dump(s, f, indent = 4, ensure_ascii = False)

    # tow selects parent
    def selTwoParentLists(self, parent = '', child = ''):
        loadJson = self.homeJsonFolder() + self.jsonName
        with open(loadJson, 'r') as f:
            roots = json.load(f)
            s = [roots[0], roots[1]]
            s.append({"parent":parent,"child":child})
            with open(loadJson, 'w') as f:
                json.dump(s, f, indent = 4, ensure_ascii = False)
    
    def oneAnimJsonExport(self, sel = '', attrs = []):
        margeAttr = []
        exportAnim = {}
        for attr in attrs:
            selKeys = pm.keyframe(sel, at = attr, query = True, timeChange = True, valueChange = True)
            oneAttr = {attr : selKeys}
            margeAttr.append(oneAttr)
            exportAnim[str(sel)] = margeAttr
        return exportAnim

    def animJsonExport(self, sels = pm.selected(), attrs = ["translateX","translateY","translateZ","rotateX","rotateY","rotateZ","scaleX","scaleY","scaleZ"]):
        exportAnims = []
        for sel in sels:
            exportAnims.append(self.oneAnimJsonExport(sel = sel, attrs = attrs))
        s = exportAnims
        with open(self.homeJsonFolder() + self.jsonName, 'w') as f:
            json.dump(s, f, indent = 4, ensure_ascii = False)

    def animJsonImport(self, nameSpace = ''):
        with open(self.homeJsonFolder() + self.jsonName, 'r') as f:
            objKeys = json.load(f)
        for objKey in objKeys:
            obj = objKey.keys()
            attrs =  objKey[obj[0]]
            setKeyObj = nameSpace + obj[0]
            for attr in attrs:
                attrKey = attr.keys()
                timeValue =  attr[attrKey[0]]
                for time,value in timeValue:
                    pm.setKeyframe(setKeyObj, t = time, v = value, at = attrKey)


#renameKeys = [("motion","C_model_geo_test_02"),("C_model_geo_test_01","C_model_geo_test_03"),]
    def objChengeJsonImport(self, renameKeys, default_value=None):
        with open(self.homeJsonFolder() + self.jsonName, 'r') as f:
            objKeys = json.load(f)
            for objKey in objKeys:
                for old_name, new_name in renameKeys:
                    obj = objKey.keys()
                    if str(obj[0]) == old_name:
                        renameObj = str(obj[0]).replace(old_name, new_name)
                    attrs =  objKey[obj[0]]
                    for attr in attrs:
                        attrKey = attr.keys()
                        timeValue =  attr[attrKey[0]]
                        for time,value in timeValue:
                            pm.setKeyframe(renameObj, t = time, v = value, at = attrKey)

class MayaJsonRun():
    def __init__(self, mayaName):
        self.mayaName = mayaName
    # read json run
    def animEXFile(self, deleteLists = [], parentList = []):
        cmds.file(save=True, force=True)
        cmds.file(rename = self.sceneDir + '/' + self.mayaName)
        for deleteList in deleteLists:
    	        cmds.delete(deleteList)
        cmds.parent(parentList["child"], parentList["parent"])
        cmds.file(save=True, force=True)
