class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        lt=len(s)
        ans=0
        left=0
        right=0
        while(right<lt):
            # print(right,left)
            if(s[right] not in dic):
                if(right==left):
                    ans=max(ans,1)
                    dic[s[right]]=right
                    right+=1
                else:
                    dic[s[right]]=right
                    ans=max(ans,right-left+1)
                    right+=1
            
            else:
                if(dic.get(s[right])<left):
                    dic[s[right]]=right
                    ans=max(ans,right-left+1)
                
                    right+=1
                    continue
                left=dic.get(s[right])+1
                
                dic[s[right]]=right
                ans=max(ans,right-left+1)
                
                right+=1
            print(left,right)
        return ans

