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
def [setAbsoluteDirectory()](#pathsetabsolutedirectory)  
def [getAbsoluteDirectory()](#pathgetabsolutedirectory)  
def [setRelativeDirectory()](#pathsetrelativedirectory)  
def [addRelativeDirectory()](#pathaddrelativedirectory)  
def [getRelativeDirectory()](#pathgetrelativedirectory)  
def [setFile()](#pathsetfile)  
def [getFile()](#pathgetfile)  
def [setExtension()](#pathsetextension)  
def [getExtension()](#pathgetextension)  
def [setTargetPath()](#pathsettargetpath)  
def [getTargetPath()](#pathgettargetpath)  
def [setSourcePath()](#pathgetsourcepath)  
def [getSourcePath()](#pathgetsourcepath)  

## Public Function
def [queryDirectory()](#pathquerydirectory)  
def [queryAbsolutePath()](#pathqueryabsolutepath)  
def [queryRelativePath()](#pathqueryrelativepath)  
def [querySequencePath()](#pathquerysequencepath)  
def [createFileExt()](#pathcreatefileext)  
def [deleteFileExt()](#pathdeletefileext)  
def [createDirectory()](#pathcreatedirectory)  
def [targetPathMove()](#pathtargetpathmove)  
def [targetPathCopy()](#pathtargetpathcopy)  
def [sourcePathMove()](#pathsourcepathmove)  
def [sourcePathCopy()](#pathsourcepathcopy)  

---
# class Path
## Special Function
### Path.\_\_init\_\_()
>Signature :  
instance=Path()  
\_absolute\_dir=None  
\_relative\_dir=None  
\_file\_str=None  
\_extension\_ext=None  
\_target\_Path=None
\_source\_Path=None

>Parameters :  
None

>Returns :  
None

>Description :  
\_absolute\_dir - 絶対ディレクトリを保持する変数  
\_relative\_dir - 相対ディレクトリを保持する変数  
\_file\_str - ファイル名を保持する変数  
\_extension\_ext - 拡張子名を保持する変数  
\_target\_Path - 支持するためのオブジェクト
\_source\_Path - 受け取るためのオブジェクト

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
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 >> instance2

>Parameters :  
None

>Returns :  
None

>Description :  
instance1からinstance2に移動する

### Path.\_\_irshift\_\_()
>Signature :  
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 >>= instance2

>Parameters :  
None

>Returns :  
None

>Description :  
instance1からinstance2にコピーする

### Path.\_\_lshift\_\_()
>Signature :  
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 << instance2

>Parameters :  
None

>Returns :  
None

>Description :  
instance2からinstance1に移動する

### Path.\_\_ilshift\_\_()
>Signature :  
instance1=Path()  
instance1.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance1.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance1.[setFile()](#pathsetfile)  
instance1.[setExtension()](#pathsetextension)  
instance2=Path()  
instance2.[setAbsoluteDirectory()](#pathsetabsolutedirectory)  
instance2.[setRelativeDirectory()](#pathsetrelativedirectory)  
instance2.[setFile()](#pathsetfile)  
instance2.[setExtension()](#pathsetextension)  
instance1 <<= instance2

>Parameters :  
None  

>Returns :  
None  

>Description :  
instance2からinstance1にコピーする  

## Single Function
### Path.mergeDirectory_create_dir()
>Signature :  
mergeDirectory_create_dir(upperDirectory_dir,lowerDirectory_dir)  

>Parameters :  
upperDirectory_dir - string(directory)  
lowerDirectory_dir - string(directory)  

>Returns :  
string(directory)  

>Description :  
絶対フォルダ階層と相対フォルダ階層を結合する関数  

### Path.mergePath_create_path()
>Signature :  
mergePath_create_path(directory_dir,file_str,extension_ext)

>Parameters :  
directory_dir - string(directory)  
file_str - string  
extension_ext - string(extension)  

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
variable - string(directory)  

>Returns :  
string(directory)  

>Description :  
絶対的フォルダ階層を設定する関数  

### Path.getAbsoluteDirectory()
>Signature :  
getAbsoluteDirectory()  

>Parameters :  
None  

>Returns :  
string(directory)  

>Description :  
設定した絶対的フォルダ階層を返す関数  

### Path.setRelativeDirectory()
>Signature :  
setRelativeDirectory(variable)  

>Parameters :  
variable - string(directory)  

>Returns :  
string(directory)  

>Description :  
相対的フォルダ階層を設定する関数  

### Path.addRelativeDirectory()
>Signature :  
addRelativeDirectory(variable)  

>Parameters :  
variable - string(directory)  

>Returns :  
string(directory)  

>Description :  
相対的フォルダ階層のさらに階層を追加する関数  

### Path.getRelativeDirectory()
>Signature :  
getRelativeDirectory()

>Parameters :  
None

>Returns :  
string(directory)

>Description :  
設定した相対的フォルダ階層を返す関数

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
[back](../../README.md) [Top](#pathlb)