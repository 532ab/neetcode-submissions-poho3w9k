# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            if not node:
                return None
            
            queue = deque([node])
            while queue:
                current = queue.popleft()
                
                # Swap children properly
                current.left, current.right = current.right, current.left
                
                # Add children to queue if they exist
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            return node
        
        return bfs(root)
            
