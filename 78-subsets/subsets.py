class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sol=[]
        length=len(nums)
        def gen(i):
            if(i==length):
                print(sol)
                res.append(sol[:])
                return
            gen(i+1)
            sol.append(nums[i])
            gen(i+1)
            sol.pop()
        gen(0)
        return res