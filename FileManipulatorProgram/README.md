# FileManipulatorProgram

## 概要
* CLIから実行されるプログラム。入力の引数に基づいて特定の操作を実行します。
* open()関数を活用し、ファイルオブジェクトを操作します。

## 要件
### reverseコマンド
* 引数inputpathで操作するファイルのパスを受け取り、引数outputpathにinputpathの内容を逆にした新しいファイルを作成します。
### copyコマンド
* 引数inputpathにあるファイルのコピーを作成し、引数outputpathとして保存します。  
### duplicate-contentsコマンド
* 第一引数inputpathにあるファイルの内容を読み込み、その内容を複製し、複製された内容をinputpathにあるファイルに第二引数n回分複製します。
### replace-string
* 第一引数inputpathにあるファイルの内容から第二引数needle(文字列)を検索し、needleの全てを第三引数newstringに置換します。
