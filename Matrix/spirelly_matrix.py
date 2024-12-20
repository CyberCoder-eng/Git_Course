# Optimize Approach


def func(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = (list(zip(*matrix)))[::-1]
    return res


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(func(arr))
