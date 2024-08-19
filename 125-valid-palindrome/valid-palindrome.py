class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        st=""
        for i in s:
            if(i.isalpha() or i.isnumeric()):
                st+=i
        if(st==st[::-1]):
            return True
        return False

       