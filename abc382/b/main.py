N, D = map(int, input().split())
S = list(input())

count = 0
for i in range(N - 1, -1, -1):
    if S[i] == '@':
        S[i] = '.'
        count += 1
        
    if count == D:
        break

print("".join(map(str, S)))