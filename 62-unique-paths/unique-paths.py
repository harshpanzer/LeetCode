class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for i in range(n)] for j in range(m)]
        def sol(i,j):
            if(i==m-1 and j==n-1):
                return 1
            if(i>m-1 or j>n-1):
                return 0
            if(dp[i][j]!=0):
                return dp[i][j]
            a=sol(i+1,j)
            b=sol(i,j+1)
            dp[i][j]=a+b
            return dp[i][j]
        return sol(0,0)