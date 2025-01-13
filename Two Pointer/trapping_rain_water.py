# Optimal Code
# Sliding Window

# Time complexity -> O(N)
# Space complexity -> O()


def Maxwater(arr):
    n = len(arr)
    res = 0
    left, right = 0, n - 1
    left_max, right_max = arr[0], arr[n - 1]

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(arr[left], left_max)
            res += left_max - arr[left]
        else:
            right -= 1
            right_max = max(arr[right], right_max)
            res += right_max - arr[right]
    return res


arr = [3, 0, 1, 0, 4, 0, 2]
print(Maxwater(arr))
