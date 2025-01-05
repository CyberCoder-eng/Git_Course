# Brute Foce

# Time Complexity -> O(N^2)
# Space Complexity -> O(1)


def countPair(arr, target):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] < target:
                count += 1
    return count


arr = [5, 2, 3, 2, 4, 1]
target = 5
print(countPair(arr, target))


# Optimal Approach

# Time Complexity -> O(n log n)
# Space Complexity -> O(1)


def func(arr, target):
    arr.sort()
    n = len(arr)
    count = 0
    i = 0
    j = n - 1
    while i < j:
        if arr[i] + arr[j] < target:
            count += j - i
            i += 1
        else:
            j -= 1
    return count


arr = [5, 2, 3, 2, 4, 1]
target = 5
print(func(arr, target))
