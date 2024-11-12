S = list(input())
T = list(input())

ans = 0
flag = True
for i, (s, t) in enumerate(zip(S, T)):
    # 文字が一致しない場合ansを更新
    if s != t: 
        ans = i + 1
        flag = False  # 長さが違う判定をスキップするため
        break

# 長さが違う かつ 文字が途中まで一致している場合
if len(S) != len(T) and flag:
    ans = min(len(S), len(T)) + 1
    
print(ans)


# 計算量 O(1)