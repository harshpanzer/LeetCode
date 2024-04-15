# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
summ=0

def trav(node,temp,summ):
    temp=temp+str(node.val)
    if(node.left):
       summ= trav(node.left,temp,summ)
    if(node.right):
        summ= trav(node.right,temp,summ)
    if(node.left==node.right==None):
        summ+=int(temp)
        return summ
    return summ

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        temp=""
        summ=0
        ans=trav(root,temp,summ)
        return ans
        