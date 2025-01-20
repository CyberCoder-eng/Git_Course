"""
Time complexity -> O(N) + O(NlogN) + O(N)
Space complexity -> O(1)
"""


def sortLinked(head):
    temp = head
    res = []

    while temp:
        res.append(temp.val)
        temp = temp.next

    res.sort()
    current_head = head
    index = 0
    while current_head:
        current_head.val = res[index]
        index += 1
        current_head = current_head.next
    return head
