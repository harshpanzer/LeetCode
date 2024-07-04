# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        ansitr=ans
        itr=head.next
        temp=0
        while(itr!=None):
            if(itr.val>0):
                temp+=itr.val
                itr=itr.next
            else:
                ansitr.val=temp
                temp=0
                if(itr.next!=None):
                    ansitr.next=ListNode()
                    ansitr=ansitr.next
                itr=itr.next
        return ans