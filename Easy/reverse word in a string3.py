class Solution(object):
    def reverseWords(self, s):
        tmp_str = ""
        res = ""
        for r in range(len(s) + 1):
            if r == len(s) or s[r] == ' ':
                res += tmp_str
                tmp_str = ""
                if r != len(s):
                    res += " "
            else:
                tmp_str = s[r] + tmp_str
        return res