N = int(input())
S = str(input())

oneIndex = ((N + 1) // 2) - 1

flag = True
if N % 2 == 0:
    flag = False

if S[:oneIndex] != '1' * oneIndex:
    flag = False

if S[oneIndex] != '/':
    flag = False

if S[oneIndex + 1:] != '2' * (N - oneIndex - 1):
    flag = False
    
if flag:
    print('Yes')
else:
    print('No')