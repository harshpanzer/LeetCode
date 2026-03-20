from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        vis={}
        ans=[[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j])==0:
                    q.append([i,j,0])
        while(q):
            i,j,cost=q.popleft()
            if((i,j) not in vis):
                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    a=x+i
                    b=y+j
                    if(a<0 or b<0 or a>=len(mat) or b>=len(mat[0])):
                        continue
                    if(mat[a][b]==1):
                        q.append([a,b,cost+1])
                    else:
                        q.append([a,b,cost])
                ans[i][j]=cost
                vis[(i,j)]=1
        return ans
                
        