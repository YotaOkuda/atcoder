import sys

K = int(input())
S = list(str(input()))
T = list(str(input()))

count_diff = 0
if abs(len(S) - len(T)) > 1:
    print('No')
elif len(S) == len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            count_diff += 1
    print('No' if count_diff >= 2 else 'Yes')
elif len(S) < len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            T.pop(i)
            count_diff += 1
        if count_diff >= 2:
            print('No')
            sys.exit()
    print('Yes')
else:
    for i in range(len(T)):
        if S[i] != T[i]:
            S.pop(i)
            count_diff += 1
        if count_diff >= 2:
            print('No')
            sys.exit()
    print('Yes')
