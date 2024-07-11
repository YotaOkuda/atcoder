from collections import defaultdict

N = int(input())

num = defaultdict(int)

for _ in range(N):
    s = input()
    num[s] += 1

max_value = max(num.values())
for key in sorted(num):
    if num[key] == max_value:
        print(key)