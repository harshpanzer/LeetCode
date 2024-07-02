class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1=len(nums1)
        length2=len(nums2)
        ans=[]
        i=0
        j=0
        while(i<length1 and j<length2):
            if(nums1[i]<nums2[j]):
                i+=1
            elif(nums1[i]>nums2[j]):
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans