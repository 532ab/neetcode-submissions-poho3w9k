class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)

        if not root:
            return True

        left_height = height(root.left)
        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        if not self.isBalanced(root.left):
            return False

        if not self.isBalanced(root.right):
            return False

        return True
