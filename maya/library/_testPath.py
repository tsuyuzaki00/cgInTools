import os

def main():
    print(__file__.split("\\")[-1])
    print(__file__.split("\\")[:-1])
    rootPath=os.path.dirname(__file__) #.../library
    baseFile=os.path.splitext(os.path.basename(__file__))[0]#_testPath
    dictsPath=os.path.join(rootPath,"_dicts")
    print(rootPath)
    print(baseFile)
    print(dictsPath)