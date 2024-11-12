'''
<方針>
- 辞書順 K 番目の文字列の長さが K を超えることはないので、s の部分文字列のうち K 文字以下のものだけ列挙する
- 最後に辞書順になるようソートする
'''

s = input()
K = int(input())

# 文字列を列挙するセット、重複がないようにセットにする
substring_set = set()

# 切り出す範囲を 1 から K としてループ
for i in range(1, K + 1):
    start = 0
    end = i
    
    # 文字列の最後尾を超えるまで
    while end < len(s) + 1:
        # セットに切り出した文字列を追加
        substring_set.add(s[start:end])
        
        # 始点、終点を更新
        start += 1
        end += 1
    
# ソートする
substring_list = sorted(substring_set)

print(substring_list[K - 1])

# 計算量 O(n^2 * log n)