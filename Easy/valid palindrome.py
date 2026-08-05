class Solution(object):
    def isPalindrome(self, s):
        dnd=[]
        for i in range(len(s)):
            if(s[i].isalnum()):
                dnd.append(s[i])
        dn = [char.lower() for char in dnd]
        for i in range(len(dn)):
            if(dn[i]==dn[len(dn)-i-1]):
                continue
            else:
                return False
        return True