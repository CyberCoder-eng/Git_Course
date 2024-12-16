# Brute Froce


def func1(a, b, k):

    res = a + b
    print(res)
    ans = sorted(res)
    print(ans)
    return ans[k - 1]


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(func1(a, b, k))


# Optimize solution


def func(a, b, k):
    n, m = len(a), len(b)
    i = j = count = 0

    while i < n and j < m:
        if a[i] < b[j]:
            count += 1
            if count == k:
                return a[i]
            i += 1
        else:
            count += 1
            if count == k:
                return b[j]
            j += 1
    while i < n:
        count += 1
        if count == k:
            return a[i]
        i += 1

    while j < m:
        count += 1
        if count == k:
            return b[j]
        j += 1
    return -1


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(func(a, b, k))
