'''
<方針>
- 文字列を 2 つずつ見て一致しているか確認する
- 一致している場合、その部分列については初回の出現であるか（リストに存在するかで管理）
'''

N = int(input())
A = list(map(int, input().split()))

ans = 0
i = 0
while i < N:
    if i + 1 < N and A[i] == A[i + 1]:
        # print(f'i{i}')
        j = i
        list = []
        while j + 1 < N and A[j] == A[j + 1]:
            if A[j] in list:
                break
            list.append(A[j])
            j += 2
        ans = max(ans, len(list) * 2)    
        i = j
    else:
        i += 1

print(ans)