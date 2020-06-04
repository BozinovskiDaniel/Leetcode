class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        # Create matrix
        matrix = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            matrix.append(row)

        # Loop over indices and apply

        for (x, y) in indices:

            # Increment all in row
            for i in range(len(matrix[0])):
                matrix[x][i] += 1
            # Increment all in col
            for i in range(len(matrix)):
                matrix[i][y] += 1

        numOfOdd = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] % 2 != 0:
                    numOfOdd += 1

        return numOfOdd


"""
    - Create matrix with 0s
    - Loop over indices and increment respective cols and rows
    - Count num of odd in matrix
    - Return count
    - Easy
"""
