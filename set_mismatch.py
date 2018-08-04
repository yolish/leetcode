class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        observation the sum of the numbers in the correct set will is S = (1+n)*n/2 
        in the errornous set it will be S' = S + a_repeat - a_missing 
        so S-S' = S-(S+a_repeat-a_missing) -> S-S' = a_missing - a_repeat -> a_missing = S-S'+a_repeat
        we find a_repeat by holding a dictionary and once the count > 1 breaking and taking it.
        Then we can find a_missing by placing a_repeat in the above equation
        '''
        n = len(nums)
        s = (n+1)*n/2
        items = set()
        s_error = sum(nums)
        repeat = 0
        for x in nums:
            if x in items:
                repeat = x
                break
            items.add(x)
        missing = s-s_error+repeat
        return [repeat,missing]