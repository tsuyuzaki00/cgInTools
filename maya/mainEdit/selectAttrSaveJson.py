import pymel.core as pm
import json
from collections import OrderedDict as od
import pprint

def objAttrExportJson(filePass = ''):
    
    sels = pm.selected()
    for sel in sels:
        date = {}
        
        pm.select(sel)
        selLists = pm.listAttr(k=True)
        s = {"object": { "node":[{ "name" : str(sel), "attrbute":[{}]}]}}
        for selList in selLists:
            selAttr = pm.getAttr(sel + '.' + selList)
            s['object']['node'][0]['attrbute'][0]['string'] = str(selList)
            s['object']['node'][0]['attrbute'][0]['value'] = str(round(selAttr, 3))

            #pprint.pprint(s, width = 40)
        with open(filePass, 'w') as f:
            json.dump(s, f, indent = 4, ensure_ascii =False)

def objAttrImportJson(filePass = ''):
    with open(filePass, 'r') as f:
        root = json.load(f)
        #pprint.pprint(root, width=40)
        nodes = root['object']['node']
        for node in nodes:
            attrs = node['attrbute']
            for attr in attrs:

                pm.select(node['name'])
                pm.setAttr(node['name'] + '.' + attr['string'], float(attr['value']))

def main():
    filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.json'
    objAttrExportJson(filePass = filePass)
    objAttrImportJson(filePass = filePass)

filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.json'
objAttrExportJson(filePass = filePass)
#objAttrImportJson(filePass = filePass)