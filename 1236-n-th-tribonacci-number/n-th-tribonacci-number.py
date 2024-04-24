
class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def check(n):
            if n in memo:
                return memo[n]
            if(n<0):
                return 0
            elif(n==1):
                return 1
            elif(n==0):
                return 0
            else:
                total= check(n-3)+check(n-2)+check(n-1) 
                memo[n]=total
                return total
        return check(n)