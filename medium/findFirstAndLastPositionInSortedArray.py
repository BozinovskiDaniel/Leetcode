class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# logn -> binary search

        return [self.getStartIndex(nums, target), self.getEndIndex(nums, target)]

    def getStartIndex(self, nums, target):

        index = -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start)/2

            # Finding left, move left
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1

            if nums[mid] == target:
                index = mid

        return index

    def getEndIndex(self, nums, target):

        index = -1

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start)/2

            # Finding right, move right
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

            if nums[mid] == target:
                index = mid

        return index


"""
- Create two separate binary search functions
- One to find left => start with index = -1, search left first then right
- One to find right => start with index = -1, search right first then left
"""
