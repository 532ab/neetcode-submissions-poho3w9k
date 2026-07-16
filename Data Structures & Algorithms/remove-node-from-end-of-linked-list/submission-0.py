class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head  # <--- Note: 'right' starts at 'head', NOT 'dummy'!
        
        # 1. Move right pointer n steps forward
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # 2. Move both together until right hits the very end (None)
        while right:
            left = left.next
            right = right.next
            
        # 3. Delete the node
        left.next = left.next.next
        
        return dummy.next