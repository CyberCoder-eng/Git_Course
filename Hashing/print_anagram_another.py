def anagram(arr):
    hash_map = dict()
    for char in range(len(arr)):
        word = " ".join(sorted(arr[char]))
        if word not in hash_map:
            hash_map[word] = []
        hash_map[word].append(arr[char])
    return [x for x in hash_map.values()]


arr = ["act", "god", "cat", "dog", "tac"]
print(anagram(arr))
