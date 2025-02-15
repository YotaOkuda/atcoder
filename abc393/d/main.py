import sys
N = int(input())
S = str(input())

count1 = 0
min1 = N
max1 = 0
for i in range(N):
  if S[i] == '1':
    count1 += 1
    min1 = min(i, min1)
    max1 = max(i, max1)

if count1 == 1:
  print(0)
  sys.exit()
elif count1 == 2:
  print(max1 - min1 - 1)
  sys.exit()

min_far = N
for i in range(min1 + 1, max1):
  max_far = 0
  if S[i] == '1':
    max_far = max(i - min1, max1 - i)
    if min_far > max_far:
      base_index = i
      min_far = max_far

ans = 0
coma = 0
for i in range(base_index - 1, min1 - 1, -1):
  if S[i] == '1':
    ans += base_index - i - 1 - coma
    coma += 1

coma = 0
for i in range(base_index + 1, max1 + 1):
  if S[i] == '1':
    ans += i - base_index - 1 - coma
    coma += 1

print(ans)