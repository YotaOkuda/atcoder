X, A, B = map(int, input().split())

# 賞味期限を過ぎていない場合
if A >= B:
    print('delicious')
# 賞味期限を過ぎたが、おなかを壊さない場合
elif A < B and (B - A) <= X:
    print('safe')
# おなかを壊す場合
else:
    print('dangerous')
    

# 計算量 O(1)