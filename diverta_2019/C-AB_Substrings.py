N = int(input())

# あらかじめ文字列に含まれる'AB'の数
count = 0
# # ..A = x, B.. = y, B..A = zの数
x, y, z = 0, 0, 0

for _ in range(N):
    s = str(input())
    count += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        z += 1
    elif s[0] == 'B':
        y += 1
    elif s[-1] == 'A':
        x += 1

# zだけで'AB'を最大化
if x == 0 and y == 0:
    ans = count + max(z - 1, 0)
# x,yを使用するとき
elif x >= 1 or y >= 1:
    ans = count + z + min(x, y)

print(ans)


# 計算量 O(N)