N = int(input())
A = list(map(int, input().split()))

i = 0
ans = 0

# iがN未満の間
while i < N:
    if i+1 < N and A[i] == A[i+1]:      # A[i],A[i+1]が一致するなら
        ans -= 1                        # ansの変動はないのでマイナス
    elif i+1 < N and A[i] < A[i+1]:     
        while i+1 < N and A[i] <= A[i+1]:   # A[i]<=A[i+1]が続くまで右に一つずつ移動
            i += 1
    elif i+1 < N and A[i] > A[i+1]:         
        while i+1 < N and A[i] >= A[i+1]:   # A[i]>=A[i+1]が続くまで右に一つずつ移動
            i += 1
    
    ans += 1    # 単調増加・減少の区間分割
    i += 1      # iの始点を移動

print(ans)