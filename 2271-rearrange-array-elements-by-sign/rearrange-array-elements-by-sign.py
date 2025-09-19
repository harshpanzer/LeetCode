class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lent=len(nums)
        a=0
        b=0
        ans=[]
        flag=0
        for i in nums:
            if(flag==0):
                while(nums[a]<0):
                    a+=1
                ans.append(nums[a])
                a+=1
                flag=1
                continue
            elif(flag==1):
                while(nums[b]>0):
                    b+=1
                ans.append(nums[b])
                b+=1
                flag=0
                continue
            
        return ans



