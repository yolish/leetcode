#https://leetcode.com/problems/power-of-two/
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            is_power_of_two = False
        else:
            is_power_of_two = True
            while n > 1:
                if n%2 == 1:
                    is_power_of_two = False
                    break
                else:
                    n = n/2
        return is_power_of_two