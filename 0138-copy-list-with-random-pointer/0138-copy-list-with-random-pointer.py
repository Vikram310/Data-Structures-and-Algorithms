"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldTonew = {None:None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldTonew[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldTonew[cur]
            copy.next = oldTonew[cur.next]
            copy.random = oldTonew[cur.random]
            cur = cur.next
        
        return oldTonew[head]