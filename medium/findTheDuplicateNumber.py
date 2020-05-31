class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                return num

        return -1  # Not found
