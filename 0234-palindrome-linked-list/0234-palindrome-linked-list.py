# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #Two - pointer
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        # slow is at middle node, so reverse the nodes from slow till end
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        #now we have two linked lists, with prev pointing to first node after middle
        left, right = head, prev
        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True