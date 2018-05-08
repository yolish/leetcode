#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

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

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m==0:
            median, indices = self.get_median(nums2)
        elif n==0:
            median, indices = self.get_median(nums1)
        else:
            is_single_median = (m+n)%2 == 1
            med1, indices1 = self.get_median(nums1)
            med2, indices2 = self.get_median(nums2)
            med_of_med = (med1*m+med2*n)/(m+n)
            while m > 2 or n > 2:
                med1, indices1 = self.get_median(nums1)
                med2, indices2 = self.get_median(nums2)
                nums1 = self.split(nums1, indices1, med1 > med_of_med)
                nums2 = self.split(nums2, indices2, med2 > med_of_med)
                m = len(nums1)
                n = len(nums2)

            nums = sorted(nums1+nums2)
            median, indices = self.get_median(nums)
            if is_single_median and len(nums)%2 == 0:
                diff1 = abs(nums[indices[0]]-med_of_med)
                diff2 = abs(nums[indices[1]]-med_of_med)
                if diff1 < diff2:
                    median = nums[indices[0]]
                else:
                    median = nums[indices[1]]
            elif not is_single_median and len(nums)%2 == 1:
                diff = [abs(elem-med_of_med) for elem in nums]
                sorted_diff = sorted(diff)
                indices = []
                found_indices = False
                for sval in sorted_diff:
                    for i, val in enumerate(diff):
                        if val == sval:
                            indices.append(i)
                        if len(indices) == 2:
                            found_indices = True
                            break
                    if found_indices:
                        break
                median_elems = [nums[index] for index in indices]
                median = sum(median_elems)/2.0
        return median*1.0



