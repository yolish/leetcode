#https://leetcode.com/problems/kth-largest-element-in-an-array/description/
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        sort and take the n-k element, n being the length of the list 
        '''
        nums.sort()
        n = len(nums)
        return nums[n - k]

        '''
        max and remove when we get to the count return it 

        n_count = 0
        while n_count < k:
            x = max(nums)
            n_count = n_count + 1
            if n_count == k:
                break
            nums.remove(x)
        return x
        '''
