class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt=len(prices)
        minn=prices[0]
        ans=0
        for i in range(1,lt):
            if(prices[i]>minn):
                ans=max(ans,prices[i]-minn)
            minn=min(prices[i],minn)
        return ans