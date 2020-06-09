# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        trav = []

        self.doInorderTrav(root, trav)

        return trav

    def doInorderTrav(self, root, trav):

        # Inorder => L->P->R
        if root:
            self.doInorderTrav(root.left, trav)
            trav.append(root.val)
            self.doInorderTrav(root.right, trav)


"""
    - Do an Inorder Traversal (left -> * -> right)
    - Return arr of vals
"""
