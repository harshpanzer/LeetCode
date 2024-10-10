class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis={}
        ans=0
        length=len(isConnected)
        def sol(i,j):
            if(i==j):
                vis[j]=1
            if(i>length-1 or j>length-1):
                return 0
            if(isConnected[i][j]==1 and i!=j and vis.get(j)==None):
                vis[j]=1
                sol(j,0)
            sol(i,j+1)
            return 0
        for i in range(length):
            if(vis.get(i)==1):
                continue
            sol(i,0)
            ans+=1    
        return ans