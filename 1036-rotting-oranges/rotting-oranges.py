class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[]
        ct=0
        
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):
                    vis.append([i,j,0])
                if(grid[i][j]==1):
                    ct+=1
        ans=0
        fl=0
        while(len(vis)>0):
            i,j,fl=vis[0]
            # print(i,j,fl)
            print(vis)
            vb=vis.pop(0)
            for a,b in [(1,0),(0,1),(-1,0),(0,-1)]:
                i+=a
                j+=b
                if(i>=0 and j>=0 and i<m and j<n and grid[i][j]==1):
                    
                    grid[i][j]=2
                    vis.append([i,j,fl+1])
                    ans=max(ans,fl+1)
                    ct-=1
                i-=a
                j-=b
        if(ct==0):
            return ans
        return -1        
                