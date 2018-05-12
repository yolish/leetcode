#https://leetcode.com/problems/number-of-lines-to-write-string/description/

class Solution(object):
    def description(self):
        return "Solution for the number of lines to write string problem"

    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """

        if len(S) == 0:
            return [0,0]

        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alphabet_width = {}
        for i, char in enumerate(alphabet):
            alphabet_width[char] = widths[i]
        num_of_lines = 1
        curr_line_width = 0
        for char in S:
            my_width = alphabet_width.get(char)
            if curr_line_width + my_width > 100:
                num_of_lines = num_of_lines + 1
                curr_line_width = my_width
            else:
                curr_line_width = curr_line_width + my_width

        return [num_of_lines, curr_line_width]