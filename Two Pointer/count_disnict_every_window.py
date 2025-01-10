def countWindow(arr, k):
    hash_map = dict()
    res = []
    for i in range(k):
        hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1
    res.append(len(hash_map))
    for i in range(k, len(arr)):
        rem = arr[i - k]
        hash_map[rem] -= 1
        if hash_map[rem] == 0:
            del hash_map[rem]

        num = arr[i]
        hash_map[num] = hash_map.get(num, 0) + 1
        res.append(len(hash_map))
    return res


arr = [1, 2, 1, 3, 4, 2, 3]
k = 4
print(countWindow(arr, k))
