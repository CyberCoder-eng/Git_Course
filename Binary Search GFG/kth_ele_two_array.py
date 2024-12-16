# Brute Froce 

def func(a, b, k):

    res = a + b
    print(res)
    ans = sorted(res)
    print(ans)
    return ans[k - 1]

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(func(a, b, k))


# Optimize solution 