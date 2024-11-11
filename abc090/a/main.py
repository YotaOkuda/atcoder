'''
<方針>
- ループ処理で特定の文字を抽出する
'''

C = []
for i in range(3):
    C.append(input())
    
print(C[0][0] + C[1][1] + C[2][2])

# 計算量 O(1)