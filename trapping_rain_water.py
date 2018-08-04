class Solution(object):
    def make_pass(self, height, trap, start_index, end_index, step, backward):
        n_units = 0
        max_val = height[start_index]
        for i in xrange(start_index + step, end_index, step):
            curr_val = height[i]
            if curr_val < max_val:
                if backward:
                    trap[i] = min(max_val - curr_val, trap[i])
                else:
                    trap[i] = max_val - curr_val
            else:
                max_val = curr_val
                if backward:
                    trap[i] = 0
            n_units = n_units + trap[i]
        return n_units

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        water are trapped when we see a decreasing sequence of heights and then and increasing until 
        the next decrease, the trapped water are the sum of diffs between the max height and the observed heights
        [0,1,0,2,1,0,1,3,2,1,2,1]
        edge cases: the last and first positions
        different approach: remember the last max, every position take the difference, and update if you see a new maximum

        '''

        n_units = 0
        n = len(height)
        print height
        trap = [0] * n
        if n > 2:
            # forward pass
            n_units = self.make_pass(height, trap, 0, n, 1, False)
            print trap
            # backward pass
            n_units = self.make_pass(height, trap, n - 1, 0, -1, True)
            print trap

        return n_units