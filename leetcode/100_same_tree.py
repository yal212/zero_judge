# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        pq = deque()
        pq.append(p)
        qq = deque()
        qq.append(q)

        if p.val !=  q.val:
            return False

        while pq and qq:            
            pnode = pq.popleft()
            qnode = qq.popleft()

            if pnode.left or qnode.left:
                if pnode.left and qnode.left and pnode.left.val == qnode.left.val:
                    pq.append(pnode.left)
                    qq.append(qnode.left)
                else:
                    return False
            
            if pnode.right or qnode.right:
                if pnode.right and qnode.right and pnode.right.val == qnode.right.val:
                    pq.append(pnode.right)
                    qq.append(qnode.right)
                else:
                    return False
        return not pq and not qq