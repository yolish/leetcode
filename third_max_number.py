class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        max, remove, max remove max remove until it is empty, need to save the last max in case we have 
        repeated elements and also a counter

        [1,2,2,4]
        4, 1
        [1,2,2]
        2, 2
        [1,2]
        2, 2
        [1]
        1, 3

        improve: use the slice

        '''

        max_elem = max(nums)
        first_max_elem = max_elem
        nums.remove(max_elem)
        n_max = 1
        while len(nums) > 0:
            curr_max = max(nums)
            nums.remove(curr_max)
            if curr_max != max_elem:
                n_max = n_max + 1
            if n_max == 3:
                break
            max_elem = curr_max

        if n_max == 3:
            return curr_max
        else:
            return first_max_elem
