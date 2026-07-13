# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        
        while current:
            # If this exact node object is already in our set, we hit a loop!
            if current in visited:
                return True
            
            # Otherwise, log it and move forward
            visited.add(current)
            current = current.next
            
        return False  # If we hit None, there is no cycle

