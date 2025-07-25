class Solution(object):
    #     def longestConsecutive(self, nums):
    #         if len(nums) == 0:
    #             return 0
    #         sortedNums = sorted(nums)
    #         counter = 1
    #         best = 1
    #         for i in range(len(sortedNums) - 1):
    #             if sortedNums[i] == sortedNums[i + 1]:
    #                 continue
    #             if (sortedNums[i] - sortedNums[i + 1]) == -1:
    #                 counter += 1
    #                 if counter > best:
    #                     best = counter
    #             else:
    #                 counter = 1
    #         return best
    #
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         """

    def longestConsecutive(self, nums):
        nonRepeatNums = set(nums)
        best = 0
        for num in nonRepeatNums:
            if num - 1 not in nonRepeatNums:
                increment = 0
                while num + increment in nonRepeatNums:
                    increment += 1
                    if increment > best:
                        best = increment
        return best
        """
        :type nums: List[int]
        :rtype: int
        """
