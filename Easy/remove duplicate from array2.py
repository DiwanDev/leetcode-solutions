class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for n in nums:
            if k < 2 or n != nums[k - 2]:
                nums[k] = n
                k += 1
        return k