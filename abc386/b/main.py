S = str(input())

N = len(S)

ans = []
i = 0
while i < len(S):
    j = i
    while j < len(S) and S[j] == S[i]:
        j += 1
    
    if S[j - 1] == '0':
        N -= (j - i) // 2
    
    i = j
    
print(N)    