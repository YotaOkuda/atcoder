'''
<方針>
- 直接会話 : A, C さんの距離の差
- 間接的に会話 : A, B and B, C さんの距離の差
- 上記二つのケースで会話可能か判断する
'''

a, b, c, d = map(int, input().split())

# 直接会話
distance_AC = abs(a - c)

# 間接的に会話
distance_AB = abs(a - b)
distance_BC = abs(b - c)

# 会話可能か判定
if distance_AC <= d:    # 直接会話可能
    print('Yes')
elif distance_AB <= d and distance_BC <= d:     # 間接的に会話可能
    print('Yes')
else:                   # 会話不可能
    print('No')
    
# 計算量 O(1)