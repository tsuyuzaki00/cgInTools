import pymel.core as pm
from mainEdit import selectAttrSaveXml as sasx
reload(sasx);

filePass = 'C:/Users/tsuyuzaki.tatsuya/Desktop/test/output.xml'
#sasx.objAttrExportXml(filePass = filePass)
sasx.objAttrImportXml(filePass = filePass)