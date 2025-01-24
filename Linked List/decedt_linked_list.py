# Optimal Code


# Time complexity -> O(N)
# Space complexity -> O(1)


# Input: head: 1 -> 3 -> 4, pos = 2
# Output: true

# Input: head: 1 -> 8 -> 3 -> 4, pos = 0
# Output: false


def detectLoop(self, head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
