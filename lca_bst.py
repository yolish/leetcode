# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        if p < root < q or q < root < p then root is the lca or root == p or root == q 
        if p,q < root then their lca is in the left subtree of root
        if p,q > root then their lca is in the right subtree

        '''
        #recursive
        if (p.val == root.val) or (q.val == root.val) or (p.val < root.val and root.val < q.val) or (
                q.val < root.val and root.val < p.val):
            return root
        elif (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:  # (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, q, p)

        '''
        iterative:
        p_val = p.val
        q_val = q.val
        root_val = root.val
        while not ((p_val == root_val) or (q_val == root_val) or (p_val < root_val and root_val < q_val) or (
                        q_val < root_val and root_val < p_val)):
            if (p_val < root_val and q_val < root_val):
                root = root.left
                root_val = root.val
            else:  # (p.val > root.val and q.val > root.val):
                root = root.right
                root_val = root.val
        return root 
        '''

