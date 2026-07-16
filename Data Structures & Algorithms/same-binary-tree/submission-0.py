# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are None (we've reached the end of both matching branches)
        if not p and not q:
            return True
        
        # Base case 2: One node is None and the other isn't (structural mismatch)
        if not p or not q:
            return False
        
        # If current values match, recursively check the left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        # Values don't match
        return False

