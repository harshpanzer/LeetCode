class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length=len(nums)
        ans=[]
        temp=[]
        for i in range(length-1,-1,-1):
            temp.append([nums[i]])
            l1=len(ans)-1
            print(ans)
            while(l1>-1):
                if(l1==-1):
                    break
                else:
                    tmp=ans[l1][:]
                    tmp.append(nums[i])
                    temp.append(tmp)
                l1-=1
            
            ans=ans+temp
            temp=[]
        ans.append([])
        return ans            
