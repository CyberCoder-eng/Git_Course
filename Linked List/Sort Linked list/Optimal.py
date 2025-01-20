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
