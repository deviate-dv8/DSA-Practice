class Solution(object):
    def isValid(self, word):
        vowels = "aeiou"
        consonants = "qwrtypsdfghjklzxcvbnm"
        valid_characters = "qwertyuiopasdfghjklzxcvbnm1234567890"
        parsed_word = word.lower()
        is_valid = True
        if len(word) < 3:
            is_valid = False
        for letter in parsed_word:
            if letter not in valid_characters:
                is_valid = False
        if (
            len(list(filter(lambda x: x in vowels, parsed_word))) == 0
            or len(list(filter(lambda x: x in consonants, parsed_word))) == 0
        ):
            is_valid = False
        return is_valid
        """
        :type word: str
        :rtype: bool
        """
