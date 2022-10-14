# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None
        
        tortoise,rabbit = head,head
        prev = None
        
        while rabbit and rabbit.next:
            prev = tortoise
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            
        
        prev.next = tortoise.next
        
        return head