N, D = map(int, input().split())
S = str(input())

dotCount = S.count('.')
atCount = S.count('@')

if atCount >= D:
    print(dotCount + D)
else:
    print(N)