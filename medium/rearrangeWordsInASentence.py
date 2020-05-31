class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """

        wordArray = text.split(' ')
        wordArray.sort(key=len)
        res = (' '.join(wordArray)).lower()

        return res.capitalize()
