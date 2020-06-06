class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0

        # Loop over both
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    break
            else:
                count += 1

        return count


"""
    - Loop over both arrays
    - If the condition is true, break the loop
    - Else increment count
"""
