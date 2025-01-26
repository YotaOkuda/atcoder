'''
<方針>
- 公比が正数とは限らずエラーが出る
- 前項 * 次項（A[i - 1] * A[i + 1]）= 現在項 * 現在項（A[i] * A[i]）が必ず成り立つことを利用
'''

N = int(input())
A = list(map(int, input().split()))

# 等比数列となっているかを判定するフラグ
flag = True
# 各項について法則が成り立つか調べる
for i in range(1, N - 1):
    if A[i - 1] * A[i + 1] != A[i] * A[i]:
        flag = False
        
print('Yes' if flag else 'No')

# 計算量 O(N)


# --- 1 つ WA がでたコード ---
'''
ratio = A[1] / A[0]
make_A = [A[0]]
while len(A) != len(make_A):
    make_A.append(int(make_A[-1] * ratio))

print('Yes' if A == make_A else 'No')
'''

