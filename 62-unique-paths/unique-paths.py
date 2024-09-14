class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans=[[-1 for _ in range(n)] for _ in range(m)]
        print(ans)
        def sol(v,h):
            a=0
            b=0
            if v > m - 1 or h > n - 1:
                return 0
            if(v==m-1 and h==n-1):
                return 1
            if ans[v][h] != -1:
                return ans[v][h]
            if(v<m-1):
                a=sol(v+1,h)
            if(h<n-1):
                b=sol(v,h+1)
            print(a+b)
            ans[v][h]= a+b
            return ans[v][h]
        return sol(0,0)