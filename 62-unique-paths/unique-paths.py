class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        def sol(i,j):
            if(i>m-1 or j>n-1):
                return 0
            if(i==m-1 and j==n-1):
                return 1
            if(dp.get((i,j))!=None):
                return dp.get((i,j))
            a=sol(i+1,j)
            b=sol(i,j+1)
            dp[(i,j)]=a+b
            return a+b
        return sol(0,0)