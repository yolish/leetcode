#https://leetcode.com/problems/merge-k-sorted-lists/description/

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

    def get_min_non_empty(self, lists):
        val = None
        index = 0
        n_non_empty_lists = 0
        for i, listnode in enumerate(lists):
            curr_val = None
            if listnode != None:
                curr_val = listnode.val
                n_non_empty_lists = n_non_empty_lists + 1
                if val == None:
                    val = curr_val
                    index = i
                else:
                    if val > curr_val:
                        val = curr_val
                        index = i
        return val, index, n_non_empty_lists

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        merged = []
        for l in lists:
            while l != None:
                merged.append(l.val)
                l = l.next
        merged.sort()

        head = None
        curr_node = None
        for val in merged:
            if head is None:
                head = ListNode(val)
            elif curr_node is None:
                curr_node = ListNode(val)
                head.next = curr_node
            else:
                curr_node.next = ListNode(val)
                curr_node = curr_node.next
        return head

        '''
        curr_node = None
        n_non_empty_lists = len(lists)

        while n_non_empty_lists > 1:
            min_val, min_index, n_non_empty_lists = self.get_min_non_empty(lists)
            lists[min_index] = lists[min_index].next
            if merged == None:
                merged = ListNode(min_val)
            elif curr_node == None:
                curr_node = ListNode(min_val)
                merged.next = curr_node
            else:
                curr_node.next = ListNode(min_val)
                curr_node = curr_node.next


        if n_non_empty_lists == 1:
            if merged == None:
                merged = lists[0]
            else: 
                my_list = lists[min_index]
                while my_list != None:
                    if curr_node == None:
                        curr_node = ListNode(min_val)
                        merged.next = curr_node
                    else:
                        curr_node.next = ListNode(min_val)
                        curr_node = curr_node.next
        '''

        return merged