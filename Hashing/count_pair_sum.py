# Brute Force
# Time complexcity -> O(N^2)
# Space complexcity -> O(1)


def func1(arr, target):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count


arr = [1, 5, 7, -1, 5]
target = 6
print(func1(arr, target))


# Optimal Approach

# Time complexcity -> O(N)
# Space complexcity -> O(N)


def func(arr, target):
    freq = dict()
    ans = 0
    for item in arr:
        temp = freq.get(target - item, 0)
        if temp:
            ans += temp
        freq[item] = freq.get(item, 0) + 1
    return ans


arr = [1, 5, 7, -1, 5]
target = 6
print(func(arr, target))
