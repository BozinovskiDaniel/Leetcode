class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return 0

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return 1
        else:
            return min(self.stack)


"""
    - Standard stack
    - Last In, First Out
    - Follow that logic and read the question properly
"""
