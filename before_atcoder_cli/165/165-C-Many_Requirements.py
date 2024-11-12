N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    

ans = []
def rec(A):
    # 数列ができたら、得点の計算を呼び出す
    if len(A) == N:
        count = calc(A)
        ans.append(count)
        # print(f'A: {A}')
        # print(f'count: {count}') 
        return
    
    # N個でM以下の値で構成される数列を列挙
    # A[i] <= A[i + 1]を満たす場合のみ
    for v in range(1, M + 1):
        if not A or (A and A[-1] <= v):
            A.append(v)
            rec(A)
            A.pop()
        
# 数列Aに対する得点を計算
def calc(A):
    sum = 0
    for i in range(Q):
        if A[b[i] - 1] - A[a[i] - 1] == c[i]:
            sum += d[i]
    
    return sum

rec([])
# 最大値を出力
print(max(ans))


# 数列を全て作成してからA[i] <= A[i + 1]を確認するとTLE
# 作成途中でチェックすることで計算量削減

# 計算量 O(10^5 * Q)
# 10^5 = 数列の総数（条件をチェックしているので実際はこれより少ない）



## 模範解答 ##
N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())

    # 数列Aの添字a[i], b[i]を0始まりにする
    a[i] -= 1
    b[i] -= 1
    
# 数列Aのスコアを計算する関数
def calc_score(A):
    score = 0
    for ai, bi, ci, di in zip(a, b, c, d):
        if A[bi] - A[ai] == ci:
            score += di
        
    return score

# 数列Aを全列挙してスコアの最大値を求める再帰関数
def rec(A):
    # 終了条件
    if len(A) == N:
        return calc_score(A)
    
    # 最大値
    result = 0
    
    # 数列Aの前回要素を取得
    prev_last = A[-1] if A else 1
    
    # 数列Aが単調増加になるように末尾に要素を追加
    for add in range(prev_last, M + 1):
        # 数列Aに要素追加
        A.append(add)
        
        # 再帰呼び出しをしながら、スコア最大値を更新
        result = max(result, rec(A))
        
        # 数列Aの末尾を削除して元に戻す
        A.pop()
        
    # 最大値を返す
    return result

# 数列Aを全列挙して調べる
A = []
print(rec(A))



## 模範回答2 ##
from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    
    a[i] -= 1
    b[i] -= 1

    
def calc(A):
    sum = 0
    for ai, bi, ci, di in zip(a, b, c, d):
        if A[bi] - A[ai] == ci:
            sum += di
        
    return sum


result = 0

for A in combinations_with_replacement(range(1, M + 1), N):
    result = max(result, calc(A))

print(result)