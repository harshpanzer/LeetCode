class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        m,n=0,0
        for i,j in stones:
            m=max(m,i)
            n=max(n,j)
        size=[1]*(m+n+2)
        dic={}
        par=[i for i in range(m+n+2)]
        def FindPar(x):
            if(x==par[x]):
                return x
            par[x]=FindPar(par[x])
            return par[x]
        def UnionFind(x,y):
            parx=FindPar(x)
            pary=FindPar(y+m+1)
            if(parx==pary):
                return 
            elif(size[parx]==size[pary]):
                par[parx]=pary
                size[pary]+=1
                return
            elif(size[parx]<size[pary]):
                par[parx]=pary
                size[pary]+=1
                return
            else:
                par[pary]=parx
                size[parx]+=1
                return
        for i,j in stones:
            UnionFind(i,j)
            dic[i]=1
            dic[j+m+1]=1
        for i,j in stones:
            FindPar(i)
            FindPar(j+m+1)
        print(par,dic)
        lst=[]
        for i in range(m+n+2):
            if(dic.get(i)==None):
                lst.append(i)
        b=0
        for i in lst:
            par.pop(i-b)
            b+=1
        print(par)
        a=set(par)
        
        length=len(a)
        return (len(stones)-length)