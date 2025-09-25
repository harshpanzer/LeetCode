class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def sol(i,j,k):
            mid=(j+i)//2
            if(i==j+1):
                return k
            if(nums[mid]==target):
                a=sol(mid+1,j,k)
                k=mid
                return max(a,k)
            if(nums[mid]<target):
                a=sol(mid+1,j,k)
                return a
                
            if(nums[mid]>target):
                a=sol(i,mid-1,k)
                return a
        lt=len(nums)
        lans=sol(0,lt-1,-1)

        def solf(i,j,tar):
            print(i,j)
            mid=(j+i)//2
            if(i==j+1):
                if(nums[i]==tar):
                    return i
                return float('inf')
            if(nums[mid]==tar):
                a=solf(i,mid-1,tar)
                return min(a,mid)
            if(nums[mid]<tar):
                a=solf(mid+1,j,tar)
                return min(a,float('inf'))
        # print(lans)
        if(lans==-1):
            return [-1,-1]
        rans=solf(0,lans,nums[lans])
        return [rans,lans]