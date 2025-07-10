class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt=len(prices)
        dp={}
        def sol(i,buy):
            a,b,c=0,0,0
            if(i>lt-1):
                return 0
            if(dp.get((i,buy))!=None):
                return dp.get((i,buy))
            if(buy):
                a=-prices[i]+sol(i+1,0)
                b=sol(i+1,1)
            else:
                a=prices[i]+sol(i+1,1)
                b=sol(i+1,0)
            dp[(i,buy)]=max(a,b)
            return max(a,b)
        return sol(0,1)

        lt=len(prices)
        