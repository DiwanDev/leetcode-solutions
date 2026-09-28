class Solution(object):
    def ArraySpecial(self, nums):
        for j in range(1, len(nums)):
            if nums[j - 1] % 2 == nums[j] % 2:
                return False
        return True
        