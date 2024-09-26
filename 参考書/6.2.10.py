# 数列AのサイズNを仮に3としておく
N = 4
# 0,1からなる長さNの数列Aを列挙
def rec(A):
    # 終了条件 --- AのサイズがNに達したら終了
    if len(A) == N:
        print(A)
        return
    
    for v in range(2):
        A.append(v)  # Aに要素を追加したうえで
        rec(A)       # 再帰的に呼び出す
        A.pop()      # Aを元に戻す
        
# 空の配列から開始
rec([])