import pymel.core as pm
import maya.mel as mel

def usdExport(path = '',name = ''):
    fullPass = path + "/" + name
    mel.eval('file -force -options "-shadowLinks 1;-mask 6399;-lightLinks 1;-fullPath" -type "Arnold-USD" -pr -ea "%s";' % fullPass)
    #mel.eval('arnoldExportAss -f "%s" -shadowLinks 1 -mask 6399 -lightLinks 1 -fullPath-cam perspShape;' % fullPass)

def main():
    scene = pm.sceneName()
    if scene == '':
        pm.error("Save the scene in a set project")
    else:
        usdExport(path = scene.dirname(),name = scene.basename())

        #Exsample
        #chengePath = scene.dirname().replace('D:/Maya', 'D:/Ritopo')
        #chengeName = scene.basename().replace('.', '_' + 'export' + '.')
        #usdExport(path = chengePath,name = chengeName)

