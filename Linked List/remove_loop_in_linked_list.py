# Optimal Code


# head = 1 -> 3 -> 4, pos = 2
# Output: true

# head = 1 -> 8 -> 3 -> 4, pos = 0
# Output: true

# Time complexity -> O(N)
# Space complexity -> O(1)


def removeLoop(self, head):
    if not head:
        return
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            while fast.next != slow:
                fast = fast.next
            fast.next = None
    return
