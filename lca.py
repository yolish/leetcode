#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def get_parent(self, root, node, level):
        if root is not None:
            level[0] = level[0] + 1
            if root.left is not None and root.left.val == node.val:
                return root
            if root.right is not None and root.right.val == node.val:
                return root
            my_parent = self.get_parent(root.left, node, level)
            if my_parent is not None:
                return my_parent
            my_parent = self.get_parent(root.right, node, level)
            if my_parent is not None:
                return my_parent



    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        '''
        cases:
        A p,q are children of the same parent 
        B-C p is a child of q (or vice versa) 
        p and q are decendants of r (where r might be == q or r == q)
        we get the parents of p and 
        if A, B OR C then we found the lca, otherwise, we set find their parents and repeat
        important: if p's parent is the root or q parent is the root we do not advance any further

                 _______3______
               /              \
            ___5__          ___1__
           /      \        /      \
           6      _2       0       8
                 /  \
                 7   4



        [-1,0,3,-2,4,null,null,8]
        8
        4
        [3,5,1,6,2,0,8,null,null,7,4]
        7
        8
        '''
        lca = None
        p_parent = None
        q_parent = None
        get_p_parent = True
        get_q_parent = True
        p_level = [0]
        q_level = [0]
        while lca is None:
            if p.val == root.val or q.val == root.val:
                lca = root
                break
            if get_p_parent:
                p_parent = self.get_parent(root, p, p_level)
            if get_q_parent :
                q_parent = self.get_parent(root, q, q_level)
            # p is a direct child of q
            if p_parent.val == q.val:
                lca = p_parent
            # q is a direct child of p
            elif q_parent.val == p.val:
                lca = p
            # p and q are children of the same parent
            elif p_parent.val == q_parent.val:
                lca = p_parent
            # only advance the one lower (or both if they are the same height)
            if p_level[0] == q_level[0]:
                p = p_parent
                q = q_parent
                q_level[0] = 0
                p_level[0] = 0
                get_p_parent = True
                get_q_parent = True
            elif p_level[0] < q_level[0]:
                q = q_parent
                q_level[0] = 0
                get_p_parent = False
            else:
                p = p_parent
                p_level[0] = 0
                get_q_parent = False



        return lca




