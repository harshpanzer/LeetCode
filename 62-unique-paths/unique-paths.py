class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp={}
        # def sol(i,j):
        #     if(i>m-1 or j>n-1):
        #         return 0
        #     if(i==m-1 and j==n-1):
        #         return 1
        #     if(dp.get((i,j))!=None):
        #         return dp.get((i,j))
        #     a=sol(i+1,j)
        #     b=sol(i,j+1)
        #     dp[(i,j)]=a+b
        #     return a+b
        # return sol(0,0)

        dp=[[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            
            for j in range(n-1,-1,-1):
                if(i==m-1 and j==n-1):
                    continue
                a=-1
                b=-1
                temp=0
                if(i+1<=m-1):
                    a=i+1
                if(j+1<=n-1):
                    b=j+1
                if(a!=-1):
                    temp+=dp[a][j]
                if(b!=-1):
                    temp+=dp[i][b]
                dp[i][j]=temp
                # print(i,j,temp)
        # print(dp)
        return dp[0][0]
