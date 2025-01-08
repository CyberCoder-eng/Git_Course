# Optimize Approach

# Time complexity -> O(N^2)
# Space complexity -> O(1)


def countTriangles(arr):
    count = 0
    arr.sort()
    n = len(arr)
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1

        while left < right:
            if arr[left] + arr[right] > arr[i]:
                count += right - left
                right -= 1
            else:
                left += 1

    return count


arr = [4, 6, 3, 7]
print(countTriangles(arr))
