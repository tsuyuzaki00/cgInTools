import maya.cmds as cmds

def OKList(sel, check):
    print 'OK' + ' : ' + check + ' : ' + sel
def NGList(sel, check, text):
    print 'NG' + ' : ' + check + ' : ' + sel + ' ' + text

def defaultMatrialCheck(sels):
    check = 'DefaultMatrial'
    for sel in sels:
        shaders = cmds.listConnections(cmds.listHistory(sel,f=1), type = 'lambert')
        if shaders == None:
            cmds.error('No Matrial')
        else :
            for shaderName in shaders:
                i = shaderName.split('|')[-1]
                cmds.select(cl = True)
                if 'lambert1' in i:
                    cmds.select(sel, add = True)
                    NGList(shaderName, check, 'Please change material')
                elif 'blinn' in i or 'lambert' in i:
                    cmds.select(shaderName, add = True)
                    NGList(shaderName, check, 'Please Rename the material')
                else :
                    OKList(shaderName, check)
            
            
def main():
    sels = cmds.ls(sl = True)
    defaultMatrialCheck(sels)

main()