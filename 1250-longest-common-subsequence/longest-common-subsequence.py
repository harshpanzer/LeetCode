class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1=len(text1)
        length2=len(text2)
        dic={}

        def sol(i,j):
            if(i<0 or j<0):
                return 0
            if(text1[i]==text2[j]):
                dic[(i,j)]=1 + sol(i-1,j-1)
                return dic[(i,j)]
            if(dic.get((i,j))!=None):
                return dic.get((i,j))
            else:
                dic[(i,j)]= 0+max(sol(i-1,j),sol(i,j-1))
                return dic[(i,j)]
        return sol(length1-1,length2-1)
                

