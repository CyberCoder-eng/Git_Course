# Optimal Approach

# Time complexcity -> O(N + M)
# Space complexcity -> O(N + M)


def func(a, b):
    res = []
    set_b = set(b)

    for num in a:
        if num in set_b:
            res.append(num)
            set_b.remove(num)
    return res


a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]
print(func(a, b))
