'''
<方針>
- A, B, C を見つけて各インデックスが等間隔ならカウントする
'''

S = str(input())

# リファクタリング後
count = 0
for i in range(len(S)):
  for j in range(i + 1, len(S)):
    for k in range(j + 1, len(S)):
      if j - i == k - j and S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
        count += 1

print(count)

# 計算量 O(N ^ 3)


# リファクタリング前（計算量はこっちのが少ない）、条件は見づらい
'''
for i in range(len(S)):
  if S[i] == 'A':
    for j in range(i + 1, len(S)):
      if S[j] == 'B':
        for k in range(j + 1, len(S)):
          if (S[k] == 'C') & ((j - i) == (k - j)):
            count += 1
'''