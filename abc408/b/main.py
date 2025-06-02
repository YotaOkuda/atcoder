'''
<方針>
- set で重複を取り除く
- リストにしてからソートする
'''

N = int(input())
A = set(list(map(int, input().split())))

A = list(A)
A.sort()
print(len(A)) 
print(*A)

# 計算量 O(NlogN)
