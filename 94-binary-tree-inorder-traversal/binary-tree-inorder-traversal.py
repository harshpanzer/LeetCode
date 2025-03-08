# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        def sol(node):
            if(node==None):
                return
            a=sol(node.left)
            lst.append(node.val)
            b=sol(node.right)
            return
        sol(root)
        return lst


            
            