## Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None

        rabbit, tortoise = head.next.next, head

        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next

        tortoise.next = tortoise.next.next
        return head