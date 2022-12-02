import os

def main(test):
    print(test)
    root_path=os.path.dirname(__file__) #.../namingLB/
    base_str=os.path.splitext(os.path.basename(__file__))[0]#.../testPath
    dicts_path=os.path.join(root_path,"_dicts")
    print(root_path)
    print(base_str)
    print(dicts_path)