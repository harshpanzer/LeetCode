class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        dp=[[float('inf') for i in range(n)] for i in range(n)]
        def sol(i,j):
            if(i>n-1 or j>n-1 or i<0 or j<0):
                return float('inf')
            if(i==n-1):
                dp[i][j]=matrix[i][j]
                return matrix[i][j]
            if(dp[i][j]!=float('inf')):
                return dp[i][j]
            a=matrix[i][j]+sol(i+1,j-1)
            b=matrix[i][j]+sol(i+1,j)
            c=matrix[i][j]+sol(i+1,j+1)
            dp[i][j]=min(a,b,c)
            return dp[i][j]
        for i in range(n):
            sol(0,i)
        return min(dp[0])
    