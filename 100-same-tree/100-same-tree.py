# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: #both nodes are NULL, then same structure so True 
            return True
        
        if not p or not q: #one of the nodes is NULL, then they are not same, so False
            return False
        
        if p.val != q.val: #both nodes are not null, but values are different, so FALSE
            return False
        
        #return True only if both sub-trees are same and identical
        
        return (self.isSameTree(p.left,q.left) and  #checking for left sub-tree
                self.isSameTree(p.right,q.right)) #checking for right sub-tree