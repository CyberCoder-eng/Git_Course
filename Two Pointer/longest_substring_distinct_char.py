# Brute Force


def uniqueChar(s):
    return len(set(s))


s = "geeksforgeeks"
print(uniqueChar(s))


# Better Code

# Time Complexity -> O(N^2)
# Space Complexity -> O(1)


def func(s):
    res = ""
    count = 0
    for char in s:
        if char not in res:
            res += char
            count = max(len(res), count)
        else:
            res = res[res.index(char) + 1 :] + char
    return count


s = "geeksforgeeks"
print(func(s))


# Optimal Code
# Time complexity -> O(N)
# Space complexity -> O(N)
def longestUniquechar(s):
    hash_map = dict()
    count = 0
    res = 0
    for char in range(len(s)):
        hash_map[s[char]] = hash_map.get(s[char], 0) + 1
        while hash_map[s[char]] > 1:
            hash_map[s[count]] = hash_map.get(s[count], 0) - 1
            count += 1
        res = max(res, char - count + 1)
    return res


s = "geeksforgeeks"
print(longestUniquechar(s))
