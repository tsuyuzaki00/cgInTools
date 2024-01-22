# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import dataLB as dLB
from ...library import baseLB as bLB
cit.reloads([bLB])

class DataTest(object):
    def __init__(self):
        self._test_int=None

    def setTest(self,variable):
        self._test_int=variable
        return self._test_int
    def getTest(self):
        return self._test_int
        

class SelfTest(bLB.SelfOrigin):
    def __init__(self,selfTest=None):
        super(SelfTest,self).__init__()
        if selfTest is None:
            self._test_DataTest=None
        elif type(selfTest) is SelfTest:
            self._test_DataTest=selfTest.getDataTest()

    def setDataTest(self,variable):
        self._test_DataTest=variable
        return self._test_DataTest
    def getDataTest(self):
        return self._test_DataTest
    
    def test(self):
        test1=eval('self.getDataTest()')
        print(test1)

def main():
    test_DataPath=dLB.DataPath()
    test_DataPath.setAbsoluteDirectory("D:/3DCG/Maya/_test/scripts/cgInToolsData")
    test_DataPath.setFile("test")
    test_DataPath.setExtension("selfpy")

    #test_DataTest=DataTest()
    #test_DataTest.setTest(0)

    test_SelfTest=SelfTest()
    test_SelfTest.setDataPath(test_DataPath)
    #test_SelfTest.setDataTest(test_DataTest)
    test_SelfTest.readData()
    print(test_SelfTest.getDataTest().getTest())
    

main()