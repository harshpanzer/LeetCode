class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        length=len(bills)
        arr=[0,0,0]
        for i in range(length):
            if(bills[i]==5):
                arr[0]+=1
            elif(bills[i]==10):
                if(arr[0]>0):
                    arr[0]-=1
                    arr[1]+=1
                else:
                    return False
            else:
                if(arr[1]>0 and arr[0]>0):
                    arr[0]-=1
                    arr[1]-=1
                    arr[2]+=1
                elif(arr[0]>2):
                    arr[0]-=3
                    arr[2]+=1
                else:
                    return False
        return True
                