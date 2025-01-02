# Optimal Code
# Time Complexcity -> O(N)
# Space Complexcity -> O(N)
def func(arr, k):
    count = 0
    total = 0
    hash_map = {0: 1}
    n = len(arr)
    for i in range(n):
        total += arr[i]
        if total - k in hash_map:
            count += hash_map[total - k]
        hash_map[total] = hash_map.get(total, 0) + 1
    return count


arr = [10, 2, -2, -20, 10]
k = -10
print(func(arr, k))
