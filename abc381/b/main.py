S = str(input())

N = len(S)

flag = True

if N % 2 != 0:
    flag = False

countString = set()
    
for i in range(1, N // 2 + 1):
    if S[2 * i - 2] != S[2 * i - 1]:
        flag = False
    countString.add(S[2 * i - 2])

if len(countString) != N // 2:
    flag = False

if flag:    
    print('Yes')
else:
    print('No')