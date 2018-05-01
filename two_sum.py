#https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def description(self):
        desc = "Solution to the two-sum problem: sort the array, then traverse" \
               " for each element e1 the remaining array until" \
               " you you see an element e2 > target -e1. " \
               "Return the first pair which gives e1+e2 = target."
        return desc
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sorted_nums = sorted(nums)
        n = len(nums)
        found_two_sum = False
        for i in xrange(n - 1):
            n1 = sorted_nums[i]
            for j in xrange(i + 1, n):
                n2 = sorted_nums[j]
                if n1 + n2 == target:
                    found_two_sum = True
                    break
                elif n2 > target-n1:
                    break
            if found_two_sum:
                break
        i_orig = nums.index(sorted_nums[i])
        j_orig = nums.index(sorted_nums[j])
        if i_orig == j_orig:
            temp = nums[i_orig]
            nums[i_orig] = temp + 1
            j_orig = nums.index(sorted_nums[j])
            nums[i_orig] = temp
        return [i_orig,j_orig]

    def naive_two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        found_two_sum = False
        for i in xrange(n-1):
            for j in xrange(i+1,n):
                if nums[i]+nums[j] == target:
                    found_two_sum = True
                    break
            if found_two_sum:
                break
        return [i,j]
