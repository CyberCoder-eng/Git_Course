# Brute Force

# Time Complexcity -> O(N^2)
# Space Complexcity -> O(1)


def twoSum(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    return False


arr = [1, 4, 45, 6, 10, 8]
target = 16
print(twoSum(arr, target))


# Optimal Approach

# Time Complexcity -> O(N)
# Space Complexcity -> O(N)


def func(arr, target):
    n = len(arr)
    hash_map = dict()
    for i in range(n):
        rem = target - arr[i]
        if rem in hash_map:
            return [hash_map[rem], i]
        hash_map[arr[i]] = i


arr = [1, 4, 45, 6, 10, 8]
target = 16
print(func(arr, target))
