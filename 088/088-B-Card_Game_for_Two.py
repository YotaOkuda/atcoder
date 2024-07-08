n = int(input())
A = list(map(int, input().split()))

Alice = 0
Bob = 0

A.sort(reverse=True)
for i in range(n):
    if i%2 == 0:
        Alice += A[i]
    else:
        Bob += A[i]

print(Alice - Bob)

#AliceとBobの二つの変数を使わず一つの変数のみで表現
'''result = 0
if i%2 == 0:
    result += A[i]
else:
    result -= A[i]'''