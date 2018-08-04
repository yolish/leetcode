#https://leetcode.com/problems/jewels-and-stones/description/

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counts = {}
        for char in S:
            my_count = counts.get(char)
            if my_count is None:
                my_count = 0
            counts[char] = my_count + 1

        n_jewels = 0
        for char in J:
            my_count = counts.get(char)
            if my_count is not None:
                n_jewels = n_jewels + my_count

        return n_jewels

'''
class Solution(object):
    def description(self):
        return "Solution to the jeweles and stones problem"

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n_jweles_in_stones = 0
        # generate a jewel dictionary
        jewel_dict = {}
        for jewel in J:
            jewel_dict[jewel] = 1
        # traverse S and check for each stone if it is a jewel or not (i.e whether it is in the dictionary)
        for stone in S:
            if jewel_dict.get(stone) is not None:
                n_jweles_in_stones = n_jweles_in_stones + 1

        return n_jweles_in_stones

'''
