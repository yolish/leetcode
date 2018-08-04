#
class Solution(object):
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        curr_node = None
        # while both lists are non-empty, take the smaller value and grow the merged list,
        # while advancing on the respective input list
        while l1 != None and l2 != None:
            val1 = l1.val
            val2 = l2.val
            if val1 < val2:
                my_val = val1
                l1 = l1.next
            else:
                my_val = val2
                l2 = l2.next

            if head == None:
                head = ListNode(my_val)
            else:
                if curr_node == None:
                    curr_node = ListNode(my_val)
                    head.next = curr_node
                else:
                    next_node = ListNode(my_val)
                    curr_node.next = next_node
                    curr_node = next_node

                    # if we reached the end of one of them, simply append the other
        next_node = None
        if l1 != None and l2 == None:
            next_node = l1
        elif l1 == None and l2 != None:
            next_node = l2

        if head == None:  # edge case: one of the input lists is empty
            head = next_node
        elif curr_node == None:  # we only had one iteration
            head.next = next_node
        else:
            curr_node.next = next_node

        return head




