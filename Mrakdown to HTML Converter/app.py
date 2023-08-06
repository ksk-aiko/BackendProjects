import sys
import markdown

# ファイルの読み込み処理を関数にまとめる
def read_file(path):
    # ファイルを開いて内容を読み込む
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except Exception as e:
        print(f"Error reading file {path}: {str(e)}")
        sys.exit(1)

# ファイルの書き込み処理を関数にまとめる
def write_file(path, data):
    # ファイルを開いて内容を書き込む
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"Error writing file {path}: {str(e)}")
        sys.exit(1)

def convert_md_to_html(input_path, output_path):
    # Markdownファイルを開いて内容を読み込む
    md_content = read_file(input_path) 
    # Markdown内容をHTMLに変換する
    html_content = markdown.markdown(md_content)
    # HTML内容を指定されたパスに保存する
    write_file(output_path, html_content)

EXPECTED_ARGS = 4
APPROPRIATE_COMMAND = "markdown"
# コマンドライン引数を確認する
if len(sys.argv) != EXPECTED_ARGS:
    print("Usage: python3 file-converter.py markdown inputfile outputfile")
    sys.exit(1)

cmd, input_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]

# 'markdown' コマンドが指定された場合、MarkdownをHTMLに変換する
if cmd == APPROPRIATE_COMMAND:
    convert_md_to_html(input_file, output_file)
else:
    print(f"Invalid command: {cmd}")
    sys.exit(1)


