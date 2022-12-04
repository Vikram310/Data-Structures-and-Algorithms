# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        s = set()
        
        while cur and cur.next:
            if cur in s:
                return True
            else:
                s.add(cur)
            cur = cur.next