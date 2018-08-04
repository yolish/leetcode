class Solution(object):
    def is_palindrome(self, s):
        n = len(s)
        palindrome = True
        if n > 1:
            for i in xrange(n / 2):
                if s[i] != s[n - i - 1]:
                    palindrome = False
        return palindrome

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome_set = set()
        longest_palindrome = ""
        n = len(s)
        if n >= 1:
            palindrome_set.add(s[0])
            for i in xrange(1, n):
                curr_palindrome = palindrome_set.pop()
                curr_len = len(curr_palindrome)
                j = min(n - i, i)
                start_index = i - j
                end_index = i + j
                while start_index >= 0 and end_index <= len(s) and end_index + 1 - start_index > curr_len:

                    # char is mid point(odd palindrome)
                    candidate = s[start_index:end_index + 1]
                    if self.is_palindrome(candidate):
                        curr_palindrome = candidate
                        curr_len = len(curr_palindrome)
                        break
                    # mid point is between chars (even palindrome)
                    candidate = s[start_index:end_index]
                    if self.is_palindrome(candidate):
                        curr_palindrome = candidate
                        curr_len = len(curr_palindrome)
                        break
                    j = j - 1
                    start_index = i - j
                    end_index = i + j
                palindrome_set.add(curr_palindrome)

        if len(palindrome_set) > 0:
            longest_palindrome = palindrome_set.pop()
        return longest_palindrome