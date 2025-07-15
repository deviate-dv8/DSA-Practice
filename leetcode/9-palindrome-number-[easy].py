class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if str(x)[::-1] != str(x):
            return False
        return True
        """
        :type x: int
        :rtype: bool
        """
