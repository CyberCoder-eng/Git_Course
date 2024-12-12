def countFreq(arr, target):
    n = len(arr)
    count = 0

    for i in range(n):
        if arr[i] == target:
            count += 1
    return count


# Brute and Batter Approach
# Time complexity -> O(N)
# Space complexity -> O(1)


# Optimize Approach

from bisect import bisect_right, bisect_left


def func(arr, target):
    return bisect_right(arr, target) - bisect_left(arr, target)


# Time complexity -> O(Log N)
# Space complexity -> O(1)
