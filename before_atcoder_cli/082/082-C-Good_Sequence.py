from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

num = defaultdict(int)

for a in A:
    num[a] += 1     # 連想配列に入力された文字を添字としてインクリメント

ans = 0

for key, value in num.items():      # numの添字と値をセットで取り出す
    if key == value:                # 添字と値が同じならそのまま
        continue
    elif key < value:               # 添字＜値なら値ー添字をプラス
        ans += value - key
    else:                           # 添字＞値なら値をプラス
        ans += value

print(ans)

# 計算量O(N) 
# N = max 10^5