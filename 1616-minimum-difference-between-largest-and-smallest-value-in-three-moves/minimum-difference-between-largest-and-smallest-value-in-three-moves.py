class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        temp=0
        nums.sort()
        print(nums)
        length=len(nums)
        ans=984730284092384092384
        i=0
        j=length-4
        if(length<5):
            return 0
        else:
            while(j!=length):
                temp=nums[j]-nums[i]
                if(temp<ans):
                    ans=temp
                temp=0
                i+=1
                j+=1
        return ans