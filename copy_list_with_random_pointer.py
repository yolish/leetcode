#https://leetcode.com/problems/copy-list-with-random-pointer/
class Solution(object):
    class RandomListNode(object):
        def __init__(self, x):
            self.label = x
            self.next = None
            self.random = None

    def get_node(self, head, pointers):
        node = None
        if head in pointers:
            node = pointers.get(head)
        else:
            node = RandomListNode(head.label)
            pointers[head] = node
        if head.random != None:
            if head.random in pointers:
                node.random = pointers.get(head.random)
            else:
                node.random = RandomListNode(head.random.label)
                pointers[head.random] = node.random
        return node

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        pointers = {}
        my_head = None
        my_node = None
        while head != None:
            if my_head == None:
                my_head = self.get_node(head, pointers)
            else:
                if my_node == None:
                    my_node = self.get_node(head, pointers)
                    my_head.next = my_node
                else:
                    my_node.next = self.get_node(head, pointers)
                    my_node = my_node.next
            head = head.next
        return my_head