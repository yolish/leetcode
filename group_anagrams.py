#https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        hold a dictionary 'sorted anagram'-> list of anagrams
        sort - if in dictionary append to value
        else create a key-value pair: sorted->[item]
        return the values of the dictionary
        O(n*(mlogm)) time
        """
        anagrams = {}
        for s in strs:
            key = "".join(sorted(s))
            group = anagrams.get(key)
            if group is None:
                anagrams[key] = [s]
            else:
                group.append(s)
        return anagrams.values()
