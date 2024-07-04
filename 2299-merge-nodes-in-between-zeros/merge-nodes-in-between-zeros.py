# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        itr2=head
        itr=head.next
        temp=0
        while(itr!=None):
            if(itr.val>0):
                temp+=itr.val
                itr=itr.next
            else:
                itr2.next=itr
                itr2=itr2.next
                itr2.val=temp
                temp=0
                itr=itr.next
        return head.next
        