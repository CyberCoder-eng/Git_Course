# Optimal Approach

# Time complexcity -> O(n*m)
# Space complexcity -> O(1)


def searchmatrix(arr, target):
    for num in arr:
        if target in num:
            return True
    return False


arr = [
    [1, 5, 9],
    [14, 20, 21],
    [30, 34, 43],
]
target = 14

print(searchmatrix(arr, target))
