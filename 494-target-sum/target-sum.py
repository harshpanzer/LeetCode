class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length=len(nums)
        dic={}
        def sol(i,temp):
            if(i==length-1):
                if((temp-nums[i])==target and (temp+nums[i])==target):
                    return 2
                elif((temp-nums[i])==target or (temp+nums[i])==target):
                    return 1
                else:
                    return 0
            if(dic.get((i,temp))!=None):
                return dic.get((i,temp))
            a=sol(i+1,temp+nums[i])
            b=sol(i+1,temp-nums[i])
            dic[(i,temp)]=(a+b)
            return a+b
        return sol(0,0)