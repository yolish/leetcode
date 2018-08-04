#https://leetcode.com/problems/most-common-word/description/
'''
Get list of word  from the paragraph using re.findall.
for each word use its lower case version and add it to a dictionary with count 1
or increase the count by 1 if it’s already in the dictionary.
Then go the items of the dictionary and get the word with the maximal count which is not in the banned list.
Complexity O(n), n the number of (case sensitive unique) words in the paragraph

'''
import re
class Solution(object):

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        words = re.findall(r'\w+', paragraph)

        word_count = {}
        for w in words:
            w_lower = w.lower()
            count = word_count.get(w_lower)
            if count is None:
                count = 0
            word_count[w_lower] = count + 1

        max_count = 0
        most_common_word = None
        for w, count in word_count.items():
            if count > max_count and w not in banned:
                max_count = count
                most_common_word = w

        return most_common_word
