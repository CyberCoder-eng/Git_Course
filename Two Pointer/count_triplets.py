# Optimal Code


def countTriplets(arr, target):
    # code here
    n = len(arr)
    ans = 0
    for i in range(n - 2):
        l, h = i + 1, n - 1
        val = target - arr[i]
        while l < h:
            curr = arr[l] + arr[h]
            if curr == val:
                if arr[l] == arr[h]:
                    ans += ((h - l) * (h - l + 1)) // 2
                    break
                else:
                    temp1, temp2 = 1, 1
                    while l < h and arr[l] == arr[l + 1]:
                        temp1 += 1
                        l += 1
                    l += 1
                    while l < h and arr[h] == arr[h - 1]:
                        temp2 += 1
                        h -= 1
                    h -= 1
                    ans += temp1 * temp2
            elif curr > val:
                h -= 1
            else:
                l += 1
    return ans


arr = [-3, -1, -1, 0, 1, 2]
target = -2
print(countTriplets(arr, target))