#https://leetcode.com/problems/plus-one/description/
class Solution(object):
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
