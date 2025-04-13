'''
<方針>
- login しているかの状態を保持しておく変数を用意する
- pribate の時にログインしていなかったら、認証エラーをカウントする
'''

N = int(input())

ans = 0
# ログイン状態を管理する変数
is_login = False

for i in range(N):
    S = str(input())
    # ログイン状態の遷移
    if S == "login":
        is_login = True
    elif S == "logout":
        is_login = False

    # 認証エラーをカウント
    if S == "private" and is_login == False:
        ans += 1

print(ans)

# 計算量 O(N)