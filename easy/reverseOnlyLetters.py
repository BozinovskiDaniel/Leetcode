class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = []

        for letter in S:
            if letter.isalpha():
                letters.append(letter)

        letters.reverse()
        string = []

        for l in S:
            if l.isalpha():
                string.append(letters.pop(0))
            else:
                string.append(l)

        return ''.join(string)


"""
    - Save letters into an array
    - Reverse letters and loop back over S
    - If it is alpha, pop it off the letters arr
    - Else, append to new str
"""
