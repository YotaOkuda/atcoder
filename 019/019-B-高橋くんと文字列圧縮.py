S = str(input())

i = 0
ans = []

while i < len(S):
    j = i

    # 文字列が一致する範囲を探索
    while j < len(S) and S[i] == S[j]:
        j += 1  

    ans.append(S[i] + str(j - i))   # 文字と一致する範囲を結合
    i = j   # 始点の更新

print(''.join(ans))

# 計算量O(N) < 10^8