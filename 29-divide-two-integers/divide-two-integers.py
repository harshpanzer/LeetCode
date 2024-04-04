class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div=abs(divisor)
        d=abs(dividend)
        count=0
        temp=div
        while(d>=div):
            m=1
            temp=div
            while(d>=temp):
                count+=m
                m+=m
                d-=temp
                temp+=temp
        if((dividend<0 and divisor>=0) or (dividend>0 and divisor<=0)):
            count=0-count
        return min(2147483647,max(count,-2147483648))

        
