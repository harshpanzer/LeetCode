class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        for i in nums:
            for j in range (len(ans)):
                ans+=[[i]+ans[j]]
        return ans
