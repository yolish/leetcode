#https://leetcode.com/problems/jewels-and-stones/description/

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
