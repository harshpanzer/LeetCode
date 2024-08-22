# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rec(node,count,temp):
            if(node==None):
                return [0,0]
            n=rec(node.left,count,temp)
            m=rec(node.right,count,temp)

            temp=max(n[1],m[1])
            temp=max(temp,n[0]+m[0])
            c=max(n[0],m[0])+1
            print(node.val,temp)
            return [c,temp]
        # def recRight(node,count):
        #     if(node==None):
        #         return
        #     recRight(node.right,count+1)
        #     return count
        a=rec(root.left,0,0)
        b=rec(root.right,0,0)
        
        return max(a[0]+b[0],a[1],b[1]) 

        