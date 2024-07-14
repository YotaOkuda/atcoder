S = str(input())

i = 0
ans = []
while i < len(S):
    j = i + 1   # jはiの次から探索

    # 大文字で始まり大文字で終わる場所の探索
    while j < len(S) and S[i].isupper() and S[j].islower(): # jは大文字で終わる位置、S[i].isupper()はなくてもいい
        j += 1

    ans.append(S[i:j+1])    # jをそのまま入れると-1されるので+1しておく

    i = j + 1   # iはjの次の文字列の位置に設定

ans.sort(key = str.lower)   # 大文字小文字を区別しないでソート
print(''.join(ans))

# 計算量O(NlogN) < 10^8