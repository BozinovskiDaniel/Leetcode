class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        seen = {}
        for num in arr:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        freq = []
        for key in seen:
            if key == seen[key]:
                freq.append(key)

        if len(freq) == 0:
            return -1
        else:
            return max(freq)


"""
    - Get all freqs in hashmap
    - Get all valid in arr
    - Return max in arr
"""
