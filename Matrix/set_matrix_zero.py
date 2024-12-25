# Optimal Approach

# Time Colplexcity -> O(n * m)
# Time Colplexcity -> O(n + m)


def func(mat):
    n = len(mat)
    m = len(mat[0])
    row = [0] * n
    col = [0] * m
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                mat[i][j] = 0
    return mat


mat = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5],
]
print(func(mat))
