# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = temp = ListNode(0)
        extra = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + extra
            if s >= 10:
                s %= 10
                extra = 1
            else:
                extra = 0
            temp.next = ListNode(s)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if extra:
            temp.next = ListNode(1)
        return head.next
