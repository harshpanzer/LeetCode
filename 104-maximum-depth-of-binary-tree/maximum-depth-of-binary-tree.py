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
        def sol(node,ans):
            if(node==None):
                return ans
            a=sol(node.left,ans+1)
            b=sol(node.right,ans+1)
            return max(a,b)
        return sol(root,0)