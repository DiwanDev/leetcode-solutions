class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        res = []
        for nums in nums1:
            greater = -1
            for j in range(n - 1, -1, -1):
                if nums < nums2[j]:   
                    greater = nums2[j]
                elif nums == nums2[j]:
                    break
            res.append(greater)
        return res