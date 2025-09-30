class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt=len(prices)
        minn=prices[0]
        ans=0
        for i in prices:
            if(minn<=i):
                ans=max(i-minn,ans)
            else:
                minn=min(minn,i)
        return ans

            








