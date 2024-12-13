# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        a=TreeNode(val)
        if(root==None):
            return a
        def sol(node):
            if(val<node.val):
                if(node.left==None):
                    node.left=a
                else:
                    sol(node.left)
            if(val>node.val):
                if(node.right==None):
                    node.right=a
                else:
                    sol(node.right)
            return root
        sol(root)
        return root
            
            
                