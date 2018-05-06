#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):

    def description(self):
        desc = "Solution for the median-of-two-sorted-arrays problem"
        return desc

    def get_median(self, l, is_single_median = None, is_left_median = True):
        median = 0.0
        indices = None
        n = len(l)
        if n > 0:
            if is_single_median is None:
                is_single_median = n%2 == 1
            middle = n/2
            if is_single_median:
                indices = [middle]
            else:
                if is_left_median or n%2==0:
                    indices = [middle-1, middle]
                else:
                    indices = [middle, middle+1]
            median = sum([l[index] for index in indices]) / (len(indices) * 1.0)
        return median, indices



    def split(self, l, indices, take_first_half):
        k = len(l)
        if k > 2:
            if take_first_half:
                start_index = 0
                if k == 2:
                    end_index = (max(indices))
                else:
                    end_index = (max(indices)+1)
            else:
                end_index = len(l)
                if k == 2:
                    start_index = max(indices)
                else:
                    start_index = min(indices)
            l = l[start_index:end_index]

        return l


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        is_single_median = (m+n)%2 == 1
        med1, indices1 = self.get_median(nums1)
        med2, indices2 = self.get_median(nums2)
        is_left_median = True
        if n != m and (n+m)%2 == 0:
            if n < m:
                is_left_median = med1 <= med2
            else:
                is_left_median = med2 <= med1
        while m+n > 4:
            med1, indices1 = self.get_median(nums1)
            med2, indices2 =  self.get_median(nums2)
            nums1 = self.split(nums1, indices1, med1 >= med2)
            nums2 = self.split(nums2, indices2, med2 > med1)
            m = len(nums1)
            n = len(nums2)
        # 0 <= n + m <= 4
        print nums1
        print nums2
        nums = sorted(nums1 + nums2)
        median, indices = self.get_median(nums, is_single_median, is_left_median)
        return median



