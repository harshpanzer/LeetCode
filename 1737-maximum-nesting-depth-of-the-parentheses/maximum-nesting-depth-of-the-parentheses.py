class Solution:
    def maxDepth(self, s: str) -> int:
        length=len(s)
        count=0
        ans=0
        for i in s:
            if(i=="("):
                count+=1
            elif(i==")"):
                count-=1
            if(count>ans):
                ans=count
        return ans

            