class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(n,dic):
            if(n==1):
                return 1
            if(n==2):
                return 2
            if(n<=0):
                return 0
            if(n in dic):
                return dic.get(n)
            dic[n]=climb(n-1,dic)+climb(n-2,dic)
            return dic.get(n)
        return climb(n,{})
            