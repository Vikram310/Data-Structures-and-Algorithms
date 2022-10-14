# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #create another function for recursively using it on left and right subtree
        def dfs(root):
            #returns two pointers, one to show whether balanced and other is length
            if not root:return [True,0] #if root is null, it is balanced and length = 0
            
            #apply the same function on left and right childs
            left,right = dfs(root.left),dfs(root.right)
            # tree is balanced only if left and right is balanced and also abs differences between 
            # lengths of left and right shoudl be <= 1
            is_balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1
            
            return [is_balanced,1+max(left[1],right[1])] #return whether tree is balanced and also length
        
        return dfs(root)[0]