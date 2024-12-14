# Brute force approach


# Time Complexity -> O(N)
# Space Complexity -> O(1)
def search_sort(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
target = 3

print(search_sort(arr, target))


# Optimize approach


# Time Complexity -> O(Log N)
# Space Complexity -> O(1)
def func(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
target = 3
print(func(arr, target))
