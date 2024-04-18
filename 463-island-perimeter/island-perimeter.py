class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans=0
        length1=len(grid)
        length2=len(grid[0])
        for i in range(length1):
            for j in range(length2):
                if(grid[i][j]==0):
                    continue
                elif(grid[i][j]==1):
                    if(j-1<0 or grid[i][j-1]==0):
                        ans+=1
                    if(i-1<0 or grid[i-1][j]==0):
                        ans+=1
                    if(j+1>length2-1 or grid[i][j+1]==0):
                        ans+=1
                    if(i+1>length1-1 or grid[i+1][j]==0):
                        ans+=1
        return ans