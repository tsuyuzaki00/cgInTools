# -*- coding: iso-8859-15 -*-

class Tree():
    def __init__(self):
        self._parent=""
        self._me=""
        self._childs=[]

    def setMe(self,variable):
        self._me=variable
        return self._me
    def getMe(self):
        return self._me

    def setParent(self,variable):
        self._parent=variable
        return self._parent
    def getParent(self):
        return self._parent
    
    def setChilds(self,variable):
        self._childs=variable
        return self._childs
    def getChilds(self):
        return self._childs


def parentTree_query_dict(chara_list):
    result={}
    for chara in chara_list:
        if chara.getParent() == "":
            result["root"]=[chara.getMe()]
        else:
            if chara.getParent() in result:
                result[chara.getParent()].append(chara.getMe())
            else:
                result[chara.getParent()]=[chara.getMe()]
                
    return result

def main():
    root=Tree()
    root.setMe("dolphin")
    root.setChilds("olimar")

    olimar=Tree()
    olimar.setParent("dolphin")
    olimar.setMe("olimar")
    olimar.setChilds(["red","blue","yellow"])

    red=Tree()
    red.setParent("olimar")
    red.setMe("red")

    blue=Tree()
    blue.setParent("olimar")
    blue.setMe("blue")

    yellow=Tree()
    yellow.setParent("olimar")
    yellow.setMe("yellow")

    chara_list=[red,blue,yellow,root,olimar]
    print(parentTree_query_dict(chara_list))

main()