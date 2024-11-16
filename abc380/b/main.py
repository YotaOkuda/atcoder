S = str(input())

ans = []
i = 0
while i < len(S):
    j = i + 1
    
    while j < len(S) and S[j] == '-':
        j += 1
    
    ans.append(j - i - 1)
    
    i =  j
    
ans.pop(-1)

print(*ans)    