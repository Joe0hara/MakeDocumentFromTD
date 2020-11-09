# MakeDocumentFromTD

![icon](images/makeDocumentFromTD_icon.jpg)

- TouchDesigner のプロジェクトからドキュメント（MarkDown、HTML）を生成するコンポーネント
- コメントの付いたオペレータ、または `readme` と名のついたDATからHeader及び文章、`screenshot`が名前に含まれるTOPをスクリーンショットを取得し、ドキュメントを自動で作成します。
- Components to generate documentation (MarkDown and HTML) from a TouchDesigner project
- The operator named `readme` or the DAT named `readme` takes a screenshot of the top of the screen including the `screenshot` in the header and the text, and creates a document automatically.

---

**[ [English](#Usage) / [日本語](#使い方) ]**

## Usage

### Installation

- put makeDocumentFromTD.tox anywhere in the project
- Set file names and other parameters
- Press the `Create` button from the parameters to output the file

### Rule

#### Text

- Create a DAT named`readme`.

![DAT Comment sample](images/DAT_comments.png)

or

- Comment on the operator

![comment sample](images/comments.png)

- Header names are automatically generated from project hierarchy and operator names
- URLs are automatically linked

#### Screenshot

- Automatically create a screenshot of the image from the TOP of the name containing `screenshot`

![screenshot sample](images/ScreenShot.png)

#### Output

- Set the name and destination of the file to be saved.

- Press the `Create` button from the parameters.

---

## Parameters

- Component
  - Target COMP

- file name
  - File name of the output document

- File Format
  - Markdown
  - HTML
  - Json

- Output file
  - File name with extension （automatic entry）

- Output Folder
  - Path of the output folder

- Image Format
  - Output image extension

- Create
  - Create Buttun

---

## 使い方

### 導入方法

- makeDocumentFromTD.tox をプロジェクトの任意の場所に置く
- ファイル名などをパラメータから設定
- パラメータから `Create` ボタンを押してファイル出力

---

### ルール

#### テキスト

- `readme` という名前のDATを作成

![DAT Comment sample](images/DAT_comments.png)

または

- オペレータにコメントを付ける

![comment sample](images/comments.png)

- ヘッダー名はプロジェクトの階層とオペレータ名から自動生成
- URLは自動的にリンク付け

#### スクリーンショット

- `screenshot` という文字列の入った名前のTOPから画像のスクリーンショットを作成

![screenshot sample](images/ScreenShot.png)

### 出力方法

- 保存するファイル名、保存先を設定
- Createボタンでドキュメント生成

---

## パラメーター

- Component
  - プロジェクトのオペレータのパス

- file name
  - 出力するドキュメントのファイル名

- File Format
  - Markdown
  - HTML
  - Json

- Output file
  - 出力される拡張子付きファイル名（自動入力）

- Output Folder
  - 出力するフォルダのパス

- Image Format
  - 出力する画像の拡張子

- Create
  - ボタンを押すとドキュメント作成する
