class Solution(object):
    def groupAnagrams(self, strs):
        sortHash = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in sortHash:
                sortHash[key].append(word)
                continue
            sortHash[key] = [word]
        return list(sortHash.values())
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
