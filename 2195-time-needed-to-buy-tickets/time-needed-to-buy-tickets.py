class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        a=tickets[k]
        length=len(tickets)
        ans=0
        for i in range(length):
            if(tickets[i]<=a and i<k):
                ans+=tickets[i]
                continue
            elif(i>k and tickets[i]>=a):
                tickets[i]=a-1
                ans+=tickets[i]
            elif(tickets[i]>a and i<k):
                tickets[i]=a
                ans+=tickets[i]
            else:
                ans+=tickets[i]
            
        # for i in range(length):
        #     ans+=tickets[i]
        return ans
