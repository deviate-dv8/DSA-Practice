class Solution(object):
    def twoSum(self, nums, target):
        for idxi, i in enumerate(nums):
            for idxj, j in enumerate(nums):
                if idxi == idxj:
                    continue
                if i + j == target:
                    return [idxi, idxj]
