#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#import numpy as np
#import math

class Solution(object):

    def description(self):
        desc = "Solution for the median-of-two-sorted-arrays problem"
        return desc

    def get_median(self, l):
        median = 0.0
        indices = None
        n = len(l)
        if n > 0:
            middle = n/2
            if n%2 == 1:
                indices = [middle]
            else:
                indices = [middle-1, middle]
            median = sum([l[index] for index in indices]) / (len(indices) * 1.0)
        return median, indices

    def split(self, l, indices, take_first_half):
        k = len(l)
        if k > 2:
            if take_first_half:
                start_index = 0
                end_index = (max(indices)+1)
            else:
                start_index = min(indices)
                end_index = len(l)
            l = l[start_index:end_index]
        return l

    def update_n_smaller(self, n_smaller_than, nums, indices, n):
        shift = 0
        if len(indices) == 2:
            shift = 1
        for i, index in enumerate(indices):
            val = nums[index]
            my_n_elem = n/2+i-shift
            n_elem =  n_smaller_than.get(val)
            if  n_elem is None:
                n_smaller_than[val] = my_n_elem
            else:
                n_smaller_than[val] = max(n_elem, my_n_elem)


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        #mtrue= np.median(sorted(nums1 + nums2))
        #print mtrue
        if m==0:
            median, indices = self.get_median(nums2)
        elif n==0:
            median, indices = self.get_median(nums1)
        else:
            k = m+n
            med1, indices1 = self.get_median(nums1)
            med2, indices2 = self.get_median(nums2)
            n_smaller_than = {}
            self.update_n_smaller(n_smaller_than, nums1, indices1, m)
            self.update_n_smaller(n_smaller_than, nums2, indices2, n)
            med_of_med =(med1*m+med2*n)*1.0/(m+n)
            while m+n > 4:
                med1, indices1 = self.get_median(nums1)
                med2, indices2 = self.get_median(nums2)
                nums1 = self.split(nums1, indices1, med1 > med_of_med)
                nums2 = self.split(nums2, indices2, med2 > med_of_med)
                self.update_n_smaller(n_smaller_than, nums1, indices1, m)
                self.update_n_smaller(n_smaller_than, nums2, indices2, n)
                m = len(nums1)
                n = len(nums2)
            median = None
            nums = sorted(nums1+nums2)
            last_n_smaller = 0
            is_single_median = k%2 == 1
            for val1 in nums1:
                for val2 in nums2:
                    val_to_update = None
                    if val1 > val2:
                        val_to_update = val1
                    elif val2 >= val1:
                        val_to_update = val2
                    if val_to_update is not None:
                        n_elem = n_smaller_than.get(val_to_update)
                        if n_elem is None:
                            n_smaller_than[val_to_update] = 1
                        else:
                            n_smaller_than[val_to_update] = n_elem+1
            for i, val in enumerate(nums):
                n_elem_smaller_than = n_smaller_than.get(val)
                if n_elem_smaller_than is not None and n_elem_smaller_than > 0:
                    last_n_smaller = n_elem_smaller_than + last_n_smaller
                else:
                    if i > 0:
                        last_n_smaller = last_n_smaller + 1
                if i > 0:
                    if is_single_median and last_n_smaller >= (k/2):
                            median = val
                            break
                    if not is_single_median and last_n_smaller >= k/2 -1:
                            if i < len(nums)-1:
                                median = (val + nums[i+1])/2.0
                            else:
                                median = (val + nums[i-1])/2.0
                            break
            if median is None:
                median, indices = self.get_median(nums)

        return median*1.0
