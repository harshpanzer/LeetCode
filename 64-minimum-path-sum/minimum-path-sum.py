class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        length1=len(grid)
        length2=len(grid[0])
        ans={}
        an=[]
        def sol(v,h,temp):
            if(v>=length1 or h>=length2):
                return float('inf')
            if(ans.get((v,h))!=None):
                return ans.get((v,h)) + temp
            if(v==(length1-1) and h==(length2-1)):
                temp+=grid[v][h]
                an.append(temp)
                return temp
            a=sol(v+1,h,temp+grid[v][h])
            b=sol(v,h+1,temp+grid[v][h])
            te=min(a,b)
            ans[(v,h)]=te-temp
            return te
        a= sol(0,0,0)

        return a
