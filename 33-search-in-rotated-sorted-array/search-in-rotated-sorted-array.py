# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         l = 0
#         h = n-1
#         m = -1
#         if nums[l]>nums[h]:
#             while l<h:
                
#                 m = (l+h)//2
#                 # print(m)
#                 if nums[m]>nums[l] and nums[m]>nums[h]:
#                     l = m
#                 elif nums[m]<nums[l] and nums[m]<nums[h]:
#                     h = m
#                 else:
#                     break
#         diff = n-m
#         l = 0
#         h = n-1
#         while l<h:
#             mid = ((l+h)//2)-diff
#             print(mid)
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid]<target:
#                 l = (mid+1)%n
#             else:
#                 h = (mid-1)%n
#         return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length=len(nums)
        low=0
        high=length-1
        mid=(low+high)//2
        
        while(low<=high):
            mid=(low+high)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>=nums[low]):
                if(nums[low]<=target<nums[mid]):
                    high=mid-1
                else:
                    low=mid+1
            else:
                if(nums[mid]<target<=nums[high]):
                    low=mid+1
                else:
                    high=mid-1
            

        return -1
                  