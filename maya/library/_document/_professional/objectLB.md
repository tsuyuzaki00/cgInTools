# objectLB

[一般向け(person)](/maya/library/_document/objectLB.md)

## クラス一覧
[SelfOrigin(object)](#selforigin)

[SelfNode(SelfOrigin)](#selfnode)

[SelfConnectNode(SelfNode)](#selfconnectnode)

[SelfDagNode(SelfNode)](#selfdagnode)

[SelfComponent(SelfOrigin)](#selfcomponent)

[SelfMatrixNode(SelfDagNode)](#selfmatrixnode)

[SelfLocationNode(SelfMatrixNode)](#selflocationnode)

[SelfAnimNode(SelfMatrixNode)](#selfanimnode)

[SelfWeightJoint(SelfConnectNode)](#selfweightjoint)

[SelfPolygon(SelfMatrixNode)](#selfpolygon)

[SelfSurface(SelfMatrixNode)](#selfsurface)

[SelfCreateNode(SelfOrigin)](#selfcreatenode)

<a id="selforigin"></a>
# class SelfOrigin

Inheritance : object

Summary : データを取得してアクションをするの指示が入っているクラス

## Single Function

None

## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

def [setReadDict()](#setreaddict)

def [getReadDict()](#getreaddict)

def [setSetChoices()](#setsetchoices)

def [getSetChoices()](#getsetchoices)

def [setDoIts()](#setdoits)

def [getDoIts()](#getdoits)

## Public Function

def [writeDict()](#writedict)

def [readDict()](#readdict)

def [doIt()](#doit)

<a id="selfnode"></a>
# class SelfNode

Inheritance : [SelfOrigin](#selforigin)

Summary : 自立ノードの原点

## Single Function
def [selectNode_create_MObject()](#selectnode_create_mobject)

def [nodeType_query_str()](#nodetype_query_str)

def [nodeAttr_create_MPlug()](#nodeattr_create_mplug)

def [editAttr_edit_func()](#editattr_edit_func)

def [queryAttr_query_value()](#queryattr_query_value)

## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

def [setNode()](#setnode)

def [getNode()](#getnode)

def [setAttr()](#setattr)

def [getAttr()](#getattr)

def [setValue()](#setvalue)

def [getValue()](#getvalue)

## Public Function

def [editAttr()](#editattr)

def [queryAttr()](#queryattr)

def [queryNodeType()](#querynodetype)

<a id="selfcomponent"></a>
# class SelfComponent

Inheritance : [SelfOrigin](#selforigin)

Summary : コンポーネントID(頂点、エッジ、面など)に関するクラス

## Single Function

def [selectComponent_create_MDagPath_MObject()](#selectcomponent_create_mdagpath_mobject)

def [shape_create_MDagPath()](#shape_create_mdagpath)

def [convertToInt_create_MObject()](#converttoint_create_mobject)

def [componentID_query_int()](#componentid_query_int)

def [shapeType_query_str()](#shapetype_query_str)

## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

def [setComponent()](#setcomponent)

def [setMFn()](#setmfn)

def [getMFn()](#getmfn)

def [setShape()](#setshape)

def [getShape()](#getshape)

def [setComponentID()](#setcomponentid)

def [getComponentID()](#getcomponentid)

## Public Function

def [queryShapeType()](#queryshapetype)

<a id="selfconnectnode"></a>
# class SelfConnectNode

Inheritance : [SelfNode](#selfnode)

Summary : DG(Dependency Graph) アトリビュート同士を接続に関するクラス

## Single Function
def [replaceMObjectToNode_query_strs()](#replacemobjecttonode_query_strs)

def [connectionNode_query_MPlugs()](#connectionnode_query_mplugs)

## Multi Function

def [_findType_query_MObjects()](#_findtype_query_mobjects)

## Private Function

def [_findAttrConect_query_MObjects()](#_findattrconect_query_mobjects)

def [_nodeTypeToMFnConverter_query_int()](#_nodetypetomfnconverter_query_int)

## Summary Function

None

## Setting Function

def [setOperationNode()](#setoperationnode)

def [getOperationNode()](#getoperationnode)

def [setOperationAttr()](#setoperationattr)

def [getOperationAttr()](#getoperationattr)

def [setFindType()](#setfindtype)

def [getFindType()](#getfindtype)

def [setFindEnum()](#setfindenum)

def [getFindEnum()](#getfindenum)

def [setFindSource()](#setfindsource)

def [getFindSource()](#getfindsource)

def [setFindTarget()](#setfindtarget)

def [getFindTarget()](#getfindtarget)

## Public Function

def [connectAttr()](#connectattr)

def [queryConnectionNodes()](#queryconnectionnodes)

def [queryConnectionNodeAttrToFind()](#queryconnectionnodeattrtofind)

def [queryConnectionNodeTypeOrMFnToFind()](#queryconnectionnodetypeormfntofind)

<a id="selfdagnode"></a>
# class SelfDagNode

Inheritance : [SelfNode](#selfnode)

Summary : DAG(Directed Acyclic Graph) 階層に関するクラス

## Single Function

def [convertMObject_create_MDagPath()](#convertmobject_create_mdagpath)

def [fullPath_query_str()](#fullpath_query_str)

def [shape_query_MObject()](#shape_query_mobject)

def [parent_query_MObject()](#parent_query_mobject)

def [child_query_MObjects()](#child_query_mobjects)

def [nodeTypes_query_strs()](#nodetype_query_strs)

## Multi Function

def [_fullPathSwitch_query_str()](#_fullpathswitch_query_str)

## Private Function

def [_fullPathSwitch_query_strs()](#_fullpathswitch_query_strs)

## Summary Function

None

## Setting Function

def [setFullPath()](#setfullpath)

def [getFullPath()](#getfullpath)

def [setFirstOnly()](#setfullpath)

def [getFirstOnly()](#getfullpath)

def [setFirstAddress()](#setfullpath)

def [getFirstAddress()](#getfullpath)

def [getNode()](#getnode-selfdagnode)

def [senDoParent()](#setdoparent)

def [getDoParent()](#getdoparent)

## Public Function

def [parent()](#parent)

def [replaceByParent()](#replacebyparent)

def [replaceByChild()](#replacebychild)

def [replaceByShape()](#replacebyshape)

def [queryShape()](#queryshape)

def [queryShapes()](#queryshapes)

def [queryShapeType()](#queryshapetype)

def [queryShapeTypes()](#queryshapetypes)

def [queryParent()](#queryparent)

def [queryChilds()](#querychilds)

<a id="selfmatrixnode"></a>
# class SelfMatrixNode

Inheritance : [SelfDagNode](#selfdagnode)

Summary : マトリクスに関するクラス

## Single Function

def [vector3_check_vector3()](#vector3_check_vector3)

def [initialNoneMMatrix_check_MMatrix()](#initialnonemmatrix_check_mmatrix)

## Multi Function

None

## Private Function

def [_nodeToNormalMMatrix_query_MMatrix()](#_nodetonormalmmatrix_query_mmatrix)

def [_nodeToWorldMMatrix_query_MMatrix()](#_nodetoworldmmatrix_query_mmatrix)

def [_nodeToParentMMatrix_query_MMatrix()](#_nodetoparentmmatrix_query_mmatrix)

def [_nodeToInverseNormalMMatrix_query_MMatrix()](#_nodetoinversenormalmmatrix_query_mmatrix)

def [_nodeToInverseWorldMMatrix_query_MMatrix()](#_nodetoinverseworldmmatrix_query_mmatrix)

def [_nodeToInverseParentMMatrix_query_MMatrix()](#_nodetoinverseparentmmatrix_query_mmatrix)

## Summary Function

None

## Setting Function

def [setNode()](#setnode-selfmatrixnode)

def [setMatrix()](#setmatrix)

def [getMatrix()](#getmatrix)

def [setMSpace()](#setmspace)

def [getMSpace()](#getmspace)

def [currentNormalMMatrix()](#currentnormalmmatrix)

def [currentWorldMMatrix()](#currentworldmmatrix)

def [currentParentMMatrix()](#currentparentmmatrix)

def [currentInverseNormalMMatrix()](#currentinversenormalmmatrix)

def [currentInverseWorldMMatrix()](#currentinverseworldmmatrix)

def [currentInverseParentMMatrix()](#currentinverseparentmmatrix)

def [setTranslateMMatrix()](#settranslatemmatrix)

def [addTranslateMMatrix()](#addtranslatemmatrix)

def [getTranslateMMatrix()](#gettranslatemmatrix)

def [setRotateMMatrix()](#setrotatemmatrix)

def [addRotateMMatrix()](#addrotatemmatrix)

def [getRotateMMatrix()](#getrotatemmatrix)

def [setQuaternionMMatrix()](#setquaternionmmatrix)

def [addQuaternionMMatrix()](#addquaternionmmatrix)

def [getQuaternionMMatrix()](#getquaternionmmatrix)

def [setAxisAngleMMatrix()](#setaxisanglemmatrix)

def [addAxisAngleMMatrix()](#addaxisanglemmatrix)

def [getAxisAngleMMatrix()](#getaxisanglemmatrix)

def [setScaleMMatrix()](#setscalemmatrix)

def [addScaleMMatrix()](#addscalemmatrix)

def [getScaleMMatrix()](#getscalemmatrix)

## Public Function

def [queryDirectionX()](querydirectionx)

def [queryDirectionY()](querydirectiony)

def [queryDirectionZ()](querydirectionz)

<a id="selflocationnode"></a>
# class SelfLocationNode

Inheritance : [SelfMatrixNode](#selfmatrixnode)

Summary : 移動、回転、スケールに関するクラス

## Single Function

None

## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

def [setMatchNode()](#setmatchnode)

def [getMatchNode()](#getmatchnode)

## Public Function

def [matchToTranslateNode()](#matchtotranslatenode)

def [matchToRotateNode()](#matchtorotatenode)

def [matchToQuaternionNode()](#matchtoquaternionnode)

def [matchToScaleNode()](#matchtoscalenode)

def [translate()](#translate)

def [rotate()](#rotate)

def [quaternion()](#quaternion)

def [scale()](#scale)

def [addParentNull()](#addparentnull)

def [addOffsetNull()](#addoffsetnull)



<a id="selfanimnode"></a>
# class SelfAnimNode

Inheritance : SelfNode

Summary : アニメーションキーに関するクラス

## Single Function

None
## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

None

## Public Function

None

<a id="selfweightjoint"></a>
# class SelfWeightJoint

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を繋げる用のノード

## Single Function

None
## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

None

## Public Function

None

<a id="selfpolygon"></a>
# class SelfPolygon

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を繋げる用のノード

## Single Function

None
## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

None

## Public Function

None

<a id="selfsurface"></a>
# class SelfSurface

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を繋げる用のノード

## Single Function

None
## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

None

## Public Function

None

<a id="selfcreatenode"></a>
# class SelfCreateNode

Inheritance : SelfNode

Summary : 

## Single Function

None
## Multi Function

None

## Private Function

None

## Summary Function

None

## Setting Function

None

## Public Function

None

# Functions
# class SelfOrigin

<a id="setreaddict"></a>
## def setReadDict()

Parameters : variable=dict ({Setting Function name : value})

Returns : None

Documents : 辞書を使ってSelfクラスにパラメータを設定する関数

<a id="getreaddict"></a>
## def getReadDict()

Parameters : None

Returns : dict ({Setting Function name : value})

Documents : 設定した辞書を取得する関数

<a id="setsetchoices"></a>
## def setSetChoices()

Parameters : variables=list (Setting Function names)

Returns : None

Documents : listを使って書き出すデータを決める関数

<a id="getsetchoices"></a>
## def getSetChoices()

Parameters : None

Returns : list (Setting Function names)

Documents : 書き出すデータのリストを取得する関数

<a id="setdoits"></a>
## def setDoIts()

Parameters : variables=list (Public Function names)

Returns : None

Documents : listを使って実行する関数を設定する関数

<a id="getdoits"></a>
## def getDoIts()

Parameters : None

Returns : list (Public Function names)

Documents : 実行させる関数たちを確認する関数

<a id="writedict"></a>
## def writeDict()

Parameters : setChoices=list (Setting Function names)

Returns : None

Documents : 設定したget関数を取得してdict形式で書き出す関数

<a id="readdict"></a>
## def readDict()

Parameters : read_dict=dict ({Setting Function name : value,...})

Returns : None

Documents : 辞書を読み込み任意のset関数に割り当てる関数

<a id="doit"></a>
## def doIt()

Parameters : doIts=list (Public Function names)

Returns : None

Documents : 設定した関数を実行する関数

# class SelfNode

<a id="selectnode_create_mobject"></a>
## def selectNode_create_MObject()

Parameters : str (node name)

Returns : maya.api.OpenMaya.MObject

Documents : 存在するノード名をMObjectに変換する関数

<a id="nodetype_query_str"></a>
## def nodeType_query_str()

Parameters : MObject=maya.api.OpenMaya.MObject

Returns : str (node type)

Documents : MObjectからノードタイプを取得する関数

<a id="nodeattr_create_mplug"></a>
## def nodeAttr_create_MPlug()

Parameters : MObject=maya.api.OpenMaya.MObject,attr=str(attribute name)

Returns : maya.api.OpenMaya.MPlug

Documents : MObjectをMPlugに変換する関数

<a id="editattr_edit_func"></a>
## def editAttr_edit_func()

Parameters : MPlug=maya.api.OpenMaya.MPlug,value=single variable

Returns : None

Documents : MPlugに対して設定したvalueに変更する関数

<a id="queryattr_query_value"></a>
## def queryAttr_query_value()

Parameters : MPlug=maya.api.OpenMaya.MPlug,type=single variable name("double")

Returns : single variable

Documents : MPlugに設定されている値を取得する関数

<a id="setnode"></a>
## def setNode()

Parameters : str(node name)

Returns : None

Documents : 自身のノードを変更する関数

<a id="getnode"></a>
## def getNode()

Parameters : fullPath=bool

Returns : str(node name)

Documents : 自身のノード名を返す関数

<a id="setattr"></a>
## def setAttr()

Parameters : str (attribute name)

Returns : None

Documents : 自身が何のアトリビュートを所持しているかを決める関数

<a id="getattr"></a>
## def getAttr()

Parameters : None

Returns : str (attribute name)

Documents : 自身が何のアトリビュートを所持しているかを返す関数

<a id="setvalue"></a>
## def setValue()

Parameters : single variable

Returns : None

Documents : 自身が何の値を所持しているかを決める関数

<a id="getvalue"></a>
## def getValue()

Parameters : None

Returns : single variable

Documents : 自身が何の値を所持しているかを返す関数

<a id="setvaluetype"></a>
## def setValueType()

Parameters : str (single variable)

Returns : None

Documents : single valueを"double","bool","int","float","string"のいずれかで返すように設定する関数

<a id="getvaluetype"></a>
## def getValueType()

Parameters : None

Returns : str (single variable)

Documents : single valueに設定したタイプを返す関数

<a id="editattr"></a>
## def editAttr()

Parameters : attr_str=str(attribute name),value=single variable

Returns : None

Documents : 設定した値を使用して設定したアトリビュートを変更する関数

<a id="queryattr"></a>
## def queryAttr()

Parameters : attr_str=str(attribute name),valueType_str=str(single variable name)

Returns : single variable

Documents : 設定したアトリビュートの値を返す関数

<a id="querynodetype"></a>
## def queryNodeType()

Parameters : None

Returns : str(node type)

Documents : 自身のノードタイプを返す関数

# class SelfComponent

<a id="selectcomponent_create_mdagpath_mobject"></a>
## def selectComponent_create_MDagPath_MObject()

Parameters : None

Returns : None

Documents : 関数

<a id="shape_create_mdagpath"></a>
## def shape_create_MDagPath()

Parameters : None

Returns : None

Documents : 関数

# class SelfConnectNode

<a id="connectionnode_query_mobjects"></a>
## def connectionNode_query_MObjects()

Parameters : node_MObject=MObject,
source=bool,
target=bool

Returns : single variable

Documents : 設定したアトリビュートの値を返す関数

# class SelfDagNode

<a id="convertmobject_create_mdagpath"></a>
## def convertMObject_create_MDagPath()

Parameters : MObject=maya.api.OpenMaya.MObject

Returns : maya.api.OpenMaya.MDagPath

Documents : MObjectをMDagPathに変換する関数

<a id="fullpath_query_str"></a>
## def fullpath_query_str()

Parameters : MDagPath=maya.api.OpenMaya.MDagPath

Returns : str(/dag node name)

Documents : MDagPathからフルパス名を取得する関数

<a id="_fullpathswitch_query_str"></a>
## def _fullPathSwitch_query_str()

Parameters : MObject=maya.api.OpenMaya.MObject,fullPath=bool(False)

Returns : str(node_name or /dag node name)

Documents : フルパスノードにするかしないかを切り替える関数