class Solution:
    def makeGood(self, s: str) -> str:
        length=len(s)
        count=0
        st=[]
        ans=s[0]
        for i in range(length):
            if(st and abs(ord(s[i])-ord(st[-1]))==32):
                st.pop()
                
            else:
                st.append(s[i])
                
        ans=""
        for i in st:
            ans+=i
        return ans