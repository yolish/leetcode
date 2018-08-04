#https://leetcode.com/problems/product-of-array-except-self/description/
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        if we were permitted to use division this is simply calculating the product P and then putting in the ith position
        P/a[i]
        but we are not.. so 
        key observation: p[i] = productExceptSelf(nums[0..i-1])*productExceptSelf(nums[i+1..n-1])
        base case: n==1 productExceptSelf(nums) = [1] # KEY (it means that in a[0] and b[n-1] we'll put 1)
        a lot of excessive calculations -> DP
        without space considerations:
        allocate a = [1,1,..1]
        allocate a go through the array and store a running product so that a[i] = productExceptSelf(nums[0..i-1])
        then do it again but from the end and muliply by the ith position.

        '''
        n = len(nums)
        p = nums[0]
        a = [1] * n
        for i in xrange(1, n):
            temp = nums[i]
            a[i] = p
            p = p * temp
        p = nums[n - 1]
        for i in xrange(n - 2, -1, -1):
            temp = nums[i]
            a[i] = p * a[i]
            p = p * temp
        return a