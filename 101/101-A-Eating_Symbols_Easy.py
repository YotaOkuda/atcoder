'''
<方針>
- '+', '-' の数をカウントして計算し、出力する
'''

S = input()

# '+', '-' の数をそれぞれカウント
plus = S.count('+')
minus = S.count('-')

print(plus - minus)