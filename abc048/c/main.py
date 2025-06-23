'''
- 貪欲法で解く
- a[i] + a[i + 1] > x の時には a[i] > x でない限り a[i + 1] を減らすことで、
  a[i + 1] + a[i + 2] をより少ない数減らすことが可能になる
'''

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    if A[i] + A[i + 1] <= X:
        continue
    else:
        if A[i] > X:
            ans += A[i] - X
            ans += A[i + 1]
            A[i] = X
            A[i + 1] = 0
        else:
            minus = A[i] + A[i + 1] - X
            ans += minus
            A[i + 1] -= minus

print(ans)        

# 計算量 O(N)
