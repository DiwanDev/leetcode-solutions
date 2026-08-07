class Solution(object):
    def backspaceCompare(self, s, t):
        j=[]
        l=[]
        for i in range(len(s)):
            if s[i]=='#':
                if len(j)>0:
                    j.pop()
            else:
                j.append(s[i])
        for i in range(len(t)):
            if t[i]=='#':
                if len(l)>0:
                    l.pop()
            else:
                l.append(t[i]) 
        if j==l:
            return True
        else:
            return False     

        