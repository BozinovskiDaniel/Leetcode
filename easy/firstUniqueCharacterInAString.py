class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}

        for letter in s:
            if letter not in seen:
                seen[letter] = 1
            else:
                seen[letter] += 1

        for letter in s:
            if seen[letter] == 1:
                return s.index(letter)

        return -1  # No non repeating chars
