N = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]
# N = [1]
def isOK(index, key):
    if N[index] >= key:
        return True
    else:
        return False
    
def binary_search(key):
    left = -1
    right = len(N)

    while right - left > 1:
        mid = int(left + (right - left)/2)
        print(left, mid, right)

        if isOK(mid, key):
            right = mid
        else:
            left = mid
    
    return right

print(binary_search(49))