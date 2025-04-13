'''
<方針>
- S が 200 以上 299 以下の範囲かを確認する
'''

S = int(input())

if 200 <= S <= 299:
    print("Success")
else:
    print("Failure")
    
# 計算量 O(1)