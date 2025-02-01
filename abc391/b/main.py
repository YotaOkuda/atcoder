'''
<方針>
- S の左上端を決めて、M 分の文字列が T と一致するか確認する
  S[i][j] を始点として、T[i]と一致するか
  S[i + 1][j], S[i + 2][j] と T[i + 1], T[i + 2] まで見る
'''

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]

for i in range(N - M + 1):  # i は行を表す
    for j in range(N - M + 1):  # j は列を表す
        # 全て一致するかを判定する変数（M 行一致するか）
        count = 0
        # T[0], T[1], ..., T[M] がそれぞれ S[i][j:j + M], S[i + 1][j:j + M], ..., S[i + M][j:j + M] と一致するか
        for z in range(M):
            if S[i + z][j:j + M] == T[z]:
                count += 1
        # 全て一致している場合、始点を出力する
        if count == M:
            print(i + 1, j + 1)
            break

# 計算量 O((N - M + 1)^2 * M^2)