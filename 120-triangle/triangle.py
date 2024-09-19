class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length=len(triangle)
        dic={}
        def sol(row,col,temp):
            if(col==length-1):
                return temp+triangle[col][row]
            if(dic.get((col,row))!=None):
                return dic.get((col,row))+temp
            a=sol(row,col+1,temp+triangle[col][row])
            b=sol(row+1,col+1,temp+triangle[col][row])
            ans=min(a,b)
            dic[(col,row)]=ans-temp
            return ans
        a= sol(0,0,0)
        print(dic)
        return a
