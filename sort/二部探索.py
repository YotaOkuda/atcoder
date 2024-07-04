# N = list(map(int, input().split()))
N = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]

def binary_search(key):
    left = 0
    right = len(N) - 1
    while left <= right:
        mid = int((left + right)/2)
        print(left, mid, right)
        if N[mid] == key:
            return mid
        elif N[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

print(binary_search(51))