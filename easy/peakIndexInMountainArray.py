class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # Loop over from the second value to the end and compare
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                return i
            
        return -1 # Not found