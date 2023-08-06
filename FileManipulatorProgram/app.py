import sys

def read_file(inputpath):
    try:
        with open(inputpath, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {inputpath}: {str(e)}")
        sys.exit(1)

def write_file(outputpath, data):
    try:
        with open(outputpath, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"Error writing file {outputpath}: {str(e)}")
        sys.exit(1)

def reverse(inputpath, outputpath):
    # 入力ファイルを開き、すべての内容を読み込む
    data = read_file(inputpath)

    # 読み込んだ内容を逆順にする
    reversed_data = data[::-1]

    # 逆順にした内容を出力ファイルに書き込む
    write_file(outputpath, reversed_data)
    
def copy(inputpath, outputpath):
    # 入力ファイルを出力ファイルへコピーする
    # ファイルの内容を読み込む
    data = read_file(inputpath)

    # 読み込んだ内容でファイルを作成する
    write_file(outputpath, data)

def duplicate_contents(inputpath, n):
    # 入力ファイルを開き、すべての内容を読み込む
    data = read_file(inputpath)

    # 読み込んだ内容をn回繰り返す
    duplicated_data = data * int(n)

    # 繰り返した内容を同じファイルに書き込む
    write_file(inputpath, duplicated_data)

def replace_string(inputpath, needle, newstring):
    # 入力ファイルを開き、すべての内容を読み込む
    data = read_file(inputpath)

    # 読み込んだ内容から指定の文字列を新しい文字列に置換する
    replaced_data = data.replace(needle, newstring)

    # 置換した内容を同じファイルに書き込む
    write_file(inputpath, replaced_data)

# コマンドラインからの入力の解析
argv_len = len(sys.argv)
if (argv_len < 2):
    print("Not enough arguments for this program.")
    sys.exit(1)

program_name = sys.argv[0]
command = sys.argv[1]

# commandの種類によって、コマンドラインからの入力と変数をの割り当てを変える
# 引数の数をチェック
if command == "reverse":
    if (argv_len < 4):
        print("Not enough arguments for 'reverse' command.")
        sys.exit(1)
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]
    reverse(inputpath, outputpath)
elif command == "copy":
    if (argv_len < 4):
        print("Not enough arguments for 'copy' command.")
        sys.exit(1)
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]
    copy(inputpath, outputpath)
elif command == "duplicate-contents":
    if (argv_len < 4):
        print("Not enough arguments for 'duplicate-contents' command.")
        sys.exit(1)
    inputpath = sys.argv[2]
    n = sys.argv[3]
    duplicate_contents(inputpath, n)
elif command == "replace-string":
    if (argv_len < 5):
        print("Not enough arguments for 'replace-string' command.")
        sys.exit(1)
    inputpath = sys.argv[2]
    needle = sys.argv[3]
    newstring = sys.argv[4]
    replace_string(inputpath, needle, newstring)
else:
    print(f"Invalid command: {command}")

