class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1=len(word1)
        length2=len(word2)
        dic={}
        def sol(i,j):
            if(i<0 or j<0):
                return 0
            if(dic.get((i,j))!=None):
                return dic.get((i,j))
            if(word1[i]==word2[j]):
                a=1+sol(i-1,j-1)
                dic[(i,j)]=a
                return a
            ans=max(sol(i-1,j),sol(i,j-1))
            dic[(i,j)]=ans
            return ans
        a=sol(length1-1,length2-1)
        ans=(length1-a)+(length2-a)
        return ans
