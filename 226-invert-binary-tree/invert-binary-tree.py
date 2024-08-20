# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)
        def inv(node:Optional[TreeNode]):
            b=0
            c=0
            if(node==None):
                return 1
            if(b==1 or c==1):
                return
            a=TreeNode()

            a=node.left
            node.left=node.right
            node.right=a
            b=inv(node.left)
            c=inv(node.right)
        inv(root)
        return root

        