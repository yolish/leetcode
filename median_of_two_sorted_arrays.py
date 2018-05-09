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
            m_orig = m
            n_orig = n
            med1, indices1 = self.get_median(nums1)
            med2, indices2 = self.get_median(nums2)
            med_of_med = (med1*m+med2*n)*1.0/(m+n)
            while m > 2 or n > 2:
                med1, indices1 = self.get_median(nums1)
                med2, indices2 = self.get_median(nums2)
                if med1 == med_of_med or med2 == med_of_med:
                    return med_of_med
                nums1 = self.split(nums1, indices1, med1 > med_of_med)
                nums2 = self.split(nums2, indices2, med2 > med_of_med)
                m = len(nums1)
                n = len(nums2)

            nums = nums1+nums2
            weights = m*[m_orig] + n*[n_orig]
            is_single_median = (m_orig + n_orig) % 2 == 1
            diff = [abs(elem - med_of_med) for elem in nums]
            sorted_diff = sorted(diff)
            candidates = []
            found_candidates = False
            for sval in sorted_diff:
                for i, val in enumerate(diff):
                    if val == sval:
                        candidates.append(i)
                    if len(candidates) == 2:
                        found_candidates = True
                        break
                if found_candidates:
                    break
            med1 = nums[candidates[0]]
            med2 = nums[candidates[1]]
            if not is_single_median:
                median = (med1+med2)/2.0
            else:
                w1 = weights[candidates[0]]
                w2 = weights[candidates[1]]
                med_of_candidates = (w1*med1+w2*med2)*1.0/(w1+w2)
                if med_of_candidates > med_of_med:
                    median = min(med1,med2)
                else:
                    median = max(med1, med2)
        return median*1.0




