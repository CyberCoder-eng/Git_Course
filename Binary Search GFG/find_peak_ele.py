# Optimize approach

# Time Complexity -> O(Log N)
# Space Complexity -> O(1)


def func(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[-2]:
        return n - 1

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1
    return "false"


arr = [1, 2, 4, 5, 7, 8, 3]
print(func(arr))
