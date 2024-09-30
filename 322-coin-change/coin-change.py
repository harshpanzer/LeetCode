class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort(reverse=True)
        length=len(coins)
        dic={}
        def sol(i,amt,ans):
            # print(ans)
            
            if(dic.get((i,amt))!=None):
                return dic.get((i,amt))
            if(i==length-1):
                if(amt%coins[i]==0):
                    # print(amt/coins[i],coins[i])
                    return amt//coins[i]
                else:
                    return 283947983248238
            if(amt==0):
                return 0
            a=float('inf')
            c=0+sol(i+1,amt,ans)
            if(amt>=coins[i]):

                a=1+sol(i,amt-coins[i],ans)
            # print(a,c)
            dic[(i,amt)]=min(a,c)
            return dic[(i,amt)]
        a=sol(0,amount,0)
        if(a!=283947983248238):
            return a
        return -1