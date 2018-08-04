#https://leetcode.com/submissions/detail/163606204/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        is_anagram = True
        if len(s) == len(t):
            encoding = {}
            for char in s:
                count = encoding.get(char)
                if count is None:
                    count = 0
                encoding[char] = count + 1
            for char in t:
                count = encoding.get(char)
                if count is None:
                    is_anagram = False
                    break
                else:
                    if count == 1:
                        del encoding[char]
                    else:
                        encoding[char] = count - 1
        else:
            is_anagram = False

        return is_anagram and len(encoding) == 0
