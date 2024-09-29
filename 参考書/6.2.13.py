N, W = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

# 0, 1 からなる長さNの数列を全列挙して調べる
# n:「0, 1 からなる数列A」の長さ
# sw:現在の数列Aに対応する品物の重さの総和
# sv:現在の数列Aに対応する品物の価値の総和
def rec(n, sw, sv):
    # 終了条件
    if n == N:
        return sv
    
    # 価値の最大値を表す変数
    result = 0
    
    # 数列Aの次の要素を0とする場合
    # 新たな品物を「選ばない」場合に対応する
    score = rec(n + 1, sw, sv)
    result = max(result, score)
    
    # 数列Aの次の要素を1とする場合
    # 新たな品物を「選ぶ」場合に対応する
    # 重さはw[n]増加し、価値はv[n]増加する
    if sw + w[n] <= W:
        score = rec(n + 1, sw + w[n], sv + v[n])
        result = max(result, score)
        
    # 最大値を返す
    return result

# 空の状態から開始して、再起的に解を求める
print(rec(0, 0, 0))