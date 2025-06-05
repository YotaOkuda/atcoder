'''
<方針>
- T と一致する Ci がある場合と、ない場合に分けて考える
- ある場合：一致する Ci があり、最大値を更新できるならインデックスも更新する
  - 初期値は範囲外の -1 とする
- ない場合：C[0] と一致する Ci があり、最大値を更新できるならインデックスも更新する
  - 初期値は R[0] と 1（index は 1 始まりなため）
'''

N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

if T in C:
    max_value = -1
    max_index = -1
    for i in range(N):
        if C[i] == T:
            if R[i] > max_value:
                max_value = R[i]
                max_index = i + 1
else:
    max_value = R[0]
    max_index = 1
    for i in range(N):
        if C[i] == C[0]:
            if R[i] > max_value:
                max_value = R[i]
                max_index = i + 1

print(max_index)

# 計算量 O(N)
