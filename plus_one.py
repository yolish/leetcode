#https://leetcode.com/problems/plus-one/description/
class Solution(object):
    def description(self):
        desc = "Solution to plus-one problem: iterate from right to left: if the digit " \
               "is smaller than 9 add 1 and break, otherwise set to zero and carry over. " \
               "If you reached the end with a carry over add '1' on the left side (begining of the array)."
        return desc
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        m = len(digits)
        for i in xrange(m):
            j = m - i - 1
            d = digits[j]
            if d < 9:
                digits[j] = d + 1
                break
            else:
                digits[j] = 0
                if j == 0:
                    digits[0:0] = [1]

        return digits
