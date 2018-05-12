#https://leetcode.com/problems/self-dividing-numbers/description/

class Solution(object):
    def description(self):
        return "Solution to the self-dividing numbers problem"

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_dividing_nums = []
        for num in xrange(left, right+1):
            s = str(num)
            self_dividing = True
            for char in s:
                digit = int(char)
                if digit == 0 or num%digit != 0:
                    self_dividing = False
                    break
            if self_dividing:
                self_dividing_nums.append(num)

        return self_dividing_nums



