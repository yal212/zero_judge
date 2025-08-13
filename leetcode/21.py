# 0ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if not h1:
            return h2
        if not h2:
            return h1
        if h2.val < h1.val:
            h1, h2 = h2, h1
        head = h1
        while h1.next and h2:
            if h1.next.val >= h2.val:
                temp = h1.next
                h1.next = h2
                h2 = h2.next
                h1.next.next = temp
            h1 = h1.next
        if not h1.next:
            h1.next = h2
        return head


# usual way
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Append remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next


# recursive version
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
