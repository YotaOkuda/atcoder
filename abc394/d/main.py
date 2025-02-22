'''
<方針>
- 先頭から見て (), [], <> を見つけたら空白にする
- 操作を行ったら i -= 1 し、S[j] が対となる記号なら空白にする
? 計算量、WAも出ている
'''

S = list(str(input()))
S_insert = S
N = len(S)

i = 0
while i < N - 1:
    j = i + 1
    # print(f'i:{i}, j:{j}')
    flag = True
    if S[i] == '(' or S[i] == '<' or S[i] == '[':
        while S[j] == "":
            j += 1
        if (S[i] == '(' and S[j] == ')') or (S[i] == '<' and S[j] == '>') or (S[i] == '[' and S[j] == ']'): 
            S[i], S[j] = "", ""
            i -= 1
            flag = False
    if flag:
        i = j

ans = "".join(S)
print('Yes' if len(ans) == 0 else 'No')