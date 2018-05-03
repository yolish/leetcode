#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):

    def description(self):
        desc = "Solution for the median-of-two-sorted-arrays problem: while both arrays are not empty" \
               "take their median d1, d2. If d1 equals d2 return d1, if both arrays are of size 1 return the mean of d1 and 2." \
               "otherwise continue with the respective half of each array, taking the first/second half for the " \
               "larger/smaller median. " \
               "Once stopped, if both lists are empty return 0.0 otherwise return the median of the" \
               "non empty array. Time complexity O(log(m+n))"
        return desc



    def get_median(self, l):
        median, indices = None, None
        n = len(l)
        if n > 0:
            if n % 2 == 1:
                i = n / 2
                indices = [i]
                median = l[i]*1.0
            else:
                middle = n / 2.0
                i1 = int(middle - 0.5)
                i2 = int(middle + 0.5)
                median = (l[i1] + l[i2])/2.0
                indices = [i1, i2]
        return median, indices

    def split(self, l, indices, take_first_half):
        split_l = []
        if len(l) > 0:
            if take_first_half:
                split_l = l[0:(min(indices) + 1)]
            else:
                split_l = l[max(indices):len(l)]
        return split_l


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        while n > 0 and m > 0:
            med1, indices1 = self.get_median(nums1)
            med2, indices2 = self.get_median(nums2)
            if med1 == med2:
                return med1
            if n == 1 and m == 1:
                return (med1 + med2)/2.0
            take_first_half = med1 > med2
            nums1 = self.split(nums1, indices1, take_first_half)
            nums2 = self.split(nums2, indices2, not take_first_half)
            n = len(nums1)
            m = len(nums2)

        if len(nums1) == 0 and len(nums2) == 0:
            median = 0.0
        else:
            if len(nums1) == 0:
                median, indices = self.get_median(nums2)
            else:
                median, indices = self.get_median(nums1)
        return median


