class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp={}
        def sol(i,buy):
            if(i>=len(prices)):
                return 0
            a,b=0,0
            if(dp.get((i,buy))!=None):
                return dp.get((i,buy))
            if(buy):
                a=-prices[i]+sol(i+1,0)
                b=sol(i+1,1)
            else:
                a=prices[i]+sol(i+1,1)-fee
                b=sol(i+1,0)
            dp[(i,buy)]=max(a,b)
            return max(a,b)
        return sol(0,1)   
