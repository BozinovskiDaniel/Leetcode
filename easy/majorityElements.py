class Solution(object):
    import math

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        rate = int(math.floor(len(nums) / 2))
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key in nums:
            if count[key] > rate:
                return key


"""
    - Calculate the rate of occurrence
    - Store how many times a val occurs
    - Loop over and if its > rate, return key
"""
