a, b = map(int, input().split())

count = 0
for s in range(a, b + 1, 1):
    s = str(s)
    if s[0] == s[4] and s[1] == s[3]:
        count += 1

print(count)