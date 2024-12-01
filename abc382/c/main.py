N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

'''
indicesA = [*range(len(A))]
sorted_indicesA = sorted(indicesA, key=lambda i: A[i])
sorted_A = [A[i] for i in sorted_indicesA]
'''

indexed_list = sorted([(value, idx) for idx, value in enumerate(A)])
result = []
seen = set()
for value, idx in indexed_list:
    if value not in seen:
        result.append([value, idx])
        seen.add(value)

minA = min(A)

def isOK(index, key):
    if result[index][0] >= key:
        return True
    else:
        return False
    
def binary_serch(key):
    left = -1
    right = len(result)
    
    while abs(right - left) > 1:
        mid = int((left + right) / 2)
        # print(left, mid, right)
        
        if isOK(mid, key):
            right = mid
        else:
            left = mid
            
    if left == -1:
        return result[0][1]
    else:
        return result[left][1]

for b in B:
    if b < minA:
        print(-1)
    else:
        print(binary_serch(b) + 1)
    