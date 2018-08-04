class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        '''
        smells like a DP problem
        [10, 15, 20, 30, 1, 15, 20]
        10  10+15 or 10+20  
        15  15+20 end


        10 + [15,...]
        10 + [20 + ...]
        [10, 15, 3, 2, 6, 7]
        10 [3,2,6,7] -> 10 + 8 = 18
        15 [2,6,7] 15 + 6 = 21


        n=1 0
        n=2 0 or 1
        n=3 0,2 or 1
        n=4 0,2 or 1,3 or 1,2
        n=5 0,2,4 or 1,3 or 0,2,3 or 1,2,4
        n=6 1,3,5 1,2,4, 1,3,4

        [20] = 0

        '''

        class Solution(object):

            def minCostClimbingStairs(self, cost):
                """
                :type cost: List[int]
                :rtype: int
                """

                n = len(cost)
                window = [cost[0], cost[1], 0]
                if n > 2:
                    for i in xrange(2, n):
                        if window[0] > window[1]:
                            curr_cost = window[1] + cost[i]
                        else:
                            curr_cost = window[0] + cost[i]

                        window[0] = window[1]
                        window[1] = curr_cost

                min_cost = min(window[0], window[1])
                return min_cost







