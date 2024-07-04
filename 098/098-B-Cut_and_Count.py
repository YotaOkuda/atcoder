from collections import Counter

N = int(input())
S = input()

ans = 0

for n in range(1, N):
    common_count = 0    # 共通文字の個数カウンター
    s1_counter, s2_counter = Counter(S[:n]), Counter(S[n:])
    common_counter = s1_counter & s2_counter

    for value in common_counter.values():
        if value >= 1:
            common_count +=1
    
    ans = max(common_count, ans)

print(ans)