'''N = int(input())
A = list(map(int, input().split()))
max = max(A)
min = min(A)
print(max - min)'''

#別解for文1つだけ　
N = int(input())
A = list(map(int, input().split()))
min = A[0]
max = A[0]
for a in A:
    if a < min:
        min = a
    if a > max:
        max = a

print(max-min)