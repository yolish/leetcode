#import math
class Solution(object):
    def description(self):
        return "Solution to the hamming distance problem"

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        s = bin(x^y)

        diff_char = "1"
        distance = 0
        for char in s:
            if char == diff_char:
                distance = distance + 1
        '''
        #slower solution
        distance = 0
        i = int(s, 2)
        while i > 0:
            power_of_two = int(math.log(i,2))
            i = i - math.pow(2, power_of_two)
            distance = distance + 1

        '''
        return distance

