'''
<方針>
- duos[i] は人i が隣り合った人のリスト
- duos ができたら、各人i について隣り合っていない人数の総和を取る
  最後に重複を除く（総和 / 2）
'''
N, M = map(int, input().split())

duos = [set() for _ in range(N)]
for i in range(M):
    A = list(map(int, input().split()))
    for j in range(N - 1):
        value = A[j] - 1
        next = A[j+1] - 1
        duos[value].add(next)
        duos[next].add(value)

ans = 0
for duo in duos:
    ans += N - 1 - len(duo)

print(int(ans / 2))

# 計算量 O(N * M)
