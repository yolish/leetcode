#https://leetcode.com/problems/rotate-image/description/
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''
        observations
        n%2 == 0 -> everyone move
        n%2 == 1 -> everyone move apart from mid,mid mid = n/2
        jth column becomes jth row
        ith row becomes n-i-1-th colum
        (i,j) -> (j,n-i-1) 
        not symmetric - each time we touch 4 elements that rotate: 
        (i,j)->(j,n-i-1)
        (j,n-i-1)->(n-i-1,n-j-1)
        (n-i-1,n-j-1)->(n-j-1,n-(n-i-1)-1) = (n-j-1,i)
        (n-j-1,i)->(i,j)
        we do that for j = i .. (n-i-1)-1
        '''

        n = len(matrix)
        if n > 0:
            for i in xrange(n):
                j = i
                while j < n - 1 - i:
                    temp1 = matrix[i][j]
                    temp2 = matrix[j][n - i - 1]
                    temp3 = matrix[n - i - 1][n - j - 1]
                    matrix[i][j] = matrix[n - j - 1][i]
                    matrix[j][n - i - 1] = temp1
                    matrix[n - i - 1][n - j - 1] = temp2
                    matrix[n - j - 1][i] = temp3
                    j = j + 1
