#https://leetcode.com/problems/3sum/description/
'''
Key observations: we need to sort and then each time consider the rest of the array and
solve a two sum problem (generalized). To avoid duplicates, we need to remember the current value
and if it is the same skip it. In the twosum solution, we first populate a dictionary
(where the sum is now 0-currentval). To make sure we do not have duplicated triplets,
we need to store values to ignore (e.g. 0-1, 1-0 so we put the 1 in the ignore).
We also need to hold counts of values for edge cases where the sum is of two equal values (e.g 4,2,2)
to make sure we have enough instances and also deal with the special case of 0 (0,0,0).
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        triplets = []
        n = len(nums)
        if n > 2:
            curr_val = nums[0]
            nums.sort()
            val_counts = {}
            for val in nums:
                count = val_counts.get(val)
                if count is None:
                    count = 0
                val_counts[val] = count + 1
            for i in xrange(0, n - 1):
                val1 = nums[i]
                if i > 0 and curr_val == val1:
                    continue
                else:
                    curr_val = val1
                my_sum = 0 - val1  # get the required sum for the other two
                # twoSum generalized
                two_sum = {}
                for j in xrange(i + 1, n):
                    val2 = nums[j]
                    two_sum[val2] = my_sum - val2
                ignore_vals = set()
                for val2, val3 in two_sum.items():
                    if val2 not in ignore_vals and val3 in two_sum:
                        if (val2 != 0 and val2 == val3 and val_counts.get(val2) > 1) or val2 != val3 or (
                                val2 == 0 and val_counts.get(val2) > 2):
                            triplets.append([val1, val2, val3])
                            ignore_vals.add(val3)
        return triplets
