# pathLB
- [x] 編集中
- [ ] 編集済み

[一般向け(person)](../pathLB.md)

## クラス一覧
class [Path(object)](#class-path-page)   

## 関数一覧
None

## 変数一覧
None

---

# class Path Page
>Inheritance :  
object

>import :    
os,shutil

>Summary :  
directory,folder,file,path  
フォルダ階層、フォルダー、ファイル、フォルダ階層とファイルを合わせたものをパス  
を所持ているオブジェクト  

## Special Function
def [\_\_init\_\_()](#path__init__)  
def [\_\_str\_\_()](#path__str__)  
def [\_\_rshift\_\_()](#path__rshift)  
def [\_\_irshift\_\_()](#path__irshift)  
def [\_\_lshift\_\_()](#path__lshift)  
def [\_\_ilshift\_\_()](#path__ilshift)  

## Single Function
def [mergeDirectory_create_dir()](#pathmergedirectory_create_dir)  
def [mergePath_create_path()](#pathmergepath_create_path)

## Multi Function
None

## Inheritance Function
None

## Private Function
None

## Setting Function
def [setAbsoluteDirectory()](#pathsetsetting)  
def [getAbsoluteDirectory()](#pathaddsetting)  
def [setRelativeDirectory()](#pathcurrentsetting)  
def [addRelativeDirectory()](#pathgetsetting)  
def [getRelativeDirectory()](#pathgetsetting)  
def [setFile()](#pathgetsetting)  
def [getFile()](#pathgetsetting)  
def [setExtension()](#pathgetsetting)  
def [getExtension()](#pathgetsetting)  

## Public Function
def [absolutePath()](#pathpublic)  
def [relativePath()](#pathpublic)  
def [sequencePath()](#pathpublic)  
def [createFileExt()](#pathpublic)  
def [deleteFileExt()](#pathpublic)  
def [createDirectory()](#pathpublic)  
def [queryDirectory()](#pathpublic)  

---
# class Path
## Special Function
### Path.\_\_init\_\_()
>Signature :  
instance=Path()  
\_absolute_dir=None  
\_relative_dir=None  
\_file_str=None  
\_extension_ext=None  

>Parameters :  
None

>Returns :  
None

>Description :  
\_absolute_dir - 絶対ディレクトリをもつ変数  
\_relative_dir - 相対ディレクトリをもつ変数  
\_file_str - ファイル名をもつ変数  
\_extension_ext - 拡張子名をもつ変数  

### Path.\_\_str\_\_()
>Signature :  
instance=Path()  
instance.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance.[setFile()](#pathsetfile)  
instance.[setExtension()](#pathsetextension)  
print(instance) or str(instance)  

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイルパスを返す

### Path.\_\_rshift\_\_()
>Signature :  
instance=Path()  
instance.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance.[setFile()](#pathsetfile)  
instance.[setExtension()](#pathsetextension)  
print(instance) or str(instance)  

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイルパスを返す

### Path.\_\_irshift\_\_()
>Signature :  
instance=Path()  
instance.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance.[setFile()](#pathsetfile)  
instance.[setExtension()](#pathsetextension)  
print(instance) or str(instance)  

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイルパスを返す

### Path.\_\_lshift\_\_()
>Signature :  
instance=Path()  
instance.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance.[setFile()](#pathsetfile)  
instance.[setExtension()](#pathsetextension)  
print(instance) or str(instance)  

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイルパスを返す

### Path.\_\_ilshift\_\_()
>Signature :  
instance=Path()  
instance.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance.[setFile()](#pathsetfile)  
instance.[setExtension()](#pathsetextension)  
print(instance) or str(instance)  

>Parameters :  
None

>Returns :  
string

>Description :  
設定したファイルパスを返す

## Single Function
### Path.mergeDirectory_create_dir()
>Signature :  
mergeDirectory_create_dir(upperDirectory_dir,lowerDirectory_dir)

>Parameters :  


>Returns :  
string(directory)

>Description :  
絶対フォルダ階層と相対フォルダ階層を結合する関数

### Path.mergePath_create_path()
>Signature :  
mergePath_create_path(directory_dir,file_str,extension_ext)

>Parameters :  


>Returns :  
string(path)

>Description :  
フォルダ階層、ファイル名、拡張子名を結合する関数

## Multi Function
None

## Inheritance Function
None

## Private Function
None

## Setting Function
### Path.setAbsoluteDirectory()
>Signature :  
setAbsoluteDirectory(variable)

>Parameters :  
variable - value  

>Returns :  
value

>Description :  
クラス内変数に設定する関数

### Path.getAbsoluteDirectory()
>Signature :  
getAbsoluteDirectory()

>Parameters :  
None

>Returns :  
value

>Description :  
クラス内変数に設定する関数

### Path.setRelativeDirectory()
>Signature :  
setRelativeDirectory(variable)

>Parameters :  
variable - value  

>Returns :  
value

>Description :  
クラス内変数に設定する関数

### Path.addRelativeDirectory()
>Signature :  
addRelativeDirectory(variable)

>Parameters :  
variable - string  

>Returns :  
list

>Description :  
クラス内変数に追加する関数  
シーケンスを渡す事が多い

### Path.getRelativeDirectory()
>Signature :  
getRelativeDirectory()

>Parameters :  
None

>Returns :  
value

>Description :  
クラス内変数に設定する関数

### Path.setFile()
>Signature :  
setFile(variable)

>Parameters :  
variable - string

>Returns :  
value

>Description :  
クラス内変数に設定している変数を返す関数  
パラメータには何も入れない

### Path.getFile()
>Signature :  
getFile()

>Parameters :  
None

>Returns :  
value

>Description :  
クラス内変数に設定している変数を返す関数  
パラメータには何も入れない

### Path.setExtension()
>Signature :  
setExtension(variable)

>Parameters :  
variable - string

>Returns :  
value

>Description :  
クラス内変数に設定している変数を返す関数  
パラメータには何も入れない

### Path.getExtension()
>Signature :  
getExtension()

>Parameters :  
None

>Returns :  
value

>Description :  
クラス内変数に設定している変数を返す関数  
パラメータには何も入れない

## Public Function
### Path.absolutePath()
>Signature :  
[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
absolutePath() or absolutePath(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

### Path.relativePath()
>Signature :  
[setRelativeDirectory()](#pathsetrelativedirectory)  
relativePath() or relativePath(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

### Path.relativePath()
>Signature :  
[setRelativeDirectory()](#pathsetrelativedirectory)  
relativePath() or relativePath(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

### Path.createFileExt()
>Signature :  
[setRelativeDirectory()](#pathsetrelativedirectory)  
createFileExt() or createFileExt(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

### Path.deleteFileExt()
>Signature :  
[setRelativeDirectory()](#pathsetrelativedirectory)  
deleteFileExt() or deleteFileExt(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

### Path.createDirectory()
>Signature :  
[setRelativeDirectory()](#pathsetrelativedirectory)  
createDirectory() or createDirectory(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

### Path.queryDirectory()
>Signature :  
[setRelativeDirectory()](#pathsetrelativedirectory)  
queryDirectory() or queryDirectory(variable)

>Parameters :  
variable - value  

>Returns :  
None

>Description :  
設定した変数を使用してアクションする際に使用する関数  
set関数に設定していれば何も変数を入れずに実行し  
無ければ変数を入れる必要がある

---
# Functions
None

---
# Variables
None

---
[back](../README.md) [Top](#pathlb)