N = int(input())
A = list(map(int, input().split()))

i = 0
ans = 0
while i < N:
    if i+1 < N and A[i] == A[i+1]:
        ans -= 1
    elif i+1 < N and A[i] < A[i+1]:
        while i+1 < N and A[i] <= A[i+1]:
            i += 1
    elif i+1 < N and A[i] > A[i+1]:
        while i+1 < N and A[i] >= A[i+1]:
            i += 1
    
    ans += 1
    i += 1

print(ans)