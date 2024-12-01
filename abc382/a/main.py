'''
<方針>
- '.', '@' の数をそれぞれカウントする
- '@' が D 個以上含まれるので、「dotCount + D」 を出力
'''

N, D = map(int, input().split())
S = str(input())

dotCount = S.count('.')
atCount = S.count('@')

print(dotCount + D)

# 計算量 O(N)