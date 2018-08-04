# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        encoding = []
        if root is not None:
            encoding.append(root.val)
            children = [root.left, root.right]
            while True:
                last_level = True
                next_gen = []
                for child in children:
                    if child is not None:
                        encoding.append(child.val)
                        next_gen.append(child.left)
                        next_gen.append(child.right)
                        last_level = False
                    else:
                        encoding.append(None)
                if last_level:
                    encoding = encoding[:len(encoding) - len(children)]
                    break
                else:
                    children = next_gen
        return str(encoding)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if len(data) == 2:  # note: data: [] -> empty tree
            root = None
        else:
            encoding = data[1:(len(data) - 1)].split(", ")
            n = len(encoding)
            root = TreeNode(encoding[0])
            if n > 1:
                none_str = "None"
                curr_level = [root]
                i = 0
                while i < n:
                    next_level = []
                    for node in curr_level:
                        if node is not None:
                            left_index = i + 1
                            if left_index < n:
                                left_val = encoding[left_index]
                                left_child = None
                                if left_val != none_str:
                                    left_child = TreeNode(left_val)
                                    node.left = left_child
                                next_level.append(left_child)
                            else:
                                i = left_index
                                break
                            right_index = i + 2
                            if right_index < n:
                                right_val = encoding[right_index]
                                right_child = None
                                if right_val != none_str:
                                    right_child = TreeNode(right_val)
                                    node.right = right_child
                                next_level.append(right_child)
                            else:
                                i = right_index
                                break
                            i = i + 2

                    curr_level = next_level

        return root






        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))