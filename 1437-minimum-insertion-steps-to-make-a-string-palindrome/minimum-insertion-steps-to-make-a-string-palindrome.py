class Solution:
    def minInsertions(self, s: str) -> int:
        length=len(s)
        dic={}
        rev=s[::-1]
        def sol(i,j):
            # print(i,j)
            if(dic.get((i,j))!=None):
                return dic.get((i,j))
            if(i<0 or j<0):
                return 0
            if(s[i]==rev[j]):
                temp=1+sol(i-1,j-1)
                return temp


            a=max(sol(i-1,j),sol(i,j-1))
            dic[(i,j)]=a
            return a
            
        a=sol(length-1,length-1)
        ans=length-a
        return ans