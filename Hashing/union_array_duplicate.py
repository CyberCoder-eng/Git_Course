def union_arr(a, b):
    return len(set(a).union(set(b)))


a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
print(union_arr(a, b))

# Optimal Approach

# Time complexcity -> O(N + M)
# Space complexcity -> O(N + M)


def func(a, b):
    hash_map = set(b)
    for num in a:
        hash_map.add(num)
    return len(hash_map)


a = [1, 2, 1, 1, 2]
b = [2, 2, 1, 2, 1]
print(func(a, b))
