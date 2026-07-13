# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # Global tracker for our record
        
        def dfs(node):
            if not node:
                return 0
            
            # 1. Get the depth of both children (Bottom-Up)
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # 2. Update our record if the path through THIS node is the longest seen so far
            current_diameter = left_depth + right_depth
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # 3. Return the depth of this node to ITS parent (standard max depth logic)
            return max(left_depth, right_depth) + 1
            
        dfs(root)
        return self.max_diameter