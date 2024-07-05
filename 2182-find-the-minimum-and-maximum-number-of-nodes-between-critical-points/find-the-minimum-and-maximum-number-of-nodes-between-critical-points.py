# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        lst=[]
        index=1
        prev=head.val
        curr=head.next
        while(curr.next!=None):
            if((curr.val>prev and curr.val>curr.next.val)or(curr.val<prev and curr.val<curr.next.val)):
                lst.append(index)
                index+=1
                prev=curr.val
                curr=curr.next
            else:
                index+=1
                prev=curr.val
                curr=curr.next
        print(lst)
        length=len(lst)
        if(length<2):
            return [-1,-1]  
        maxx=lst[length-1]-lst[0]
        minn=324324324234324234234234
        for i in range(length-1):
            temp=lst[i+1]-lst[i]
            if(temp<minn):
                minn=temp
        return [minn,maxx]

