class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp={}
        def sol(i,buy,count):
            if(len(prices)==i):
                return 0
            if(count==0):
                return 0
            if(dp.get((i,buy,count))!=None):
                return dp.get((i,buy,count))
            a,b=0,0
            if(buy):
                a=-prices[i]+sol(i+1,0,count)
                b=sol(i+1,1,count)
            elif(buy==0):
                a=prices[i]+sol(i+1,1,count-1)
                b=sol(i+1,0,count)
            dp[(i,buy,count)]=max(a,b)
            print(max(a,b))
            return max(a,b)
        return sol(0,1,k)
