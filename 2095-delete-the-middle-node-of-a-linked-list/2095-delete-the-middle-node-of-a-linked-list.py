# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # checking if it is a single node
        if not head.next:
            return None
        
        #initialise two pointers tortoise and rabbit (slow,fast) to head(start) of linked list
        tortoise,rabbit = head,head
        #initialise one more pointer prev, which is just before tortoise
        prev = None
        
        # iterate till the last node
        while rabbit and rabbit.next:
            prev = tortoise #prev moves one step ahead and points to tortoise node
            tortoise = tortoise.next #tortoise takes one step fwd
            rabbit = rabbit.next.next #rabbit takes two steps fwd
        '''    
        when rabbit is at last position, tortoise will be at exact middle poisition, and prev will 
        before tortoise, as we need to remove the middle node, just point tortoise next to 
        prev next
        '''
        prev.next = tortoise.next
        
        return head