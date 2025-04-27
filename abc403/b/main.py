'''
<方針>
- 文字列 U 分、文字列 T の先頭から一文字ずつ比較していく
- 連続部分文字列を含むかの状態を bool値 で保持する
- 比較する文字が '?' もしくは、一致しない場合はカウントする
- カウントが len_U に達したら連続部分文字列とする
'''

T = str(input())
U = str(input())

len_T = len(T)
len_U = len(U)

ans = False
for i in range(len_T - len_U + 1):
    # U と比較する文字列を T から切り出す
    check_str = T[i:i+len_U]
    # len_U 分すべて部分文字列かをカウントする
    count = 0
    for j in range(len_U):
        if check_str[j] == '?' or check_str[j] == U[j]:    
            count += 1 
        if count == len_U:
            ans = True

print('Yes' if ans else 'No')

# 計算量 O(len_T ^ 2)
