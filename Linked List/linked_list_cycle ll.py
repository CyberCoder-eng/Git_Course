# head = 1->3->2->4->5
# output: 3

# Optimal Code
# Time complexity -> O(N)
# Space complexity -> O(1)


def findFirstNode(self, head):
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
            return slow
    return None
