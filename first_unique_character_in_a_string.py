#https://leetcode.com/submissions/detail/163778609/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_unique_index = -1
        char_counts = {}
        for char in s:
            count = char_counts.get(char)
            if count is None:
                count = 0
            char_counts[char] = count + 1

        for i, char in enumerate(s):
            if char_counts.get(char) == 1:
                first_unique_index = i
                break

        return first_unique_index