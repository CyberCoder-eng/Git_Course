# Brute force
# Time complexcity -> O(N^2)
# Space complexcity -> O(1)


def longSubsequnce(arr):
    longest = 0
    for num in arr:
        count = 1
        x = arr
        while x + 1 in num:
            count += 1
            x += 1
        longest = max(longest, count)
    return longest


arr = [2, 6, 9, 4, 1, 5, 3]
print(longSubsequnce(arr))

# Optimal Approach


# Time complexcity -> O(N)
# Space complexcity -> O(N)
def func(arr):
    hash_map = set()
    longest = 0
    for num in arr:
        hash_map.add(num)
    for num in hash_map:
        if num - 1 not in hash_map:
            x = num
            count = 1
            while x + 1 in hash_map:
                count += 1
                x += 1
            longest = max(longest, count)
    return longest


arr = [2, 6, 9, 4, 1, 5, 3]
print(func(arr))
