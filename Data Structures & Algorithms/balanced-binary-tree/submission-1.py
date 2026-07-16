class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0  # Base case: Height of None is 0
            
            # 1. Ask left and right children for their heights
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 2. If left is unbalanced (-1), right is unbalanced (-1),
            #    or they differ by more than 1, this whole tree is unbalanced (-1)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            # 3. Otherwise, return the actual height of this node
            return 1 + max(left, right)
            
        return dfs(root) != -1





