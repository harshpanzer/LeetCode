class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=[0]
        dp={}
        def sol(i,buy,count):
            if(i==len(prices)):
                return 0
            if(count>1):
                return 0
            curr_price=prices[i]
            a,b,c,d=0,0,0,0
            if(dp.get((i,buy,count))!=None):
                return dp.get((i,buy,count))
            if(buy):

                a=-curr_price+sol(i+1,0,count)
                b=sol(i+1,1,count)
            elif(buy==0):
                c=curr_price+sol(i+1,1,count+1)
                d=sol(i+1,0,count)
            dp[(i,buy,count)]=max(a,b,c,d)
            # print(max(a,b,c))
            return max(a,b,c,d)
        return sol(0,1,0)