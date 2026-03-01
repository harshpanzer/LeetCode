class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        i,j=0,1
        lt=len(s)
        count=0
        lst=[]
        for l in s:
            lst.append(l)
        for kl in range(lt):
            i,j=0,1
            count=0
            while(i!=lt):
                # print(i,j,lst)
                if(lst[i]=='*'):
                    i+=1
                    j=i+1
                    count=0
                    continue
                if(j==lt):
                    i+=1
                    j=i+1
                    count=0
                    continue
                elif(count==k):
                    i+=1
                    j=i+1
                    count=0
                    continue
                elif(lst[i]==lst[j] and lst[i]!='*'):
                    lst[j]='*'
                    i=0
                    j=1
                    count=0
                # elif(lst[i]==lst[j] and lst[i]=='*'):
                #     i+=1
                #     j=i+1
                elif(lst[i]!=lst[j] and (lst[i]=='*' or lst[j]=='*')):
                    j+=1
                elif(lst[i]!=lst[j]):
                    j+=1
                    count+=1
        ans=""
        for i in lst:
            if(i=='*'):
                continue
            ans+=i
        return ans