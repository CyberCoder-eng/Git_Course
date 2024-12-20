# Brute Force

# Time complexity -> O(N)
# Space complexity -> O(N)


def func(arr, k):
    n = len(arr)
    current = 0
    count = 0
    hash_map = set(arr)
    while count < k:
        current += 1
        if current not in hash_map:
            count += 1
    return current


arr = [2, 3, 4, 7, 11]
k = 5
print(func(arr, k))


# Optimize Approach

# Time complexity -> O(Log N)
# Space complexity -> O(0)


def func1(arr, k):
    n = len(arr)
    low = 0
    high = n - 1
    res = len(arr) + k
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > mid + k:
            res = mid + k
            high = mid - 1
        else:
            low = mid + 1
    return res


arr = [2, 3, 4, 7, 11]
k = 5
print(func(arr, k))
