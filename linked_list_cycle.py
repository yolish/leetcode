#https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    '''

    head:1->[2->3->4-5<>2]
    curr_node:None, tail:None, stop_node: 0-  (ListNode(0))

    curr_node:1->[2->3->4-5<>2]
    head:2->[3->4->5<>2]
    tail:stop_node
    curr_node:1->stop_node
    tail:1->stop_node

    curr_node:2->[3->4->5<>2]
    head:[3->4->5<>2]
    curr_node:2->[1->stop_node]
    tail:2->[1->stop_node]

    curr_node:3->[4->5<>2->1->stop_node]
    head:4->[5<>2->1->stop_node]
    curr_node:3->[2->1->stop_node]
    tail:3->[2->1->stop_node]

    curr_node:4->[5<>2->1->stop_node]
    head:5->[2->1->stop_node]
    curr_node:>4->[3->2->1->stop_node]
    tail:4->[3->2->1->stop_node]

    ...

    head:stop_node



    '''

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        has_cycle = False
        curr_node = None
        tail = None
        stop_node = ListNode(None)
        while head != None:
            curr_node = head
            head = head.next
            if tail == None:
                tail = stop_node
            curr_node.next = tail
            tail = curr_node
            if head == stop_node:
                has_cycle = True
                break
        return has_cycle

