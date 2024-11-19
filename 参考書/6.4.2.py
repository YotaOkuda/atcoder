# 十分大きい値
INF = 2 ** 60

# 入力
N = int(input())
h = list(map(int, input().split()))

# 再帰関数
def rec(i):
    # 終了条件
    if i == 0:
        return 0
    
    # 答え
    result = INF
    
    # 頂点 i - 1 から来た場合
    if i - 1 >= 0:
        result = min(result, rec(i - 1) + abs(h[i] - h[i - 1]))
        
    # 頂点 i - 2 から来た場合
    if i - 2 >= 0:
        result = min(result, rec(i - 2) + abs(h[i] - h[i - 2]))
        
    # 答えを返す
    return result

# 再帰的に求める
print(rec(N - 1))