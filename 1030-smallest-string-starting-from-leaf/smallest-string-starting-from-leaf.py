# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def trav(root,ans,temp):
    if(root==None):
        return 0
    if(root.left==root.right==None):
        temp+=chr(root.val+97)
        temp=temp[::-1]
        ans.append(temp)
        return ans
    temp+=chr(root.val+97)  
    trav(root.left,ans,temp)   
    trav(root.right,ans,temp)
    return ans
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        final=trav(root,[],"")
        ans=min(final)
        return ans