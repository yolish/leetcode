#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):

    def description(self):
        desc = "Solution for the median-of-two-sorted-arrays problem"
        return desc

    def get_median_elements(self, l, condition = None):
        median, median_elements, indices = None, None, None
        n = len(l)
        if n > 0:
            middle = n/2
            if condition is None:
                condition = n%2 == 1
            if condition:
                indices = [middle]
                median_elements = [l[middle]]
            else:
                if n%2 == 1: # external condition
                    indices = [middle-1, middle]
                    median_elements = [l[middle] , l[middle+1]]
                else:
                    indices = [middle - 1, middle]
                    median_elements = [l[middle - 1], l[middle]]
            median = sum(median_elements) / (len(median_elements) * 1.0)
        return median, median_elements, indices



    def split(self, l, indices, take_first_half):
        split_l = []
        if len(l) > 0:
            if take_first_half:
                split_l = l[0:(max(indices) + 1)]
            else:
                split_l = l[min(indices):len(l)]
        return split_l


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        med1, med_elem1, indices1 = self.get_median_elements(nums1)
        med2, med_elem2, indices2 = self.get_median_elements(nums2)

        if med1 is None or med2 is None:
            if med1 is None:
                median = med2
            else:
                median = med1
            if median is None:
                median = 0.0
            return median

        n = len(nums1)
        m = len(nums2)
        n_median_elem = int(1.0/((n+m)%2 + 1) * 2) # 1 for odd, 2 for even
        while n > 2 or m > 2:
            med1, med_elem1, indices1 = self.get_median_elements(nums1)
            med2, med_elem2, indices2 =  self.get_median_elements(nums2)
            nums1 = self.split(nums1, indices1, med1 >= med2)
            nums2 = self.split(nums2, indices2, med2 >= med1)
            n = len(nums1)
            m = len(nums2)
        # 2 <= n + m <= 4
        nums = sorted(nums1 + nums2)
        median, med_elem, indices = self.get_median_elements(nums, n_median_elem == 1)
        return median



