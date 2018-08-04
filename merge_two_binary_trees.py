# https://leetcode.com/problems/merge-two-binary-trees/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        '''
        t1 not none and t2 not none
        merged = TreeNode(t1.val+t2.val)
        merged.left = mergeTrees(t1.left, t2.left)
        merged.right = mergeTree(t1.right, t2.right)

        t2 none
        merged = t1

        t1 none
        merged = t2
        '''

        merged = None
        if t1 is None and t2 is not None:
            merged = t2
        elif t2 is None and t1 is not None:
            merged = t1
        elif t1 is not None and t2 is not None:
            merged = TreeNode(t1.val + t2.val)
            merged.left = self.mergeTrees(t1.left, t2.left)
            merged.right = self.mergeTrees(t1.right, t2.right)

        return merged