#https://leetcode.com/problems/insert-delete-getrandom-o1/description/
import random
class RandomizedSet(object):
    '''
    ["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[-1],[-2],[-2],[],[-1],[-2],[]]
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ds = set()
        self.keys = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        new_item = False
        if val not in self.ds:
            self.ds.add(val)
            self.keys.append(val)
            new_item = True
        return new_item

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        in_ds = False
        if val in self.ds:
            self.ds.remove(val)
            in_ds = True
        return in_ds

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        n = len(self.keys)
        while n > 0:
            index = random.randint(0, n - 1)
            my_key = self.keys[index]
            if my_key in self.ds:
                return my_key
            else:
                self.keys[index] = self.keys[n - 1]
                self.keys.pop()
                n = n - 1





                # Your RandomizedSet object will be instantiated and called as such:
                # obj = RandomizedSet()
                # param_1 = obj.insert(val)
                # param_2 = obj.remove(val)
                # param_3 = obj.getRandom()