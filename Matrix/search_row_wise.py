# Time complexcity -> O(n*m)
# Space complexcity -> O(1)


def func(arr, x):
    for num in arr:
        if x in num:
            return True
    return False


arr = [
    [3, 4, 9],
    [2, 5, 6],
    [9, 25, 25],
]
x = 9
print(func(arr, x))
