import pymel.core as pm

class ErrorStop:    
    def nameCover(self, there):
        allSel = pm.select(hi = True, ado = True)
        allCheck = pm.selected()
        pm.select(cl = True)
        
        for check in allCheck:
            if check == there:
                pm.error('It stopped because double name clash')

    def pleaseSelect(self,sel):
        if sel == []:
            pm.error('Please select an object')
    
    def selectOnlyOne(self,sel):
        if pm.selected()[1:]:
            pm.error('Please select only one')
            
    def selectOnlyTwo(self,sel):
        if pm.selected()[2:]:
            pm.error('Please select only two')

errorStop = ErrorStop()