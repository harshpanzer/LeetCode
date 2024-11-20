# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def sol(node,temp):
            if(node==None):
                return temp
            aa=sol(node.left,temp)
            bb=sol(node.right,temp)
            # aa=a.val
            # bb=b.val
            if(aa<0):
                aa=0
            if(bb<0):
                bb=0
            ans.append((aa+bb+node.val))
            temp+=max(aa,bb)+node.val
            return temp
        sol(root,0)
        return max(ans)