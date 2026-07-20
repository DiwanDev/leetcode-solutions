class Solution(object):
    def search(self, nums, target):
        n=0
        if target in nums:
            for i in nums:
                if i==target:
                    break 
                n+=1
            return n
        else:
            return -1