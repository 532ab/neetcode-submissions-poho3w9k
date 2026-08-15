# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []

        def backtrack(root):
            if not root:
                return False

            path.append(root.val)

            if not root.left and not root.right:
                result = sum(path) == targetSum
                path.pop()
                return result

            if backtrack(root.left):
                path.pop()
                return True

            if backtrack(root.right):
                path.pop()
                return True

            path.pop()
            return False

        return backtrack(root)
            

            