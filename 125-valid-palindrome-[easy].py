class Solution(object):
    def isPalindrome(self, s):
        small_letters = list("qwertyuiopasdfghjklzxcvbnm1234567890")
        parsed = list(filter(lambda x: x in small_letters, list(s.lower())))
        after = list(reversed(parsed))
        if parsed == after:
            return True
        else:
            return False
