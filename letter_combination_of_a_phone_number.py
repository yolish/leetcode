#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        '''
        thoughts:
        base case: one digit [2-9] -> ["a1","a2","a3"] 
        general case: [] + letterCombinations(s[1:])
        problem how to do the concatenation?
        also a lot of repeated calculations -> calls for DP
        start for the first and save each one
        then do the next and append it to every item in the saved list - but we don't have enough
        how many a1 will we have we'll need three for each letter that followes so 
        12
        a 
        for the kth position we'll need to duplicate each of the chars for 3^(n-k-1) and so on
        we'll create duplicates for each char and append it 
        but 7 and 9 are 4 sp it will need to calculate in advance and then divide each time 
        '''

        '''
        summary:
        Key observations: this is a DP problem.
        Base case: [“a1”, “a2”, “a3”] and then we need to call again with the rest.
        But we need to allocate new strings and we do a lot of repeated calculations -> DP.
        A key observation is that the number of combinations is:
        C = n1 x n2 x n3 x n4 .. where n_i is the length of the char group of the digit. Because they are not equal in length (some are three and some are four) we cannot summarize it with an equation.
        For the first digit we need to create  C’ = C/n1 strings for each of its associated chars.
        For digit_i that follows, we’ll append the associated chars with C’ = C’/n_i.
        Solution: hold dictionary that maps from digits to char group. Compute the number of combinations C.
        For the first digit, populate the list, adding each  char  C/n1 times. For all other position i, append each char for C’=C’/ni, while j < C (since str is immutable, this will be in practice creating a new string and assigning it to the jth position).
        Return the list of combinations

        '''

        combinations = []
        if len(digits) > 0:
            digits_to_char_group = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                                    "9": "wxyz"}

            # O(n) - calculate the number of combinations
            n_combinations = 1
            for d in digits:
                char_group = digits_to_char_group.get(d)
                n_combinations = n_combinations * len(char_group)
            n_duplicates = n_combinations
            # O(Nc), populate the combinations list with the first position
            char_group = digits_to_char_group.get(digits[0])
            n_duplicates = n_duplicates / len(char_group)
            for char in char_group:
                for i in xrange(n_duplicates):
                    combinations.append(char)

            for pos in xrange(1, len(digits)):
                char_group = digits_to_char_group.get(digits[pos])
                n_duplicates = n_duplicates / len(char_group)
                j = 0
                while j < n_combinations:
                    for char in char_group:
                        for i in xrange(n_duplicates):
                            combinations[j] = combinations[j] + char
                            j = j + 1
        return combinations