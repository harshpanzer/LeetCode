class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for i in range(n)] for j in range(m)]
        # def sol(i,j):
        #     if(i==m-1 and j==n-1):
        #         return 1
        #     if(i>m-1 or j>n-1):
        #         return 0
        #     if(dp[i][j]!=0):
        #         return dp[i][j]
        #     a=sol(i+1,j)
        #     b=sol(i,j+1)
        #     dp[i][j]=a+b
        #     return dp[i][j]
        # return sol(0,0)

        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(i==m-1 and j==n-1):
                    continue
                a,b=0,0
                if(i<m-1):
                    a=dp[i+1][j]
                if(j<n-1):
                    b=dp[i][j+1]
                dp[i][j]=a+b
        return dp[0][0]