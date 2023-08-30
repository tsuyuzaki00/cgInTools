# baseLB
- [ ] 編集中
- [x] 編集済み

[一般向け(person)](../baseLB.md)

## クラス一覧
class : [SelfOrigin(object)](#class-selforigin-page)

## 関数一覧
None

## 変数一覧
None

---

# class SelfOrigin Page
>Inheritance :  
object

>import :  
None

>Summary :  
データを取得してアクションをするの指示が入っているクラス

## Single Function
None

## Multi Function
None

## Inheritance Function
None

## Private Function
None

## Setting Function
def [setReadDict()](#selforiginsetreaddict)  
def [getReadDict()](#selforigingetreaddict)  
def [setDataChoices()](#selforiginsetdatachoices)  
def [addDataChoices()](#selforiginadddatachoices)  
def [getDataChoices()](#selforigingetdatachoices)  
def [setDoIts()](#selforiginsetdoIts)  
def [addDoIts()](#selforiginadddoits)  
def [getDoIts()](#selforigingetdoits)  
## Public Function
def [writeDict()](#selforiginwritedict)  
def [readDict()](#selforiginreaddict)  
def [doIt()](#selforigindoit)  

---
# class SelfOrigin
## Single Function
None

## Multi Function
None

## Inheritance Function
None

## Private Function
None

## Setting Function

### SelfOrigin.setReadDict()
>Signature :  
setReadDict(variable)

>Parameters :  
variable - dict

>Returns :  
dict

>Description :  
setting関数たちに組み込むためのdictを読み込む関数

### SelfOrigin.getReadDict()
>Signature :  
getReadDict()

>Parameters :  
None

>Returns :  
dict

>Description :  
setting関数に設定するdictを返す関数

### SelfOrigin.setDataChoices()
>Signature :  
setDataChoices(variables)

>Parameters :  
variables - strings

>Returns :  
strings

>Description :  
writeDict()を実行した際に書き出せるように設定する関数  
writeDict()に書き出したいsetting関数のset,getを除いた文字列を入れる必要がある  
例: setNode(),getNode()があった場合setDataChoices(["Node"])となる  

### SelfOrigin.addDataChoices()
>Signature :  
addDataChoices(variables)

>Parameters :  
variables - strings

>Returns :  
strings

>Description :  
writeDict()を実行した際に書き出せるように設定を追加する関数  
writeDict()に書き出したいsetting関数のset,getを除いた文字列を入れる必要がある  
例: setNode(),getNode()があった場合addDataChoices(["Node"])となる  

### SelfOrigin.getDataChoices()
>Signature :  
getDataChoices()

>Parameters :  
None

>Returns :  
strings

>Description :  
設定した書き出す予定のシーケンス文字列を返す関数

### SelfOrigin.setDoIts()
>Signature :  
setDoIts(variables)

>Parameters :  
variables - strings

>Returns :  
strings

>Description :  
doIt()を実行した際に実行してほしいpublic関数名を設定する関数  
例: read(),create()があった場合setDoIts(["read","create"])となる

### SelfOrigin.addDoIts()
>Signature :  
addDoIts(variables)

>Parameters :  
variables - strings

>Returns :  
strings

>Description :  
doIt()を実行した際に実行してほしいpublic関数名を設定に追加する関数  
例: read(),create()があった場合addDoIts(["read","create"])となる

### SelfOrigin.getDoIts()
>Signature :  
getDoIts()

>Parameters :  
None

>Returns :  
strings

>Description :  
設定したpublic関数名のlistを返す関数

## Public Function
### SelfOrigin.writeDict()
>Signature :  
[setDataChoices()](#selforiginsetdatachoices)  
writeDict() or writeDict(dataChoices)

>Parameters :  
dataChoices - dict

>Returns :  
dict

>Description :  
dataChoicesで設定したsetting関数をdictで返す関数

### SelfOrigin.readDict()
>Signature :  
[setReadDict()](#selforiginsetreaddict)  
readDict() or readDict(settingData)

>Parameters :  
settingData - dict

>Returns :  
None

>Description :  
dictを使ってsetting関数たちに読み込ませる関数

### SelfOrigin.doIt()
>Signature :  
[setDoIts](#selforiginsetdoits)  
doIt() or doIt(doIts)

>Parameters :  
doIts - strings

>Returns :  
None

>Description :  
doItsで設定したpublic関数を順番に実行する関数

---

# Functions

---

# Variables