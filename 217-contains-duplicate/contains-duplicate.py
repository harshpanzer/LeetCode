class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in range(len(nums)):
            if(dic.get(nums[i])==1):
                return True
            else:
                dic[nums[i]]=1
        return False