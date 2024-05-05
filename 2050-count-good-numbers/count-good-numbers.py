class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=1000000007
        def count(x,num):
            if(num==0):
                return 1
            elif(num%2==0):
                # even=n//2
                # even=5**even
                # odd=n//2
                # odd=4**odd
                # ans=even*odd
                return count((x*x)%mod,num//2)
            else:
                # even=(n//2)+1
                # even=5**even
                # odd=(n//2)
                # odd=4**odd
                return x*count((x*x)%mod,(num-1)//2)
        odd = n//2
        even = n//2 + n%2
        return (count(5,even)%mod * count(4,odd)%mod)%mod
        