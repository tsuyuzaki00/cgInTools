# objectLB

[一般向け(person)](/maya/library/_document/objectLB.md)

## クラス一覧

[SelfNode(object)](#selfnode)

[SelfDagNode(SelfNode)](#selfdagnode)

[SelfConnectNode(SelfDagNode)](#selfconnectnode)

[SelfMatrixNode(SelfDagNode)](#selfmatrixnode)

[SelfLocationNode(SelfMatrixNode)](#selflocationnode)

[SelfAnimNode(SelfMatrixNode)](#selfanimnode)

[SelfWeightJoint(SelfConnectNode)](#selfweightjoint)

[SelfPolygon(SelfMatrixNode)](#selfpolygon)

[SelfSurface(SelfMatrixNode)](#selfsurface)

[SelfCreateNode(object)](#selfcreatenode)

<a id="selfnode"></a>
# class SelfNode

Inheritance : object

Summary : 自立ノードの原点

## Single Function
def [selectOpenMaya_create_MObject()](#selectopenmaya_create_mobject)

def [nodeType_query_str()](#nodetype_query_str)

def [fullPath_query_str()](#fullpath_query_str)

def [convertMObject_create_MDagPath](#convertmobject_create_mdagpath)

def [nodeAttr_create_MPlug()](#nodeattr_create_mplug)

def [editAttr_edit_func()](#editattr_edit_func)

def [queryAttr_query_value()](#queryattr_query_value)

## Multi Function

def [_fullPathSwitch_query_str()](#_fullpathswitch_query_str)

## Private Function

None

## Summary Function

None

## Setting Function
def [\_\_init\_\_()](#__init__)

def [setNode()](#setnode)

def [getNode()](#getnode)

def [getNodeType()](#getnodetype)

def [setAttr()](#setattr)

def [getAttr()](#getattr)

def [setValue()](#setvalue)

def [getValue()](#getvalue)

## Public Function

def [editAttr()](#editattr)

def [queryAttr()](#queryattr)

===================

<a id="selectopenmaya_create_mobject"></a>
### def selectOpenMaya_create_MObject()

Parameters : str(node name)

Returns : maya.api.OpenMaya.MObject

Documents : 存在するノード名をMObjectに変換する関数

<a id="nodetype_query_str"></a>
### def nodeType_query_str()

Parameters : MObject=maya.api.OpenMaya.MObject

Returns : str(node type)

Documents : MObjectからノードタイプを取得する関数

<a id="fullpath_query_str"></a>
### def fullpath_query_str()

Parameters : MDagPath=maya.api.OpenMaya.MDagPath

Returns : str(/dag node name)

Documents : MObjectからフルパス名を取得する関数

<a id="convertmobject_create_mdagpath"></a>
### def convertMObject_create_MDagPath()

Parameters : MObject=maya.api.OpenMaya.MObject

Returns : maya.api.OpenMaya.MDagPath

Documents : MObjectをMDagPathに変換する関数

<a id="nodeattr_create_mplug"></a>
### def nodeAttr_create_MPlug()

Parameters : MObject=maya.api.OpenMaya.MObject,attr=str(attribute name)

Returns : maya.api.OpenMaya.MPlug

Documents : MObjectをMPlugに変換する関数

<a id="editattr_edit_func"></a>
### def editAttr_edit_func()

Parameters : MPlug=maya.api.OpenMaya.MPlug,value=single variable

Returns : None

Documents : MPlugに対して設定したvalueに変更する関数

<a id="queryattr_query_value"></a>
### def queryAttr_query_value()

Parameters : MPlug=maya.api.OpenMaya.MPlug,type=single variable name("double")

Returns : single variable

Documents : MPlugに設定されている値を取得する関数

<a id="_fullpathswitch_query_str"></a>
### def _fullPathSwitch_query_str()

Parameters : MObject=maya.api.OpenMaya.MObject,fullPath=bool(False)

Returns : str(node_name or /dag node name)

Documents : フルパスノードにするかしないかを切り替える関数

<a id="__init__"></a>
### def \_\_init\_\_()

Parameters : str(node name)

Returns : None

Documents : 自身が何のノードなのかを入れる必要がある

<a id="setnode"></a>
### def setNode()

Parameters : str(node name)

Returns : MObject

Documents : 自身のノードを変更する関数

<a id="getnode"></a>
### def getNode()

Parameters : fullPath=bool

Returns : str(node name)

Documents : 自身のノード名を返す関数

<a id="getnodetype"></a>
### def getNodeType()

Parameters : None

Returns : str(node type)

Documents : 自身のノードタイプを返す関数

<a id="setattr"></a>
### def setAttr()

Parameters : str(attribute name)

Returns : str(attribute name)

Documents : 自身が何のアトリビュートを所持しているかを決める関数

<a id="getattr"></a>
### def getAttr()

Parameters : None

Returns : str(attribute name)

Documents : 自身が何のアトリビュートを所持しているかを返す関数

<a id="setvalue"></a>
### def setValue()

Parameters : single variable

Returns : single variable

Documents : 自身が何の値を所持しているかを決める関数

<a id="getvalue"></a>
### def getValue()

Parameters : None

Returns : single variable

Documents : 自身が何の値を所持しているかを返す関数

<a id="editattr"></a>
### def editAttr()

Parameters : attr_str=str(attribute name),value=single variable

Returns : None

Documents : 設定した値を使用して設定したアトリビュートを変更する関数

<a id="queryattr"></a>
### def queryAttr()

Parameters : attr_str=str(attribute name),valueType_str=str(single variable name)

Returns : single variable

Documents : 設定したアトリビュートの値を返す関数

<a id="selfdagnode"></a>
# class SelfDagNode

Inheritance : SelfNode

Summary : DAG(Directed Acyclic Graph) 階層に関するクラス

<a id="selfconnectnode"></a>
# class SelfConnectNode

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を接続に関するクラス

<a id="selfmatrixnode"></a>
# class SelfMatrixNode

Inheritance : SelfDagNode

Summary : マトリクスに関するクラス

<a id="selflocationnode"></a>
# class SelfLocationNode

Inheritance : SelfMatrixNode

Summary : 移動、回転、スケールに関するクラス

<a id="selfanimnode"></a>
# class SelfAnimNode

Inheritance : SelfNode

Summary : アニメーションキーに関するクラス

<a id="selfweightjoint"></a>
# class SelfWeightJoint

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を繋げる用のノード

<a id="selfpolygon"></a>
# class SelfPolygon

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を繋げる用のノード

<a id="selfsurface"></a>
# class SelfSurface

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を繋げる用のノード

<a id="selfcreatenode"></a>
# class SelfCreateNode

Inheritance : SelfNode

Summary : DG(Dependency Graph) アトリビュート同士を繋げる用のノード