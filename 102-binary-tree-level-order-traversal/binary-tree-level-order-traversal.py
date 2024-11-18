# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[root]
        ans=[]
        
        if(q[0]==None):
            return []
        
        while(len(q)!=0):
            temp=[]
            leng=len(q)
            for i in range(leng):
                a=q.pop(0)
                temp.append(a.val)
                if(a.left!=None):
                    q.append(a.left)
                if(a.right!=None):
                    q.append(a.right)
            ans.append(temp)    
            
        return ans
        