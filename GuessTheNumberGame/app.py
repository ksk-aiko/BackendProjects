import random

# ユーザーが最小数nを入力
n = int(input("最小数を入力してください: "))

# ユーザーが最大数mを入力し、n <= mであることを確認
while True:
    m = int(input("最大数を入力してください: "))
    if n <= m:
        break
    else:
        print("最小数が最大数を超えています。もう一度入力してください")

# nからmの範囲で乱数生成
random_number = random.randint(n, m)

# 推測できる回数を設定
max_tries = int(input("トライできる回数を設定してください: "))

# 乱数を推測し、入力
tries = 0
while tries < max_tries:
    guess = int(input(f"{tries + 1}回目のチャレンジです: "))
    
    # 正解か
    if guess == random_number:
        print("おめでとうございます！見事正解です！")
        break
    else:
        # 回数内か
        tries += 1
        if tries >= max_tries:
            print("残念！上限回数に到達しました。次回またチャレンジしてください！")
            break
        print("ハズレ！もう一度チャレンジ！")


