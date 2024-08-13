S = input()

n = len(S)

i = 0
words = []

while i < n:
	j = i + 1
	while j < n and S[j].islower():
		j += 1
		
	words.append(S[i:j+1])
	i = j + 1

words.sort(key=str.lower)
result = "".join(words)

print(result)