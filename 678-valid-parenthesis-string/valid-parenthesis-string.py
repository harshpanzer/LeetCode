class Solution:
    def checkValidString(self, s: str) -> bool:
        opened = stars = 0
        # check for problematic ")"
        for char in s:
            if char == ")":
                if opened == 0:
                    if stars == 0:
                        return False
                    stars -= 1
                else:
                    opened -= 1
            elif char == "(":
                opened += 1
            elif char == "*":
                stars += 1
        
        # check for problematic "("
        closed = stars = 0
        for char in reversed(s):
            if char == "(":
                if closed == 0:
                    if stars == 0:
                        return False
                    stars -= 1
                else:
                    closed -= 1
            elif char == ")":
                closed += 1
            elif char == "*":
                stars += 1
        
        return True