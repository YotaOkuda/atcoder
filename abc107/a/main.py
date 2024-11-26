'''
<方針>
- N - i で残りの車両を計算し、後ろからのインデックスに合わせて + 1
'''

N, i = map(int, input().split())

print(N - i + 1)

# 計算量 O(1)