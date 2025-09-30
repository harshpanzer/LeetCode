class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt=len(prices)
        dp={}
        def sol(i,buy):
            a,b,c,d=0,0,0,0
            if(i==lt):
                return 0
            if(dp.get((i,buy))!=None):
                return dp.get((i,buy))
            if(buy):
                a=sol(i+1,False)-prices[i]
                b=sol(i+1,True)
            else:
                c=sol(i+1,True)+prices[i]
                d=sol(i+1,False)
            dp[(i,buy)]=max(a,b,c,d)
            return max(a,b,c,d)
        return sol(0,True)
        