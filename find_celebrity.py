#https://leetcode.com/problems/find-the-celebrity/description/
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        my_celeb = -1
        not_celebs = set()
        i = 0
        while i < n:
            if i not in not_celebs:
                is_celeb = True
                for j in xrange(n):
                    if j != i:
                        if knows(i, j):
                            not_celebs.add(i)
                            is_celeb = False
                            break
                        else:
                            not_celebs.add(j)
                            if not knows(j, i):
                                not_celebs.add(i)
                                is_celeb = False
                                break
                if is_celeb:
                    my_celeb = i
                    break
            i = i + 1
        return my_celeb

