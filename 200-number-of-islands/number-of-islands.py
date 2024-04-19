
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        length1=len(grid)
        length2=len(grid[0])
        def check(grid,i,j):
            if i < 0 or j < 0 or i >= length1 or j >= length2:
                return 0
            if(grid[i][j])=="0":
                return 0
            if(grid[i][j])=="1":
                grid[i][j]="2"
                check(grid,i,j+1)
                check(grid,i+1,j)
                check(grid,i-1,j)
                check(grid,i,j-1)
            if((grid[i][j])=="2"):
                return 0
        for i in range(length1):
            for j in range(length2):
                if(grid[i][j])=="1":
                    ans+=1
                    check(grid,i,j)
        return ans