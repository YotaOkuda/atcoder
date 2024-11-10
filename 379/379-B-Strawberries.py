'''
<方針>
- 'O' が何個続いているかカウントする
- 'X' が出たらカウントを 0 にリセット
- カウントが K 以上になったら、イチゴを食べる回数を ans にカウントし、
  次回もカウントされないよう、使った歯を虫歯にする（count -= K）
'''

N, K = map(int, input().split())
S = input()

# 'O' が連続で出現する回数をカウント
count = 0
# イチゴが何回食べられるか
ans = 0

i = 0
while i < len(S):
    # 'O' ならカウントし、'X' ならリセット
    if S[i] == 'O':
        count += 1
    else:
        count = 0
    
    # カウントが K 以上か判定し処理
    if count >= K:
        ans += 1
        count -= K
    
    # i を更新
    i += 1
    
print(ans)

# 計算量 O(N) = O(1), N = 100 