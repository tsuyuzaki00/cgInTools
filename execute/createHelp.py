import os
import inspect

import cgInTools as cit
#from cgInTools.maya.execute import infJntRemoveEditEX as EX; cit.reloads([EX])
from cgInTools.maya.library import jsonLB as LB; cit.reloads([LB])
#from cgInTools.maya.manager import skinWeightByJointMN as MN; cit.reloads([MN])
#from cgInTools.maya.option import autoRenameOP as OP; cit.reloads([OP])

texts=""
for text in inspect.getmembers(LB,inspect.ismethod):
    print(text)

filePath=os.path.join(cit.execute_path,"help.md")

#with open(filePath,'w') as file:
#        file.write(str(texts))