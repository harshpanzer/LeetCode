class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol=[]
        global add
        add=0
        res=[]
        length=len(candidates)
        def check(i,add):
            if(add==target):
                res.append(sol[:])
                return
            if(add<target and i<length):
                sol.append(candidates[i])
                add+=candidates[i]
                check(i,add)
                sol.pop()
                check(i+1,add-candidates[i])
                
            if(add>target):
                return
        check(0,0)
        return res

