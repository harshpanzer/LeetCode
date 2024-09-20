class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length1=len(matrix)
        length2=len(matrix[0])
        dic={}
        def sol(row,col,temp):
            if(row<0 or row>(length2-1)):
                return float('inf')
            if(col==length1-1):
                return temp+matrix[col][row]
            if(dic.get((col,row))!=None):
                return dic.get((col,row))+temp
            a=sol(row-1,col+1,temp+matrix[col][row])
            b=sol(row,col+1,temp+matrix[col][row])
            c=sol(row+1,col+1,temp+matrix[col][row])
            ans=min(a,b,c)
            dic[(col,row)]=ans-temp
            return ans
        ans=[]
        for i in range(length2):
            temp=sol(i,0,0)
            print(temp)
            ans.append(temp)
        return min(ans)