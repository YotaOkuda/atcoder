import bisect

N = int(input())
A = list(map(int, input().split()))

ans = 0

for a in A:
    ans += N - bisect.bisect_left(A, a * 2)
    

print(ans)