class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        '''
        2^10 = 1024
        2^20 = 1024*1024 > 100000 so it's enough to hold the primes up to 23
        we can calculate the representation of L and the number of bits in L, and then simply add 1 and update accordingly.
        For each sum that is in the prime set we hold, we increment the counter

        4,8
        4 [0,0,1,0] bit_sum = 1 n_int_with_prime_bits = 0 
        5 [1,0,1,0] bit_sum = 2 n_int_with_prime_bits = 1 
        6 [0,1,1,0] bit_sum = 2 n_int_with_prime_bits = 2 
        7 [1,1,1,0] bit_sum = 3 n_int_with_prime_bits = 3
        8 [0,0,0,1] bit_sum = 1 n_int_with_prime_bits = 3


        '''
        n_int_with_prime_bits = 0
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])
        n_bits = R.bit_length()
        bits = [0] * n_bits  # right to left representation 8: [0,0,0,1]
        diff = R - L
        # calculate the L's bits sum and the binary representation
        i = 0
        bits_sum = 0
        while L > 0:
            bit_val = L % 2
            bits[i] = bit_val
            L = L / 2
            i = i + 1
            bits_sum = bits_sum + bit_val
        if bits_sum in primes:
            n_int_with_prime_bits = n_int_with_prime_bits + 1
        # add 1 and update the sum, then check if it is in the primes set and increment the counter if required
        for i in xrange(diff):
            for k in xrange(n_bits):
                if bits[k] == 0:
                    bits[k] = 1
                    bits_sum = bits_sum + 1
                    break
                else:
                    bits[k] = 0
                    bits_sum = bits_sum - 1
            if bits_sum in primes:
                n_int_with_prime_bits = n_int_with_prime_bits + 1
        return n_int_with_prime_bits