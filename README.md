# scriptsInTools

## 各フォルダーの定義
### _Menu
上部メニューに表示させるフォルダー

### readme
readmeの参照するフォルダー

### documents
全体で使用するマニュアルをまとめるフォルダー

### image
README.mdで使用する画像を保存するフォルダー

### ui
どのDCCツールでも使えるUIファイルを格納するフォルダー
### init.py
外部フォルダーのパスを取得する際に使用可能

## アプリ内フォルダーの定義
### setup
初期設定で各データを配置するためのフォルダー

mayaの場合

・iconsはscriptsと同じ階層

・modulesはC:\Users\"user_name"\Documents\maya
    
modに読み込んでほしいパスを書く
    
例 + CustomTools 1 D:/Maya (オンオフ なんでもいい名前 番号 パス名)

・userSetupはscripts内の階層


### _settings
UIの初期設定をjsonファイルにして保存するフォルダー
### data
書き出し読み込みを行うjsonファイルを保存するフォルダー

### execute
Libraryを読み込んだりして、コマンド実行する物を格納するフォルダー

### library
使いまわしやすいスクリプトを格納するフォルダー

### manager
execute,libray,uiのファイルをインポートして組み合わせたものを格納するフォルダー

### documents
アプリ内フォルダーのみで使用するマニュアルをまとめるフォルダー

### images
アプリ内フォルダーのみで使用する画像を保存するフォルダー