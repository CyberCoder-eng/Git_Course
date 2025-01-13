# def func(arr):
#     n = len(arr)
#     res = 0
#     for i in range(n):
#         for j in range(i + 1, 1):
#             mini = min(arr[i], arr[j]) * (j - i)
#             res = max(mini, res)
#     return res


# arr = [1, 5, 4, 3]
# print(func(arr))


def maxwater(arr):
    n = len(arr)
    left, right = 0, n - 1
    res = 0

    while left < right:
        mini = min(arr[left], arr[right]) * (right - left)
        res = max(mini, res)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return res


arr = [1, 5, 4, 3]
print(maxwater(arr))
