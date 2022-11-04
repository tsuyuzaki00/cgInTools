import cgInTools as cit
from cgInTools.maya.library import jsonLB as cj
from cgInTools.maya.execute import selectCornerEdgeEX as ex

def main():
    write_dict={
    "lowAngle":45,
    "highAngle":180
    }
    setting=cj.Json()
    setting.setPath(cit.mayaData_path)
    setting.setFile("selectCornerEdge")
    setting.setWriteDict(write_dict)
    setting.write()
    ex.main()