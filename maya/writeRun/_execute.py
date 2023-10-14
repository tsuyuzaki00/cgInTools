# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
#from cgInTools.maya.library import _testPath as TP
from cgInTools.library import pathLB as pLB
from cgInTools.library import _testLB as tLB
from cgInTools.maya.library import dataLB as dLB
from cgInTools.maya.library import objectLB as oLB
from cgInTools.maya.library import appLB as aLB
from cgInTools.library import serializeLB as sLB
#from cgInTools.maya.manager import equipmentSettingsMN as MN
#from cgInTools.maya.option import autoRenameOP as OP
#from cgInTools.maya.execute import exportAnimPackEX as EX
cit.reloads([pLB,dLB,oLB,aLB,sLB,tLB])

def main():
    #TP.main()
    #MN.main()
    #OP.main()
    #EX.main()
    test_DataPath=pLB.DataPath()
    test_DataPath.setAbsoluteDirectory("D:/3DCG/Maya/_test/data")
    test_DataPath.setFile("test")
    test_DataPath.setExtension("selfpy")

    test_DataTest=tLB.DataTest()
    test_DataTest.setVariable("tehu")
    
    test_SelfTest=tLB.SelfTest()
    test_SelfTest.setDataTest(test_DataTest)
    test_SelfTest.setDataPath(test_DataPath)
    #test_SelfTest.setDataChoices(["DataTest"])
    test_SelfTest.writeData()

    newTest_SelfTest=tLB.SelfTest()
    newTest_SelfTest.setDataPath(test_DataPath)
    read_SelfTest=newTest_SelfTest.readData()
    print(read_SelfTest.getDataTest().getVariable())

main()