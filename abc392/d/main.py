from collections import defaultdict
import itertools

N = int(input())

scy = []
for i in range(N):
  A = list(map(int, input().split()))
  num = defaultdict(int)

  for j in range(A[0]):
    num[A[j + 1]] += 1
  scy.append(num)

max_value = 0
for v in itertools.combinations(scy, 2):
  total = 0
  for key in v[0]:
    if v[1][key]:
      total = total + (v[0][key] * v[1][key])
  
  print(total)