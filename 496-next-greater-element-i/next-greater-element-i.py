class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        st=[]
        ans=[]
        l1=len(nums2)
        l2=len(nums1)
        temp=float("-inf")
        for i in range(l1-1,-1,-1):
            while(st and st[-1]<nums2[i]):
                st.pop()
            dic[nums2[i]] = st[-1] if st else -1
            st.append(nums2[i])
        return [dic[num] for num in nums1]
            


        