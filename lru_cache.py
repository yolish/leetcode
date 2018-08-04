#https://leetcode.com/problems/lru-cache/description/
class LRUCache(object):
    class LinkedNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import time
        self.capacity = capacity
        self.cache = {}
        self.stamps = {}
        self.timeline = None  # a linked list of time stamps t1->t2->t3->...
        self.last_time = None  # the last timestamp added
        self.timer = time.time

    def update(self, key, value, lru_key=None, lru_stamp=None):
        my_time = self.timer()
        if lru_key != None and lru_stamp != None:  # max_capacity: remove key
            del self.cache[lru_key]
            del self.stamps[lru_stamp]
        elif lru_key == None and lru_stamp != None:  # update time stamp
            del self.stamps[lru_stamp]
        self.cache[key] = [value, my_time]
        self.stamps[my_time] = key

        if self.timeline is None:
            self.timeline = ListNode(my_time)
        else:
            if self.last_time == None:
                self.last_time = ListNode(my_time)
                self.timeline.next = self.last_time
            else:
                self.last_time.next = ListNode(my_time)
                self.last_time = self.last_time.next

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        value = -1
        record = self.cache.get(key)
        if record != None:
            value = record[0]
            lru_stamp = record[1]
            self.update(key, value, lru_key=None, lru_stamp=lru_stamp)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        lru_key = None
        lru_stamp = None
        if key not in self.cache:
            if len(self.cache) == self.capacity and self.timeline != None:
                lru_stamp = self.timeline.val
                while lru_stamp not in self.stamps:
                    self.timeline = self.timeline.next
                    lru_stamp = self.timeline.val
                self.timeline = self.timeline.next
                lru_key = self.stamps.get(lru_stamp)

        else:
            lru_stamp = self.cache.get(key)[1]
        self.update(key, value, lru_key, lru_stamp)

    '''
        def __init__(self, capacity):
        """
        :type capacity: int
        """
        import time
        self.capacity = capacity
        self.cache = {}
        self.stamps = {}
        self.timer = time.time

    def update(self, key, value, lru_key=None, lru_stamp=None):
        my_time = self.timer()
        if lru_key != None and lru_stamp != None:  # max_capacity: remove key
            del self.cache[lru_key]
            del self.stamps[lru_stamp]
        elif lru_key == None and lru_stamp != None:  # update time stamp
            del self.stamps[lru_stamp]
        self.cache[key] = [value, my_time]
        self.stamps[my_time] = key

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        value = -1
        record = self.cache.get(key)
        if record != None:
            value = record[0]
            lru_stamp = record[1]
            self.update(key, value, lru_key=None, lru_stamp=lru_stamp)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        lru_key = None
        lru_stamp = None
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                lru_stamp = self.timer()
                for stamp in self.stamps.keys():
                    if lru_stamp > stamp:
                        lru_stamp = stamp
                lru_key = self.stamps.get(lru_stamp)
        else:
            lru_stamp = self.cache.get(key)[1]
        self.update(key, value, lru_key, lru_stamp)

    '''



'''
1:2,x1, x1:1
1:2,x2  x2:1
1:2,x2, 2:5,x3; x2:1,x3:2
3:3,x4, 2:3,x3; x3:2,x4:3
2:3,x5, 3:3,x4; x5:2,x4:3
["LRUCache","get","put","get","put","put","get","get"]
[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
capacity: 2
c:{} s:{} null
c:{} s:{} -1
c:{2:[6, x1]}, s:{x1:2} null
c:{2:[6, x1]}, s:{x1:2} -1
c{2:[6, x1], 1:[5, x2]} s:{x1:2, x2:1}

["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

c:{2:[1,x1]} s:{x1:1} -1 
c:{1:[1,x2], 2:[1,x1]} s:{x1:2, x2:1} -1 
c:{1:[1,x2], 2:[3,x1]} s:{x1:2, x2:1}




'''




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

    '''
        def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.ages = []  # first element is the least used

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.cache.get(key)
        if val == None:
            val = -1
        else:
            self.ages.remove(key)
            self.ages.append(key)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                least_used = self.ages[0]
                del self.cache[least_used]
                self.ages.pop(0)
            self.cache[key] = value
            self.ages.append(key)



            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)
    '''
