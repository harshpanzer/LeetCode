# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def trav(node,count,val,depth):
    if not node:
        return node
    if(depth==1):
        temp=TreeNode()
        temp.val=val
        temp.left=node
        return temp
    elif(count==depth-1):
        l=node.left
        node.left=TreeNode(val,l,None)
        r=node.right
        node.right=TreeNode(val,None,r)
        return node

    trav(node.left,count+1,val,depth)
    trav(node.right,count+1,val,depth)
    return node
        


        
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return trav(root,1,val,depth)