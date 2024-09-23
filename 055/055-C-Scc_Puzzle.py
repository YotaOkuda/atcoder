# N=Sの個数、M=Cの個数
N, M = map(int, input().split())

count = 0
if M - N*2 >= 0:  # (S=1,C=2)で作成して、Cに余りが出る場合
    count += N
    M -= N * 2  # Cの残りの個数を更新
    count += M // 4  # (C=4)で作れる数を求める
elif M - N*2 < 0:  # Cが足りなくて(S=1,C=2)でしか作成できない場合
    count += M // 2

print(count)


# (S=1,C=2) or (C=4)で'Scc'を一つ作れる
# (S=1,C=2)の方が多く作れるので先に計算する

# 計算量 O(1)


# もっと簡単に
if N >= M // 2:
    print(M // 2)
else:
    print(N + (M - N*2)//4)