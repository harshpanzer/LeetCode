from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        vis={}
        q=deque()
        for i in range(len(board)):
            for j in [0,len(board[0])-1]:
                if(board[i][j]=="O"):
                    q.append([i,j])
        for i in[0,len(board)-1]:
            for j in range(len(board[0])):
                if(j!=0 and j!=len(board[0])-1):
                    if(board[i][j]=="O"):
                        q.append([i,j])
        check={}
        while(q):
            i,j=q.popleft()

            for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                a=i+x
                b=j+y
                if(a<0 or b<0 or a>=len(board) or b>=len(board[0]) or (a,b) in check or (a,b) in q):
                    continue
                elif(board[a][b]=="O"):
                    check[(a,b)]=1
                    q.append([a,b])
                else:
                    continue
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if((i,j) not in check and board[i][j]=="O"):
                    board[i][j]="X"
        