# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root==None):
            return True
        check=[0,0]
        def sol(node,ct):
            print(check)
            if(node==None):
                return ct
            a=sol(node.left,ct+1)
            b=sol(node.right,ct+1)
            if(abs(a-b)>1):
                check[0]=1
            return max(a,b)
        sol(root,0)
        if(check[0]==1):
            return False
        else:
            return True