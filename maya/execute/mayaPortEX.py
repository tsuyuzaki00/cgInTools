import sys
import maya.cmds as cmds

def main():
    if int(sys.version[0]) == 2:
        try:
            # Open new ports
            cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)
            cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)
            print("MayaPort Connected!")
        except RuntimeError:
            pass
    elif int(sys.version[0]) == 3:
        try:
            # Open new ports
            cmds.commandPort(name=":7001",sourceType="mel")
            print("MayaPort Connected!")
        except RuntimeError:
            pass
    else:
        pass