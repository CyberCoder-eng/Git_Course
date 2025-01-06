# Optimize Code


# Time complexity -> O(n log n)
# Space complexity -> O(1)


def func(arr, target):
    arr.sort()
    n = len(arr)
    left = 0
    right = n - 1
    res = []
    total = float("inf")

    while left < right:
        curr_total = arr[left] + arr[right]
        if abs(target - curr_total) < abs(target - total):
            total = curr_total
            res = [arr[left], arr[right]]
        if curr_total < target:
            left += 1
        elif curr_total > target:
            right -= 1
        else:
            break
    return res


arr = [5, 2, 7, 1, 4]
target = 10
print(func(arr, target))
