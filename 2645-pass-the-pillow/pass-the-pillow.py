class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if(time<n):
            return time+1
        a=time%(n-1)
        b=time//(n-1)

        print(b)
        if(a==0):
            if(b%2==0):
                return 1
            else:
                return n
        
        else:
            if(b%2==0):
                
                return a+1
            else:
                return n-a