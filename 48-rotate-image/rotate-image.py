def rotateSquare(i,n,matrix):
    if n == 0  or n == 1:
        return
    else:
        for j in range(i,n-i-1):
            temp1 = matrix[j][n-i-1]
            matrix[j][n-i-1] = matrix[i][j]
            temp2 = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = temp1
            temp3 = matrix[n-j-1][i]
            matrix[n-j-1][i] = temp2
            matrix[i][j] = temp3


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n%2:
            q = n//2
        else:
            q = n//2 + 1
        for i in range(q):
            rotateSquare(i,n,matrix)
