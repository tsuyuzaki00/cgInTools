## フォルダー名
全小文字 区切りなし アンダースコア区切りなし

例 os,sys

## ファイル名
最初小文字 大文字区切り アンダースコア区切りなし


## 定数名
全大文字 アンダースコア区切りあり

例 FAVORITE_CONST

## クラス名 
最初大文字 大文字区切り アンダースコア区切りなし

例 ClassName

## クラス継承名、クラス変数名
最初アンダースコア大文字 大文字区切り アンダースコア区切りなし

例 _ClassName

## 関数、クラス内関数名
最初小文字 アンダースコア区切り3つ以上(name_mode_type_...)

例 

## 変数、関数内変数名
最初小文字 大文字区切り アンダースコア区切り2つ以内(name_type)

例 

## 辞書名
最初小文字 大文字区切り アンダースコア区切りなし

例 

## ファイル内完結の関数内変数名
最初アンダースコア

## 変更しない変数、関数名
アンダースコア開始

## mode一覧
create

edit

query

check

## type一覧
### 単体変数
int 小数点のない数字

froat 小数点ありの数字

string 文字列

unicode UNIシステムの文字列

none 空で返す

bool (boolean) 真偽

func (function) 関数(returnを書いてない時に書く)

obj 3DCGのオブジェクト名

joint 3DCGのジョイント名

### 複合変数
### 数が決まっている場合
list5

tuple3

dict3

obj2

### 数が決まってない場合
lists

tuples

dicts

objs