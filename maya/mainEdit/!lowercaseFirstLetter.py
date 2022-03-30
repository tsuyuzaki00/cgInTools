import pymel.core as pm
    
def check(str):
    str = str[0].lower() + str[1:]
    return str

def main():
    test = check('Test')
    print test

main()