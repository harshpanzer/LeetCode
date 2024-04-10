def indexx(sel,length):
    if(sel<length):
        return sel
    while(sel>length-1):
        sel=sel%length
        sel=(sel*2)+1
        return indexx(sel,length)

class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort()
        length=len(deck)
        ans=deck.copy()

        # for i in range(length):
        #     ans.append(0)
        for i in range(length):
            sel=i*2
            if(sel<=length-1):
                ans[sel]=deck[i]
                
            elif(sel>length-1):
                
                a=indexx(sel,length)
                ans[a]=deck[i]
        return ans