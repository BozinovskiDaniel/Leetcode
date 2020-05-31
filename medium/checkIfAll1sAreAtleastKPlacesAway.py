class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = -1

        for i in range(len(nums)):

            if nums[i] == 1:
                if temp == -1:
                    temp = i
                    continue
                else:
                    if (i - temp - 1) < k:
                        return False
                    temp = i

        return True
