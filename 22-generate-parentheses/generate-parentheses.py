class Solution(object):
    def generateParenthesis(self, n):
        # def backtrack(S='', left=0, right=0):
        #     if len(S) == 2 * n:
        #         result.append(S)
        #         return
        #     if left < n:
        #         backtrack(S + '(', left + 1, right)
        #     if right < left:
        #         backtrack(S + ')', left, right + 1)
        #     print(S)
        # result = []
        # backtrack()
        # return result
        ans=[]
        def backtrack(st="",left=0,right=0):

            if(len(st)==2*n):
                ans.append(st)
                return
            if(left<n):
                backtrack(st+"(",left+1,right)
            if(right<left):
                backtrack(st+")",left,right+1)
        backtrack()
        return ans