"""
Time complexity ->  O(N)
Space complexity -> O(1)
"""


def mergeLinked(head1, head2):
    temp = Node = ListNode()
    while head1 and head2:
        if head1.val < head2.val:
            Node.next = head1
            head1 = head1.next
        else:
            Node.next = head2
            head2 = head2.next
        Node = Node.next
    Node.next = head1 or head2
    return temp.next


# Second solution
def sortedMerge(self, head1, head2):
    temp1 = head1
    temp2 = head2
    res = Node(-1)
    ans = res

    while temp1 != None and temp2 != None:
        if temp1.data < temp2.data:
            res.next = temp1
            res = res.next
            temp1 = temp1.next
        else:
            res.next = temp2
            res = res.next
            temp2 = temp2.next
    if temp1 is None:
        res.next = temp2
    if temp2 is None:
        res.next = temp1
    return ans.next
