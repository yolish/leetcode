#https://leetcode.com/problems/array-partition-i/description/

class Solution(object):
    def description(self):
        return "Solution for the array partition I problem"
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_sum = 0
        for i in xrange(0, len(nums), 2):
            max_sum = max_sum + nums[i]
        return max_sum


