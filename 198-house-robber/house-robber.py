class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
        lst=[-1]*length
        def sol(i):
            if(i==0):
                return nums[i]
            if(i<0):
                return 0
            if(lst[i]!=-1):
                return lst[i]
            a= nums[i]+sol(i-2)
            b= sol(i-1)
            ans=max(a,b)
            lst[i]=ans
            return ans
        return sol(length-1)

            