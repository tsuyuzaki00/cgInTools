# -*- coding: iso-8859-15 -*-
import maya.cmds as cmds
import maya.api.OpenMaya as om2

import cgInTools as cit
from ...library import baseLB as bLB
from ..library import dataLB as dLB
from ..library import selfLB as sLB
from ..library import nodeLB as nLB
from ..library import matrixLB as mLB
cit.reloads([bLB,dLB,sLB,nLB,mLB])

def main():
    normal_matrix=cmds.getAttr("pCone2.worldMatrix[0]")
    parentInverse_matrix=cmds.getAttr("pCone2.parentInverseMatrix[0]")

    main_DataMatrix=dLB.DataMatrix()
    main_DataMatrix.setMatrix(normal_matrix)

    parentInverse_DataMatrix=dLB.DataMatrix()
    parentInverse_DataMatrix.setMatrix(parentInverse_matrix)

    main_DataMatrix*=parentInverse_DataMatrix
    #test_AppMatrix=mLB.AppMatrix()
    #test_AppMatrix.setDataMatrix(main_DataMatrix)
    #test_AppMatrix.setSubjectDataMatrix(parentInverse_DataMatrix)
    #test_AppMatrix.mirror().getMatrix()

main()