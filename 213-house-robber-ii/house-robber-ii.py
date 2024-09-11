class Solution:
    def rob(self, nums: List[int]) -> int:
        length=len(nums)
        lst=[-1]*length
        if(length==1):
            return nums[0]
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
        ans1=sol(length-2)
        nums.pop(0)
        length=length-1
        lst=[-1]*length
        ans2=sol(length-1)
        print(length)
        return max(ans1,ans2)