N, Q = map(int, input().split())
S = input()

count = S.count('ABC')

for i in range(Q):
    X, C = input().split()
    X = int(X)
    S = S[:X - 1] + C + S[X:]
    if S[X -2:X + 1] == 'ABC':
        count += 1
    print(count)
# ans = []
#     ans.append(S.count('ABC'))
# for i in ans:
#     print(i)

# ABCの位置を記録しておく