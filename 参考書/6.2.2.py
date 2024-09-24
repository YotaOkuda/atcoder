def rec(N):
    # 終了条件を最初に記述
    # 再起呼び出しを行わず直接returnする
    if N == 0:
        return 0
    
    return N + rec(N -1)

# rec(5)を呼び出したとき、rec(0)から値が返されることに注意