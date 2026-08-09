class Solution(object):
    def removeStars(self, s):
        d=[]
        for i in range(len(s)):
            if s[i]=="*":
                d.pop()
            else:
                d.append(s[i])
        result = "".join(d)
        return result