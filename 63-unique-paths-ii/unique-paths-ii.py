class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        length1=len(obstacleGrid)
        length2=len(obstacleGrid[0])
        arr=[[-1 for _ in range(length2)] for _ in range(length1)]
        print(arr)
        def sol(v,h):
            
            if(v>(length1-1) or h>(length2-1)):
                return 0
            if(obstacleGrid[v][h]==1):
                return 0
            if(arr[v][h]!=-1):
                return arr[v][h]
            if(v==length1-1 and h== length2-1):
                return 1

            a=sol(v+1,h)
            b=sol(v,h+1)
            arr[v][h]=a+b
            return a+b
        return sol(0,0)

