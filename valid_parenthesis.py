#https://leetcode.com/problems/valid-parentheses/description/
'''
brute-force: create a dictionary with keys as the closing signs and values as the opening signs
go the chars given string and use them as keys to the dictionary. If the char is not a key, then it is an opening sign – push it to a stack, if it is, the last element in the stack should be its matching opening sign – if it is not break and return invalid if it is remove it from the stack.
Improve: if the length of the string is an odd number return invalid (no need to check content)

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        is_valid = True
        close_open_pairs = {"}": "{", "]": "[", ")": "("}
        my_stack = []
        for s1 in s:
            s2 = close_open_pairs.get(s1)
            if s2 is None:  # s1 is an openning sign
                my_stack.append(s1)
            else:
                n = len(my_stack)
                if n == 0 or my_stack[n - 1] != s2:
                    is_valid = False
                    break
        return is_valid and len(my_stack) == 0
