import pymel.core as pm
import os

def main():
    #test = "%s/%s.png"%(os.path.dirname(__file__), "perryToolLogo")
    test2 = pm.env.envVars
    for v in test2.values():
        print(v)
    #parts = test2.split(",")
    #for part in parts:
    #    print part
    