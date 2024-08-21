# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if(root==None):
            return 0
        def rec(node,count):
            if(node==None):
                return count
            count+=1
            print(count)
            return max(rec(node.left,count),rec(node.right,count))
        return rec(root,0)
            
            
        
        

        


        
        

        