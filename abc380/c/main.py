from collections import defaultdict

N, K = map(int, input().split())
S = str(input())

oneBlock = []

i = 0
while i < len(S):
    j = i
    
    if S[j] == '1':
        while j < len(S) and S[j] == '1':
            j += 1
        oneBlock.append([i, j, '1' * (j - i)])
    else:
        while j < len(S) and S[j] != '1':
            j += 1
    
    i = j
    

kStart, kEnd, kOne = oneBlock[K - 1]
S = S[:kStart] + S[kEnd:]

k1Start, k1End, k1One = oneBlock[K - 2]
S = S[:k1End] + kOne + S[k1End:]
print(S)