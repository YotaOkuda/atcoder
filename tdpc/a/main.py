'''
<方針>
- setとdpリスト両方使う？
- dp[i] はi点を取っているかを表す
'''
N = int(input())
P = list(map(int, input().split()))

points = set([0])

for i in range(N):
    M = len(points)
    for p in points:
        points.add(p + P[i])

print(len(points))
