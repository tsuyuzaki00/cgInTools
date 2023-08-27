# jsonLB
- [x] 編集中
- [ ] 編集済み

[一般向け(person)](../jsonLB.md)

## クラス一覧
class [Json()](#json)  
class [JsonPack()](#jsonpack)  

## 関数一覧
def [readJson()](#readjson)  
def [writeJson()](#writejson)  

## 変数一覧
None

---
<a id="json"></a>
# class Json Page
Inheritance :  
object

import :  
json,os

Summary :  
Jsonファイルを読み込み書き出しするクラス

## Single Function
def [path_create_str()](#jsonpathcreatestr)  
def [jsonPath_query_dict()](#jsonjsonpathquerydict)  
def [jsonPath_create_func()](#jsonjsonpathcreatefunc)  
## Multi Function
None
## Inheritance Function
None
## Private Function
None
## Setting Function
def [setDirectory()](#jsonsetdirectory)  
def [getDirectory()](#jsongetdirectory)  
def [setFile()](#jsonsetfile)  
def [getFile()](#jsongetfile)  
def [setExtension()](#jsonsetextension)  
def [getExtension()](#jsongetextension)  
def [setWriteDict()](#jsonsetwritedict)  
def [getWriteDict()](#jsongetwritedict)  
## Public Function
def [read()](#jsonread)  
def [write()](#jsonwrite)  

---

<a id="jsonpack"></a>
# class JsonPack Page

Inheritance :  
object

import :  
json,os

Summary :  
複数のJsonファイルを読み込み書き出しするクラス

## Single Function
None
## Multi Function
None
## Inheritance Function
None
## Private Function
def [\_\_readPack_query_dicts()](#jsonpackreadpackquerydicts)  
def [\_\_writePack_create_func()](#jsonpackwritepackcreatefunc)  
## Setting Function
def [setDirectory()](#jsonpacksetdirectory)  
def [getDirectory()](#jsonpackgetdirectory)  
def [setFile()](#jsonpacksetfile)  
def [getFile()](#jsonpackgetfile)  
def [setExtension()](#jsonpacksetextension)  
def [getExtension()](#jsonpackgetextension)  
def [setJsonObjects()](#jsonpacksetjsonobjects)  
def [addJsonObjects()](#jsonpackaddjsonobjects)  
def [getJsonObjects()](#jsonpackgetjsonobjects)  
## Public Function
def [readPack()](#jsonpackreadpack)  
def [writePack()](#jsonpackwritepack)  

---
# class Json
## Single Function
<a id="jsonpathcreatestr"></a>
### Json.path_create_str()
Signature :  
path_create_str(directory,file,extension="json",newFolder=None)

Parameters :  
directory - string(directory)  
file - string  
extension - string(extension)  
newFolder - string  

Returns :  
string(path)  

Description :  
フォルダ階層の文字列、ファイル名の文字列、拡張子の文字列、必要ならフォルダーの文字列を入れてパスの文字列を作成する関数

<a id="jsonjsonpathquerydict"></a>
### Json.jsonPath_query_dict()
Signature :  
jsonPath_query_dict(path)

Parameters :  
path - string(path)

Returns :  
dict

Description :  
指定したパスからjsonファイルを読み込む関数

<a id="jsonjsonpathcreatefunc"></a>
### Json.jsonPath_create_func()
Signature :  
jsonPath_create_func(path,write_dict)

Parameters :  
path - string(path)  
write_dict - dict  

Returns :  
None

Description :  
指定したパスにjsonファイルを書き出す関数
## Multi Function
None
## Inheritance Function
None
## Private Function
None
## Setting Function
<a id="jsonsetdirectory"></a>
### Json.setDirectory()
Signature :  
setDirectory(variable)

Parameters :  
variable - string

Returns :  
string(directory)

Description :  
フォルダ階層の文字列を設定する関数

<a id="jsongetdirectory"></a>
### Json.getDirectory()
Signature :  
getDirectory()

Parameters :  
None

Returns :  
string(directory)

Description :  
設定したフォルダ階層の文字列を返す関数

<a id="jsonsetfile"></a>
### Json.setFile()
Signature :  
setFile(variable)

Parameters :  
variable - string

Returns :  
string

Description :  
ファイル名の文字列を設定する関数

<a id="jsongetfile"></a>
### Json.getFile()
Signature :  
getFile()

Parameters :  
None

Returns :  
string

Description :  
設定したファイル名の文字列を返す関数

<a id="jsonsetextension"></a>
### Json.setExtension()
Signature :  
setExtension(variable)

Parameters :  
variable - string(extension)

Returns :  
string

Description :  
拡張子の文字列を設定する関数

<a id="jsongetextension"></a>
### Json.getExtension()
Signature :  
getExtension()

Parameters :  
None

Returns :  
string(extension)

Description :  
設定した拡張子の文字列を返す関数

<a id="jsonsetwritedict"></a>
### Json.setWriteDict()
Signature :  
setWriteDict(variable)

Parameters :  
variable - dict

Returns :  
dict

Description :  
Jsonファイルに書き出す辞書を設定する関数

<a id="jsongetwritedict"></a>
### Json.getWriteDict()
Signature :  
 getWriteDict()

Parameters :  
None

Returns :  
dict

Description :  
設定したJsonファイルに書き出す辞書を返す関数

## Public Function
<a id="jsonread"></a>
### Json.read()

Signature :  
[setDirectory(variable)](#jsonsetdirectory)  
[setFile(variable)](#jsonsetfile)  
[setExtension(variable)](#jsonsetextension)  
read() or read(path)

Parameters :  
path - string(path)

Returns :  
dict

Description :  
Jsonファイルを読み込む関数

<a id="jsonwrite"></a>
### Json.write()

Signature :  
[setDirectory(variable)](#jsonsetdirectory)    
[setFile(variable)](#jsonsetfile)  
[setExtension(variable)](#jsonsetextension)  
[setWriteDict(variable)](#jsonsetwritedict)  
write() or write(path,write)

Parameters :  
path - string(path)  
write - dict  

Returns :  
None

Description :  
Jsonファイルを書き出す関数

--- 

# class JsonPack
## Single Function
None
##  Multi Function
None
## Inheritance Function
None
## Private Function
<a id="jsonpackreadpackquerydicts"></a>
### JsonPack.\_\_readPack_query_dicts()

Signature :  
\_\_readPack_query_dict(directory,file,extension)

Parameters :  
directory - string(directory)  
file - string  
extension - string(extension)  

Returns :  
dicts

Description :  
JsonPackファイルを読み込む関数

<a id="jsonpackwritepackcreatefunc"></a>
### JsonPack.\_\_writePack_create_func()

Signature :  
\_\_writePack_create_func(directory,file,extension,write_Jsons)

Parameters :  
directory - string(directory)  
file - string  
extension - string(extension)  
write_Jsons - [Json](#class-json-page)  

Returns :
 None

Description :
 JsonPackファイルを書き出す関数
 
## Setting Function

<a id="jsonpacksetdirectory"></a>
### JsonPack.setDirectory()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpackgetdirectory"></a>
### JsonPack.getDirectory()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpacksetfile"></a>
### JsonPack.setFile()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpackgetfile"></a>
### JsonPack.getFile()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpacksetextension"></a>
### JsonPack.setExtension()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpackgetextension"></a>
### JsonPack.getExtension()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpacksetjsonobjects"></a>
### JsonPack.setJsonObjects()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpackaddjsonobject"></a>
### JsonPack.addJsonObjects()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpackgetjsonobject"></a>
### JsonPack.getJsonObjects()

Signature : 

Parameters : 

Returns : None

Description : 

## Public Function

<a id="jsonpackreadpacks"></a>
### JsonPack.readPack()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="jsonpackwritepack"></a>
### JsonPack.writePack()

Signature : 

Parameters : 

Returns : None

Description : 

---
# Functions

<a id="readjson"></a>
### def readJson()

Signature : 

Parameters : 

Returns : None

Description : 

<a id="writejson"></a>
### def writeJson()

Signature : 

Parameters : 

Returns : None

Description : 

---

# Variables