'''S = input()
n = len(S)
print(S[0] +str(n-2) +S[n-1])'''

#別解
S = input()
print(S[0] + str(len(S)-2) + S[-1])