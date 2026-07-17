# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # This helper function will walk down the tree 
        # and count the "good" nodes.
        def count_good_nodes(node, max_so_far):
            # Base Case: If we reach an empty spot, we found 0 good nodes.
            if not node:
                return 0
            
            # 1. Check if the current node is "good"
            if node.val >= max_so_far:
                current_node_score = 1
            else:
                current_node_score = 0
                
            # 2. Update our record high for the path moving forward
            new_max = max(max_so_far, node.val)
            
            # 3. Recursively count the good nodes in the left and right branches
            left_side_count = count_good_nodes(node.left, new_max)
            right_side_count = count_good_nodes(node.right, new_max)
            
            # 4. Sum up our current score and the scores from both branches
            total_good_nodes = current_node_score + left_side_count + right_side_count
            
            return total_good_nodes

        # Start the journey at the root node.
        # Since it's the start, the highest number we've seen so far is the root's value.
        return count_good_nodes(root, root.val)
