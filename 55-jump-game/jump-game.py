class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count=0
        length=len(nums)
        if(nums[0]==0 and length==1):
            return True
        ptr=0
        for i in nums:
            ptr+=1
            if(count<i):
                count=i
            if(count>=length-ptr):
                return True
            if(count==0):
                return False
            count-=1
            
        