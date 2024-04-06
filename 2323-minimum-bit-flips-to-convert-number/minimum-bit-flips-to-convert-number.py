class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        c=start^goal
        c=str(bin(c))[2:]
        count=0
        for i in c:
            if(i=="1"):
                count+=1
        return count