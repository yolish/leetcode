#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        '''
        iterative - breadth 
        '''
        traversal = []
        curr_level = [root]
        if root is not None:
            while True:
                next_level = []
                level_traversal = []
                for node in curr_level:
                    if node is not None:
                        level_traversal.append(node.val)
                        next_level.append(node.left)
                        next_level.append(node.right)
                if len(level_traversal) > 0:
                    traversal.append(level_traversal)
                else:
                    break
                curr_level = next_level
        return traversal



