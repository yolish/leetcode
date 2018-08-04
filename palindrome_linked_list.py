# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    class ListNode(object):
        def __init(self, x):
            self.val = x
            self.next = None

    '''
    head:1->[2->2->1-]
    n:0

    #get size by the traversing
    n:4
    mid:2

    #advance n/2 times if n is even and n/2+1 if it is odd
    tail:1->[2->2->1-]
    tail:2->[2->1-]
    tail:2-[>1-]

    #reverse the list in place
    prev_node:2-[>1-]
    new_head:1-
    prev_node:2-
    tail:2-

    prev_node:1-
    new_head:-
    prev_node:1->2-
    tail:1->2-

    #compare lists and break if we get a pair of non-equal values
    head:1->2-
    tail:1->2-
    '''

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        is_palindrome = True

        # get the list's size to calculate mid point O(n) time, O(1) space
        n = 0
        tail = head
        while tail != None:
            tail = tail.next
            n = n + 1
        mid = n / 2

        # adavnce tail to the middle  O(n/2) time, O(1) space
        tail = head
        i = 0
        k = n / 2
        if n % 2 == 1:
            k = k + 1
        while i < k and tail != None:
            tail = tail.next
            i = i + 1

        # reverse the second half of the list in place  O(n/2) time, O(1) space
        new_head = tail
        tail = None
        prev_node = None
        while new_head != None:
            prev_node = new_head
            new_head = new_head.next
            prev_node.next = tail
            tail = prev_node
        # compare lists
        while tail != None and head != None:  # this is important when n is an odd number
            if tail.val != head.val:
                is_palindrome = False
                break
            tail = tail.next
            head = head.next

        return is_palindrome




