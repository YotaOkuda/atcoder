'''
N, X = map(int, input().split())

def rec(N, X, L, S):
    if N == 0:
        return 1
        
    # Xの長さに応じて条件分岐
    if X == 1:
        return 0
    elif X <= L[N - 1] + 1:
        return rec(N - 1, X - 1, L, S)
    elif X == L[N - 1] + 2:
        return S[N - 1] + 1
    elif X <= 2*L[N - 1] + 2:
        return rec(N - 1, X - L[N - 1] - 2, L, S) + S[N - 1] + 1
    else:
        return 2*S[N - 1] + 1

# バーガーの長さ L とパティ数 S    
L = [1] * (N + 1)
S = [1] * (N + 1)

for n in range(1, N + 1):
    L[n] = L[n - 1]*2 + 3
    S[n] = S[n - 1]*2 + 1    

print(rec(N, X, L, S))
'''

# 計算量 O(N)


# re
N, X = map(int, input().split())

def rec(N, X, L, S):
    if N == 0:
        return 1
    
    if X == 1:
        return 0
    elif X <= L[N - 1] + 1:
        return rec(N - 1, X - 1, L, S)
    elif X == L[N - 1] + 2:
        return S[N - 1] + 1
    elif X <= 2*L[N -1] + 2:
        return rec(N - 1, X - L[N - 1] - 2, L, S) + S[N - 1] + 1
    else:
        return 2*S[N - 1] + 1
    
L = [1] * (N + 1)
S = [1] * (N + 1)

for i in range(1, N + 1):
    L[i] = 2*L[i - 1] + 3
    S[i] = 2*S[i - 1] + 1
    
print(rec(N, X, L, S))