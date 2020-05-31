class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split(' ')

        count = 0

        for word in words:
            count += 1
            if word.startswith(searchWord):
                return count

        return -1  # Not a prefix
