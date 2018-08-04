class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''
        dictionary
        we see a value, if it is not in the dictionary we put abs(val-k)-val and (val+k)-val in the dictionary
        otherwise, we add the pairs. 
        To make sure we do not have repeated pairs, we hold another dictionary with the elements we already added to the pair set and consider them, only if they are not there
        '''
        diffs = {}
        elems = set()
        pairs = []
        for n in nums:
            if n not in elems:
                elems.add(n)
                if e not in diffs:
                    e1 = abs(n - k)
                    e2 = k + n
                    diffs[e1] = n
                    diffs[e2] = n
                else:
                    pairs.append([n, diffs.get(n)])
        return pairs


