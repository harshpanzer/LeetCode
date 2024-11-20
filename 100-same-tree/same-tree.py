# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        am=[]
        bm=[]
        def sol1(node):
            if(node==None):
                am.append(None)
                return 
            a=sol1(node.left)
            b=sol1(node.right)
            am.append(node.val)
            return
        def sol2(node):
            if(node==None):
                bm.append(None)
                return 
            a=sol2(node.left)
            b=sol2(node.right)
            bm.append(node.val)
            return
        
        sol1(p)
        sol2(q)
        print(am,bm)
        if(am==bm):
            return True
        return False