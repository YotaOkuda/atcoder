N, c1, c2 = map(str, input().split())
S = list(str(input()))

for i in range(int(N)):
    if S[i] != c1:
        S[i] = c2
    
print(''.join(map(str, S)))