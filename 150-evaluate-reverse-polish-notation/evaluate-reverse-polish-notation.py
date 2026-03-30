class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a)/b))
            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            else:
                stack.append(int(i))

        return stack[0]