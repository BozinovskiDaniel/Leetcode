class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = 0
        nums.sort()  # Sort the nums

        fullSeq = []
        for i in range(len(nums) + 1):
            fullSeq.append(i)

        # Compare
        for i in range(len(fullSeq)):
            if fullSeq[i] not in nums:
                missing = fullSeq[i]
                break

        return missing
