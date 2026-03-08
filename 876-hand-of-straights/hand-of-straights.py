import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heap=[]
        for i in hand:
            heapq.heappush(heap,i)
        prev=heap[0]-1
        arr=[]
        size=groupSize
        while(heap):
            # print(heap,size)
            a=heapq.heappop(heap)
            
            if(a-1==prev):
                size-=1
                if(size==0):
                    size=groupSize
                    for i in arr:
                        heapq.heappush(heap,i)
                    if(not heap):
                        return True
                    prev=heap[0]-1
                    arr=[]
                else:
                    prev=a
            elif(a==prev):
                arr.append(a)
                continue
            else:
                return False
        length=len(arr)
        if(groupSize!=size):
            return False
        return True

                