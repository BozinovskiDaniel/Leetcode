"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        # Use BFS
        depth = 0
        queue = []

        queue.append(root)

        while len(queue) > 0:

            for i in range(len(queue)):
                curr = queue.pop(0)

                for child in curr.children:
                    queue.append(child)

            depth += 1

        return depth


"""
    - Perform a standard BFS
    - Keep a counter of the depth
    - Return the depth
"""
