class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        stringArr = []
        for letter in s:
            if letter.isalnum():
                stringArr.append(letter)

        newS = ''.join(stringArr)

        rev = newS[::-1]

        for i in range(len(newS)):
            if newS[i] != rev[i]:
                return False

        return True


"""
    Cover the initial string to lowercase
    Add all alphanumeric chars to an array
    Get a reversed version
    Standard palindrome
"""
