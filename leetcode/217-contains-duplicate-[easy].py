class Solution(object):
    def containsDuplicate(self, nums):
        numSeen = set()
        for num in nums:
            if num in numSeen:
                return True
            numSeen.add(num)
        return False

        """
        :type nums: List[int]
        :rtype: bool
        """
