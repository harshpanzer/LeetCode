from collections import deque
class MyStack:

    def __init__(self):
        self.dq1=deque()
        self.dq2=deque()

    def push(self, x: int) -> None:
        if(len(self.dq1)==0):
            self.dq1.appendleft(x)
            return
        self.dq1.appendleft(x)
        for i in range(len(self.dq1)-1):
            a=self.dq1[i+1]
            self.dq1[i+1]=self.dq1[i]
            self.dq1[i]=a
        
        


    def pop(self) -> int:
        a=self.dq1.pop()
        return a

    def top(self) -> int:
        return self.dq1[len(self.dq1)-1]

    def empty(self) -> bool:
        return len(self.dq1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()