class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i <= j:
            self.swap(s, i, j)
            i += 1
            j -= 1

    def swap(self, s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp


"""
    - Loop from front and back simultaneously
    - Swap each element at each indices
"""
