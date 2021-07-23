"""
    https://leetcode.com/problems/binary-tree-pruning/
    814. Binary Tree Pruning (medium)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        if self.update(root):
            return None
        else:
            return root

    def update(self, node):
        if node.left is not None:
            if self.update(node.left):
                node.left = None

        if node.right is not None:
            if self.update(node.right):
                node.right = None

        if node.left is None and node.right is None:
            return True if node.val == 0 else False

        return False
