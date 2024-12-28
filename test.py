from collections import Counter

K = int(input())
S = str(input())
T = str(input())

diff = Counter(S) - Counter(T)
print(diff)