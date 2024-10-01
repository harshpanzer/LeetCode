class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # coins.sort(reverse=True)
        length=len(coins)
        dic={}
        ff={}
        def sol(i,amt,ans):
            # print(ans)
            
            if(dic.get((i,amt))!=None):
                return dic.get((i,amt))
            if(i==length-1):
                if(amt%coins[i]==0):
                    
                    print(amt/coins[i],coins[i])
                    return ans+1
                else:
                    return ans
            if(amt==0):
                return ans+1
            a=0
            c=0+sol(i+1,amt,ans)
            if(amt>=coins[i]):

                a=sol(i,amt-coins[i],ans)
            # print(a,c,amt)
            dic[(i,amt)]=a+c
            return a+c
        a=sol(0,amount,0)
        if(a!=0):
            return a
        return 0