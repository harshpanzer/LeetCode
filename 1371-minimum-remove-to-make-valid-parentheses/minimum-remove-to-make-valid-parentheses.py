class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        check1=0
        stack=[]
        count=0
        for i in s:
            if(i==")" and count==0):
                continue
            elif(i=="("):
                count+=1
                check1=1
                stack.append(i)
            elif(i==")"):
                count-=1
                stack.append(i)
            else:
                stack.append(i)
        ans=[]
        stack=stack[::-1]
        check2=0
        for i in stack:
            if(i=="(" and check2==0):
                count-=1
                continue
            if(count<0 and i==")"):
                count+=1
                check2=1
                continue
            elif(count>0 and i=="("):
                
                count-=1
                continue
            else:
                if(i==")"):
                    check2=1
                ans.append(i)
        ans=ans[::-1]
        return "".join(ans)