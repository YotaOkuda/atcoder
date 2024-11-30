N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

minA = min(A)
for b in B:
    if minA > b:
        print(-1)
    else:
        for i, a in enumerate(A):
            if a <= b:
                print(i + 1)
                break


'''
indicesA = [*range(len(A))]
sorted_indicesA = sorted(indicesA, key=lambda i: A[i])
sorted_A = [A[i] for i in sorted_indicesA]

indicesB = [*range(len(B))]
sorted_indicesB = sorted(indicesB, key=lambda i: B[i])
sorted_B = [B[i] for i in sorted_indicesB]

ans = []

print(f'sorted_A:{sorted_A}')
print(f'sorted_indicesA:{sorted_indicesA}')
print(f'sorted_B:{sorted_B}')
print(f'sorted_indicesB:{sorted_indicesB}')

for b in sorted_B:
    if sorted_A[0] > b:
        ans.append(-1)
    elif sorted_A[0] == b:
        ans.append(sorted_indicesA[0] + 1)
    else:
        for i, a in enumerate(sorted_A):
            if a > b:
                #print(f'i:{i}, a:{a}, b:{b}')
                ans.append(sorted_indicesA[i - 1] + 1)
                #sorted_A.pop(i - 1)
                #sorted_indicesA.pop(i - 1)
                break

for indexB in sorted_indicesB:
    print(ans[indexB])
'''