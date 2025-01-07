# Brute Force


def countPair(arr, target):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count


arr = [-1, 1, 5, 5, 7]
target = 6
print(countPair(arr, target))


# Optimize code


def func(arr, target):
    n = len(arr)
    count = 0
    hash_map = dict()
    for num in arr:
        rem = target - num
        if rem in hash_map:
            count += hash_map[rem]
        hash_map[num] = hash_map.get(num, 0) + 1
    return count


arr = [-1, 1, 5, 5, 7]
target = 6
print(func(arr, target))
