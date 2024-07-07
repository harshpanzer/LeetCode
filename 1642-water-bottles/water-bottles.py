class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        emp=numBottles
        temp=0
        rem=0
        while(emp>=numExchange):
            temp=emp//numExchange
            rem=emp%numExchange
            ans+=temp
            emp+=rem+temp-emp
        return ans
