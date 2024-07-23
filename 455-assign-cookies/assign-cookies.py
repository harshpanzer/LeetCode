class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        length1=len(s)
        length2=len(g)
        ans=0
        pt1=0
        pt2=0
        g.sort()
        s.sort()
        temp=0
        while(pt1<length1 and pt2<length2):
            if(s[pt1]>=g[pt2]):
                print(temp)
                ans+=1
                pt1+=1
                pt2+=1

            else:
                pt1+=1
        return ans
