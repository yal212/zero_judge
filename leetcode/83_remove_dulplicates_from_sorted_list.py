# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        now = head
        while now and now.next:
            while now.next and now.val == now.next.val:
                now.next = now.next.next
            now = now.next
        return head
