# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # Step 1: Dump all nodes into a standard Python array
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
            
        # Step 2: Use two pointers (Left and Right) to weave them together
        left = 0
        right = len(nodes) - 1
        
        while left < right:
            # Connect the left node's next to the right node
            nodes[left].next = nodes[right]
            left += 1
            
            # If the pointers met, we are done!
            if left == right:
                break
                
            # Connect the right node's next to the next left node
            nodes[right].next = nodes[left]
            right -= 1
            
        # Step 3: Crucial clean up! 
        # The last node in our reordered list must point to None, 
        # otherwise we create an infinite loop cycle.
        nodes[left].next = None
