class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        length=len(nums)
        for i in range(length):
            dic[nums[i]]=dic.get(nums[i],0)+1
        # a=dic.items()
        a=sorted(dic.items(), key=lambda item: item[1], reverse=True)
        ans=[]
        for i in a:
            if(k==0):
                break
            else:
                ans.append(i[0])
                k-=1
        return ans

