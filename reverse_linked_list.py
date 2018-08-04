#https://leetcode.com/problems/reverse-linked-list/description/
class Solution(object):
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = None
        prev_node = None
        while head != None:
            prev_node = head  # advance prev_node
            head = head.next  # advance head
            prev_node.next = tail  # append tail to the previuos node
            tail = prev_node  # make tail point to the prev node now appended with the tail

        return tail