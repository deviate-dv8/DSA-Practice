class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        for num in nums:
            num = str(num)
            if num in hashmap:
                hashmap[num] += 1
                continue
            hashmap[num] = 1
        sorted_items = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)
        return [int(item[0]) for item in sorted_items[:k]]
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
