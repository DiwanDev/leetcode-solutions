class Solution(object):
    def firstPalindrome(self, words):
        for w in words:
            l, r = 0, len(w) - 1
            while w[l] == w[r]:
                if l >= r:
                    return w
                l, r = l + 1, r - 1
        return ""
        