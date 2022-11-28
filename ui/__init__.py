import os
import glob

dirFolder=os.path.dirname(__file__)
files = glob.glob(dirFolder+"/*")
print(files)