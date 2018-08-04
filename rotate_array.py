class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        note1: take k to be k%n to deal with k >=n. only do if k%n > 0. note2: the item at index n-k will be te item at index 0 in the new array. Starting from this index we can get the new sequence. note 3: starting from i = 0 we can move in k steps and put item at index i in index i+k saving the value of the last one, until we get to 0 again. Set i to be n-k if k >= n
        brute force: start from old_index = (n-k) and advance by 1 each time for n and populating a separate list (appending
        the item). Note that when old_index == n-1 we need to reset it to zero
        improve O(1) space starting from i = 0 we can move in k steps and put item at index i in index i+k saving the value of the last one, until
         we get to 0 again (do it and then break). Set i to be k-n if k >= n and continuw for i = 1 ..k
        [1,2,3,4,5,6]
2
[1,2,3,4,5,6,7]
3

        '''
        n = len(nums)
        index_sum = (n - 1) * (n) / 2
        if n > 0:
            k = k % n
            if k > 0:
                for i in xrange(k):
                    prev_item = nums[i]
                    curr_index = i
                    next_index = curr_index + k
                    while next_index != i:
                        next_index = (curr_index + k)
                        if next_index >= n:
                            next_index = next_index - n
                        next_item = nums[next_index]
                        nums[next_index] = prev_item
                        prev_item = next_item
                        curr_index = next_index
                        if index_sum == 0:
                            break
                        index_sum = index_sum - next_index
                    if index_sum == 0:
                        break












