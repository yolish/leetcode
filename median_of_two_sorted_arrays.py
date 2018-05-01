#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):
    def median(self, l):
        n = len(l)
        if n == 0:
            return None
        if n%2 == 1:
            val = l[n/2]*1.0
        else:
            middle = n/2.0
            val1 = l[int(middle - 0.5)]
            val2 = l[int(middle + 0.5)]
            val = (val1+val2)/2.0
        return val


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        med1 = self.median(nums1)
        med2 = self.median(nums2)
        if med1 is None:
            med1 = med2
        if med2 is None:
            med2 = med1
        if med2 is None and med1 is None:
            med1 = 0
            med2 = 0
        med = (med1+med2)/2.0
        int_med = int(med)
        diff = med - int_med
        if diff != 0 and diff != 0.5:
            if diff > 0.5:
                med = int_med + 1.0
            else:
                med = int_med + 0.0

        return med

        # not in O(log(m+n))
        # let m be the length of nums1 and n the length of nums2
        # merge the lists
        # median def for l list of size k:
        # if k is odd take the element at position i = k/2
        # else take the average of elements in position k/2 - 0.5 and k/2 + 0.5
'''
[1,1]
[1,2]

[1,1]
[]
'''