from collections import deque 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        q=deque()
        q.append((sr,sc))
        a=sr
        b=sc
        c=0
        d=0
        vis={}
        # vis[(a,b)]=1
        while(q):
            a,b=q.popleft()
            if(vis.get((a,b))==1):
                continue
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                
                c=a+i
                d=b+j
                if(0<=c<m and 0<=d<n and image[c][d]==image[a][b]):
                    
                    q.append((c,d))
            vis[a,b]=1
            image[a][b]=color
        return image