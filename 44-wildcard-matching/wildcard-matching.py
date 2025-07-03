class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        def sol(i,j):
            # print(i,j)
            if((i<0 and j<0) or (j==0 and p[j]=="*")):
                return True
            if(i<0 and p[j]=="*"):
                return sol(i,j-1)
            elif(i<0 or j<0):
                return False
            elif(dp.get((i,j))!=None):
                return dp.get((i,j))
            else:
                if(s[i]==p[j]):
                    return sol(i-1,j-1)
                if(p[j]=="?"):
                    return sol(i-1,j-1)
                if(p[j]=="*"):
                    a=sol(i-1,j)
                    b=sol(i-1,j-1)
                    c=sol(i,j-1)
                    dp[(i,j)]=(a or b or c)
                    return (a or b or c)
                else:
                    return False
            
        return sol(len(s)-1,len(p)-1)