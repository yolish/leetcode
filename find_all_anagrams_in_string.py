#https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Solution(object):
    def encode_anagram(self, s):
        anagram = {}
        for char in s:
            char_count = anagram.get(char)
            if char_count is None:
                char_count = 0
            anagram[char] = char_count + 1
        return anagram

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        '''
        s: "cbaebabacd" p: "abc"
        n = 10 m = 3 

        '''

        indices = []
        n = len(s)
        m = len(p)
        if m <= n:
            if m == 1:
                i = 0
                for char in s:
                    if char == p:
                        indices.append(i)
                    i = i + 1
            else:
                p_anagram = self.encode_anagram(p)
                s_anagram = self.encode_anagram(s[0:m])
                i = m
                while True:
                    if p_anagram == s_anagram:
                        indices.append(i - m)
                    count = s_anagram.get(s[i - m])
                    if count is not None:
                        if count == 1:
                            del s_anagram[s[i - m]]
                        else:
                            s_anagram[s[i - m]] = count - 1

                    if i < n:
                        count = s_anagram.get(s[i])
                        if count is None:
                            count = 0
                        s_anagram[s[i]] = count + 1
                    else:
                        break
                    i = i + 1

        return indices


