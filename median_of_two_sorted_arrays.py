#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):

    def get_median_elements(self, l):
        med_elem = []
        n = len(l)
        if n == 0:
            return med_elem
        if n % 2 == 1:
            med_elem.append(l[n / 2])
        else:
            middle = n / 2.0
            med_elem.append(l[int(middle - 0.5)])
            med_elem.append(l[int(middle + 0.5)])
        return med_elem


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        med_elem_1 = self.get_median_elements(nums1)
        med_elem_2 = self.get_median_elements(nums2)
        med_elem = self.get_median_elements(med_elem_1 + med_elem_2)
        if len(med_elem) == 0:
            median = 0.0
        else:
            median = mean(med_elem)

        return median
'''
[1,1]
[1,2]

[1,1]
[]
'''