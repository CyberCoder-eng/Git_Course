# Optimal Code

# Time Complexity -> O(N)
# Space Complexity -> O(1)


def rotate(self, head, k):
    temp = head
    count = 1
    while temp.next:
        count += 1
        temp = temp.next
    k %= count
    temp.next = head
    while k:
        temp = temp.next
        k -= 1
    new_head = temp.next
    temp.next = None
    return new_head
