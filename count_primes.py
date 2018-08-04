#https://leetcode.com/problems/count-primes/description/
'''
Count the number of prime numbers less than a non-negative number, n.
brute force: go through i in  0 to n-1, increase counter if I is a prime number. is_prime goes through j in 0 to i and breaks if i is dividable by j (i%j==0)
O(n*n) time, O(1) space
Improve 1: same as 1 but we only go through j in o to sqrt(i) (more than that is redundant)
O(n*sqrt(n)) time, O(1) space
Improve 2: create a set with 2 to n-1. For i in 2 to sqrt(n), go through ith multiplication that are < n and remove them from the set. Return the length of the set –
n/2 + n/3 + … n/sqrt(n) – O(n) but also O(n) space complexity
'''


class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        else:
            primes = [2, 3]
            x = 5
            for x in xrange(x, n, 6):
                for p in primes:
                    if p * p > x:
                        primes.append(x)
                        break
                    else:
                        if x % p == 0:
                            break
                y = x + 2
                if y < n:
                    for p in primes:
                        if p * p > y:
                            primes.append(y)
                            break
                        else:
                            if y % p == 0:
                                break

            n_primes = len(primes)

        return n_primes


'''
    def is_prime(self, i):
        prime = True
        if i < 2:
            prime = False
        else:
            upper_bound = int(math.sqrt(i)) + 1
            for j in xrange(2, upper_bound):
                if i%j == 0:
                    prime = False
                    break
        return prime


    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_primes = 0
        for i in xrange(n):
            if self.is_prime(i):
                n_primes = n_primes + 1
        return n_primes

'''

