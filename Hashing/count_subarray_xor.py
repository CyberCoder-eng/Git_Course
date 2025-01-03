# Optimal Code

# Time complexcity -> O(N)
# Space complexcity -> O(N)


def subarrayXor(arr, k):
    hash_map = dict()
    count = 0
    xor = 0
    for i in range(len(arr)):
        xor ^= arr[i]
        if xor == k:
            count += 1

        if xor ^ k in hash_map:
            count += hash_map[xor ^ k]
        hash_map[xor] = hash_map.get(xor, 0) + 1
    return count


arr = [4, 2, 2, 6, 4]
k = 6
print(subarrayXor(arr, k))
