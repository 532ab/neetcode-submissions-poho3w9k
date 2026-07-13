# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to anchor the start
        dummy = ListNode(0)
        current = dummy
        
        # 2. Your while loop logic, fixed for linked lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1  # Link the smaller node
                list1 = list1.next    # Move list1 pointer forward
            else:
                current.next = list2
                list2 = list2.next    # Move list2 pointer forward
                
            current = current.next    # Move our main building pointer forward
            
        # 3. Clean up the leftovers
        # If one list runs out, just attach the remainder of the other list
        current.next = list1 if list1 else list2
        
        # 4. Return the head of the real merged list (skipping the dummy)
        return dummy.next