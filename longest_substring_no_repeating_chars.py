#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        no repeating - dict/set 
        if we see a char in the dict record length, if it's longer than the current update it.
        then we need to update the dictionary - remove all the chars from the start_index of the substring up to the prev
        position of the repeating char if their position is before the prev pos and append the current, record the length as the
        current length minus teh number of ones being removed, and update the start index to be the prev pos + 1
        abcabcbb
        {a:0,b:1,c:2} cl = 3 pp = 0 si = 0 ml = 0
        {a:3,b:4,c:2} cl = 3 si = 1 ml = 3 

        "pwwkew"
        {w:2, k:3 e:4} cl ml

        '''
        max_length = 0
        char2pos = {}
        i = 0
        n = len(s)
        curr_length = 0
        start_index = 0
        while i < n:
            char = s[i]
            if char in char2pos:
                prev_pos = char2pos.get(char)
                n_removed = 0
                for j in xrange(start_index, prev_pos):
                    my_char = s[j]
                    my_pos = char2pos.get(my_char)
                    if my_pos <= j:
                        del char2pos[my_char]
                        n_removed = n_removed + 1
                if curr_length > max_length:
                    max_length = curr_length
                curr_length = curr_length - n_removed
                start_index = prev_pos + 1
            else:
                curr_length = curr_length + 1
            char2pos[char] = i
            i = i + 1
        if max_length < curr_length:
            max_length = curr_length
        return max_length