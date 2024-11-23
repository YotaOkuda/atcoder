'''
<方針>
- 素直に全条件を確認する
- 文字列が奇数かどうか
- '111...' が連続するインデックスをもとめ、'1', '/', '2' で構成されているか
  '1', '2' かどうか かつ 適切な長さか判定する
'''

N = int(input())
S = str(input())

# '1' が続くインデックスを条件式から求める
oneIndex = ((N + 1) // 2) - 1

# 条件を満たしているか表すフラグ
flag = True

# 文字列の長さが奇数であるか
if N % 2 == 0:
    flag = False

# '1' 部分が正しいか
if S[:oneIndex] != '1' * oneIndex:
    flag = False

if S[oneIndex] != '/':
    flag = False

# '2' 部分が正しいか（'1' 部分と同じ長さ）
if S[oneIndex + 1:] != '2' * (N - oneIndex - 1):
    flag = False
    
# 答えを出力
if flag:
    print('Yes')
else:
    print('No')
    
# 計算量 O(N) = O(1), 1 <= N <= 100