# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

'''


class Solution(object):
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def get_list_length(self, l):
        n = 0
        while l != None:
            n = n + 1
            l = l.next
        return n

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # key observation: the intersection can start at most only when the lists are the same length
        # so if one list is longer than the other we need to traverse it x steps (x being the gap)
        # brute force will be to reverse and take the last node equal but we want time O(n) memory O(1)
        # and not to change the lists, so instead we will remember we traverse

        intersection_node = None
        # get the length of each list: a, b
        a = self.get_list_length(headA)
        b = self.get_list_length(headB)
        if a > 0 and b > 0:
            gap = a - b
            moveA = True
            if gap < 0:
                moveA = False
                gap = -1 * gap
            while gap > 0:
                if moveA:
                    headA = headA.next
                else:
                    headA = headB.next
                gap = gap - 1
            # both pointers point to equally long lists
            # go through both and remember when the intersection began
            begin_intersect = False
            while headA != None and headB != None:
                val_a = headA.val
                val_b = headB.val
                if val_a == val_b:
                    if not begin_intersect:
                        intersection_node = headA
                    begin_intersect = True
                else:
                    intersection_node = None
                    begin_intersect = False

            return intersection_node
