class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length=len(nums)
        a=sum(nums)
        target=a
        # print(a)
        if(target%2==1):
            return False
        dic={}
        tar=target//2
        print(tar)
        def sol(i,tar,temp):
            if(dic.get((i,temp))!=None):
                return dic.get((i,temp)) 
            if(i>length-1):
                print(temp)
                if(temp==tar):
                    return True
                else:
                    return False
            
            if(temp==tar):
                return True
            b=sol(i+1,tar,temp+nums[i])
            if(b==True):
                return True
            a=sol(i+1,tar,temp)
            
            dic[(i,temp)]=(a or b)
            return (a or b)
        return sol(0,tar,0)
