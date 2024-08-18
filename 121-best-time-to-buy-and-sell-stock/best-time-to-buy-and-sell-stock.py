class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        i=0
        j=0
        ans=0

        while(j<length):
            temp=prices[i]
            if(prices[j]<prices[i]):
                i=j
            elif(prices[j]>prices[i]):
                ans=max(ans,prices[j]-prices[i])
            j+=1
        return ans

