# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # left boundary without leaves
    def left_boundary(self, root, boundary):
        if root is not None:
            has_left_child = root.left is not None
            has_right_child = root.right is not None
            if has_left_child or has_right_child:
                boundary.append(root.val)
            if has_left_child:
                self.left_boundary(root.left, boundary)
            elif has_right_child:
                self.left_boundary(root.right, boundary)

    # leaves from left to right
    def leaves_boundary(self, root, boundary):
        if root is not None:
            if root.left is None and root.right is None:
                boundary.append(root.val)
            self.leaves_boundary(root.left, boundary)
            self.leaves_boundary(root.right, boundary)

    # right boundary without leaves
    def right_boundary(self, root, boundary):
        if root is not None:
            has_left_child = root.left is not None
            has_right_child = root.right is not None
            if root.right is not None:
                self.right_boundary(root.right, boundary)
            elif has_left_child:
                self.right_boundary(root.left, boundary)
            if has_left_child or has_right_child:
                boundary.append(root.val)

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        observation: 
        the boundary = [top down left boundary - leaves] + [leaves from left to right] + [bottom up right_boundary - leaves]
        top down left boundary - append val if not leaf, call left if there is, otherwise call right
        leaves left to right: preorder, and adding only when it is a leaf
        bottom up right boundary - call right if there is, otherwise call left, append only if not leaf
        edge cases: root is empty, root is a leaf
        important: if the left side is None: we'll put only the root value
        for the right side, we'll pop the root to avoid duplications
        '''
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        boundary = []
        if root.left is not None:
            self.left_boundary(root, boundary)
        else:
            boundary = [root.val]
        self.leaves_boundary(root, boundary)
        if root.right is not None:
            self.right_boundary(root, boundary)
            boundary.pop()
        return boundary