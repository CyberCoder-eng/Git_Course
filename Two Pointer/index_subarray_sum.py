# Brute Force

# Time Complexity -> O(N^2)
# Space Complexity -> O(1)


def subarraySum(arr, target):
    n = len(arr)
    res = []
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total == target:
                res.append(i + 1)
                res.append(j + 1)
                return res
    return [-1]


arr = [1, 2, 3, 7, 5]
target = 12
print(subarraySum(arr, target))


# Sliding Window
# Optimal Approach


# Time Complexity -> O(N)
# Space Complexity -> O(1)
def func(arr, target):
    n = len(arr)
    res = []
    a, b = 0, 0
    total = 0
    for i in range(n):
        total += arr[i]
        if total >= target:
            b = i
            while total > target and a < b:
                total -= arr[a]
                a += 1
            if total == target:
                res.append(a + 1)
                res.append(b + 1)
                return res
    return [-1]


arr = [1, 2, 3, 7, 5]
target = 12
print(func(arr, target))
