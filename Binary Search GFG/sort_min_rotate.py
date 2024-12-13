# Optimize approach
# Time complexity -> O(Log N)
# Space complexity -> O(1)


def func(arr):
    n = len(arr)
    low = 0
    high = n - 1
    mini = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            mini = min(arr[low], mini)
            low = mid + 1
        else:
            mini = min(mini, arr[mid])
            high = mid - 1
    return mini


arr = [3, 4, 5, 1, 2]
print(func(arr))
