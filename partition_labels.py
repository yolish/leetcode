#https://leetcode.com/problems/partition-labels/
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        '''
        observation:
        for a char c, if i is the first index it appears and j is the last, then c must be in th group start starts at k <= i and end at l >= j
        a=>0,7
        b=>1,5
        c=>4,8
        d=>...

         find a group if that overlaps contains add to it otherwise, create a group of your own.
         KEY NOTE: needs to be by order! so we need to traverse the dictionary by order of strings
         "ababcadefegdehijhklij"

        '''
        indices = {}
        i = 0
        for char in S:
            my_indices = indices.get(char)
            if my_indices is None:
                indices[char] = [i, i]
            else:
                my_indices[1] = i
            i = i + 1

        groups = []
        for char in S:
            my_indices = indices.get(char)
            if my_indices is not None:
                start_index = my_indices[0]
                end_index = my_indices[1]
                create_group = True
                for g in groups:
                    g_start_index = g[0]
                    g_end_index = g[1]
                    if (start_index >= g_start_index and start_index <= g_end_index) or (
                            end_index >= g_start_index and end_index <= g_end_index):
                        g[0] = min(g_start_index, start_index)
                        g[1] = max(g_end_index, end_index)
                        create_group = False
                        break
                if create_group:
                    groups.append([start_index, end_index])
                del indices[char]

        sizes = []
        for g in groups:
            sizes.append(g[1] - g[0] + 1)

        return sizes