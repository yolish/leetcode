#https://leetcode.com/problems/add-two-numbers/description/
class Solution(object):
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def node_to_val(self, l):
        val = 0
        if l != None:
            val = l.val
        return val

    def get_next_node(self, l):
        next_node = None
        if l != None:
            next_node = l.next
        return next_node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_over = 0
        head = None
        curr_node = None
        while l1 != None or l2 != None:
            val1 = self.node_to_val(l1)
            val2 = self.node_to_val(l2)
            res = val1 + val2
            # compute node value and carry over value
            new_val = res + carry_over
            carry_over = new_val / 10
            new_val = new_val - 10 * carry_over
            # add new value
            if head == None:
                head = ListNode(new_val)
            else:
                if curr_node == None:
                    curr_node = ListNode(new_val)
                    head.next = curr_node
                else:
                    curr_node.next = ListNode(new_val)
                    curr_node = curr_node.next
            # prepare for the next iteration
            l1 = self.get_next_node(l1)
            l2 = self.get_next_node(l2)

        if carry_over > 0:
            carry_over_node = ListNode(carry_over)
            if curr_node == None:
                head.next = carry_over_node
            else:
                curr_node.next = carry_over_node

        return head




