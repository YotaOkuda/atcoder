'''
<方針>
- 0 の連続と、1 の連続を区間分割する
- 1 の塊とその始点、終点（厳密には 1 が終わり、0 が始まるインデックス）、をリストに記録していく
- リストの K（index : K - 1) 番目と K - 1（index : K - 2）の
  「始点、終点、1 の塊」を参照し、文字列を組み替える
'''

N, K = map(int, input().split())
S = str(input())

# 1 の塊を記録するリスト
oneBlock = []

# 文字列を先頭から見て区間分割する
i = 0
while i < len(S):
    j = i
    
    # 1 の塊なら、リストに「始点、終点、1 の塊」を記録
    if S[j] == '1':
        while j < len(S) and S[j] == '1':
            j += 1
        oneBlock.append([i, j, '1' * (j - i)])
    else:
        while j < len(S) and S[j] != '1':
            j += 1
    
    i = j
    
# K 番目の「始点、終点、1 の塊」を参照
kStart, kEnd, kOne = oneBlock[K - 1]
# K 番目の 1 の塊を消した文字列を作成
S = S[:kStart] + S[kEnd:]

# K - 1 番目の「始点、終点、1 の塊」を参照
k1Start, k1End, k1One = oneBlock[K - 2]
# K 番目の 1 の塊を、K - 1 番目の 1 の塊の後ろにつける
S = S[:k1End] + kOne + S[k1End:]

print(S)

# 計算量 O(N)


# >>> 別解 >>>
# 0 と 1 それぞれ連長圧縮を行い、K 番目の「1 の塊」と、その左の「0 の塊」をスワップする