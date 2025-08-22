# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        
        left = root.left
        right = root.right
        if left.val != right.val:
            return False

        lq = deque()
        lq.append(left)
        rq = deque()
        rq.append(right)

        while lq and rq:
            lnode = lq.popleft()
            rnode = rq.popleft()

            if lnode.left or rnode.right:
                if lnode.left and rnode.right and lnode.left.val == rnode.right.val:
                    lq.append(lnode.left)
                    rq.append(rnode.right)
                else:
                    return False
            
            if lnode.right or rnode.left:
                if lnode.right and rnode.left and lnode.right.val == rnode.left.val:
                    lq.append(lnode.right)
                    rq.append(rnode.left)
                else:
                    return False
        return not lq and not rq
