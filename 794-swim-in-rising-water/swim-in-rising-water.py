import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        lt=len(grid)
        lst=[]
        heapq.heappush(lst,[grid[0][0],0,0])
        ans=0
        vis=[[0 for i in range(lt)] for j in range(lt)]
        while(lst):
            num,i,j=heapq.heappop(lst)
            print(num)
            ans=max(ans,num)
            if(i==lt-1 and j==lt-1):
                
                return ans
            else:
                for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
                    a=x+i
                    b=y+j
                    if(a>-1 and b>-1 and a<lt and b<lt and vis[a][b]!=1):
                        ans=max(ans,num)
                        vis[a][b]=1
                        heapq.heappush(lst,[grid[a][b],a,b])
        

        