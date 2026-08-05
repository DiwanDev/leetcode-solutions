class Solution(object):
    def maxScore(self, s):
        n,res=len(s),0
        for i in range(1,n):
            leftz=0
            for j in range(i):
                if s[j]=='0':
                    leftz+=1
            righto=0
            for j in range(i,n):
                if s[j]=='1':
                    righto+=1
            res=max(res,leftz+righto)
        return res        