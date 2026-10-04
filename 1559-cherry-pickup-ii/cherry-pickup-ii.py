class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        lt1=len(grid)
        lt2=len(grid[0])
        dic={}
        def sol(i1,j1,j2):
            
            if(i1>lt1-1 or j1<0 or j2<0 or j1>lt2-1 or j2>lt2-1):
                return float('-inf')
            if(i1==lt1-1):
                if(j1==j2):
                    return grid[i1][j1]
                return grid[i1][j1]+grid[i1][j2]
            if(dic.get((i1,j1,j2))!=None):
                return dic.get((i1,j1,j2))
            a=sol(i1+1,j1-1,j2-1)
            b=sol(i1+1,j1-1,j2)
            c=sol(i1+1,j1-1,j2+1)
            d=sol(i1+1,j1,j2-1)
            e=sol(i1+1,j1,j2)
            f=sol(i1+1,j1,j2+1)
            g=sol(i1+1,j1+1,j2-1)
            h=sol(i1+1,j1+1,j2)
            i=sol(i1+1,j1+1,j2+1)
            ans=max(a,b,c,d,e,f,g,h,i)
            if(j1==j2):
                dic[(i1,j1,j2)]=ans+grid[i1][j1]
                return ans+grid[i1][j1]
            else:
                dic[(i1,j1,j2)]=ans+grid[i1][j1]+grid[i1][j2]
                return ans+grid[i1][j1]+grid[i1][j2]
        return sol(0,0,lt2-1)
            