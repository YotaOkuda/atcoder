# 区間分割・連長圧縮

S = str(input())
N = len(S)

i = 0
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
    print(S[i], j -  i)
    i = j