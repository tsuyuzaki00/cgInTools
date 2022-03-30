from scriptsInTools.MayaLibrary import mayaSelectJson as msj

def main():
    
    export = msj.SelctJson(fileName = 'test', workSpacePath = 'D:/GMR/proxys')
    export.selectJsonExport()