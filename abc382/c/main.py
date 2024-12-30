'''
<方針>
- ある美味しさ Bj が美食度 An より高い場合、An-1 < An が成立すれば An+1 は絶対に食べることはできない
- 数列 A を単調減少にした数列を新たに作る
- 値とインデックスを記録しておく
- 二部探索で各 Bj に対して、Bj > An となる最小の An を求める
'''

# 入力
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A の最小値を求めておく
min_a = min(A)

# A を左から見て、単調減少にしていくリスト
monotony_a = []
monotony_a.append(A[0])
# {美食度 : index} の dict
value_to_index = {A[0]: 0}
# 現在の最小値
current_min = A[0]
# 単調減少リスト、dict を作る
for i in range(1, N):
    if A[i] < current_min:
        current_min = A[i]
        monotony_a.append(A[i])
        value_to_index[A[i]] = i

# 配列を反転
monotony_a.reverse()

# 二部探索
def isOK(index, key):
    if monotony_a[index] > key:
        return True
    else:
        return False
    
def binary_serch(key):
    left = -1
    right = len(monotony_a)
    
    while abs(right - left) > 1:
        mid = int((left + right) / 2)
        
        if isOK(mid, key):
            right = mid
        else:
            left = mid
            
    return monotony_a[left]

# 各 Bj について、食べる人を求めていく
for b in B:
    # 食べる人がいない場合
    if b < min_a:
        print(-1)
    else:
        print(value_to_index[binary_serch(b)] + 1)

# 計算量 O(N + M log N), 二部探索の部分は O(M log N)