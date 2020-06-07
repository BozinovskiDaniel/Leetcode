# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """

        return self.dfs(original, cloned, target)

    def dfs(self, original, cloned, target):

        if not original or not cloned:
            return None

        # Base case
        if original == target:
            return cloned

        return self.dfs(original.left, cloned.left, target) or self.dfs(original.right, cloned.right, target)


"""
    - Perform a dfs and if the original == target, return cloned
    - If their null, return None
    - Else return dfs on left or dfs on right
"""
