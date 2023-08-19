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

例 class ClassName():

## 関数、クラス内シングル関数名

最初小文字 アンダースコア区切り3つ以上(name_mode_type_...) self変数、関数を入れるのは禁止

例 def name_create_func():

## クラス内推奨プライベート関数名

最初アンダースコア小文字 アンダースコア区切り3つ以上(_name_mode_type_...) self変数、関数を入れるのはOK

例 def _name_create_func():

## クラス内完全プライベート関数名 定数まとめ関数名

最初アンダースコア2つ小文字 アンダースコア区切り3つ以上(__name_mode_type_...) self変数、関数を入れるのはOK

例 def __name_create_func():

## クラス内の変数設置関数、実行する用のパブリック関数名

最初小文字 大文字区切り非推奨 アンダースコア区切無し self変数、関数を入れるのはOK

例 create()

例 setObject()

## 変数、関数内変数名,クラス継承名、クラス変数名

最初小文字 大文字区切り アンダースコア区切り2つ以内(name_type)

例 nodeName_obj

例 num=0 本当に小規模の場合は無しでもよい

## 初期設定変数、クラス内変数名

アンダースコア開始

例 self._name

## mode 動作

create 新しく作った際のモード

edit 元々ある物を加工した際のモード

query ある物の中身を取得する際のモード

check 問題ないか調べる際のモード

## type 戻り値

### 単体変数

func (function) 関数(returnを書いてない時に書く)

int 小数点のない数字

froat 小数点ありの数字

string 文字列

unicode UNIシステムの文字列

none 空で返す

bool (boolean) 真偽

obj 3DCGのオブジェクト名

shape 3DCGのシェイプ名

node ノード名

attr アトリビュート名

### 複合変数

list or 〇〇s

tuple

dict

### [ list or tuple or dict ]の場合

lists=[ [], [], ...]

tuples=[ (), (), ...]

dicts=[ {}, {}, ...]

objs=[ "obj", "obj", ...]
