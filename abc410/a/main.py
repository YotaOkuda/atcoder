'''
<方針>
- K が a 以下ならば、K はレースに参加できる
'''

N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = 0
for a in A:
    if a >= K:
        ans += 1

print(ans)

# 計算量 O(N)
