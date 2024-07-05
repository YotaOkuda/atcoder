from collections import Counter

N = int(input())
S = input()

ans = 0

for n in range(1, N):
    common_count = 0    # 共通文字の個数カウンター
    s1_counter, s2_counter = Counter(S[:n]), Counter(S[n:]) # Counterメソッド、文字列に含まれる各文字の個数を格納
    common_counter = s1_counter & s2_counter    # 共通の文字のみ取り出す

    for value in common_counter.values():   # valuesメソッドで値を取り出す
        if value >= 1:                      # 重複は考慮しないので1以上（共通の文字）でカウント
            common_count +=1
    
    ans = max(common_count, ans)            # 最大の共通文字を更新

print(ans)