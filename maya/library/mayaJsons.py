import maya.cmds as cmds
import json
import os

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