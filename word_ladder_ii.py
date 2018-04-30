#https://leetcode.com/problems/word-ladder-ii/description/
'''
Notes:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''
class Solution(object):

    def description(self):
        desc = "Solution to word-ladder-ii: " \
               "First, create a graph whose vertices are the words in the list and the begin word." \
               " Add an edge between two vertices if they are a 1-letter transformation of one another." \
               " Then find the shortest paths from the source to the target."
        return desc

    def is_transformation_of(self, word1, word2):
        """
        check if word2 is a transformation of word1
        :type word1: str
        :type word2: str
        :rtype bool
        """
        is_transformation = False
        n = len(word1)
        distance = 0
        for i in xrange(n):
            if word1[i] != word2[i]:
                distance = distance+1
            if distance > 1:
                break
        if distance == 1:
            is_transformation = True
        return is_transformation

    def recover_paths(self, graph, u, source, paths, curr_path, max_path_length):
        if u == source or len(curr_path) >= max_path_length:
            return
        my_path = curr_path[:]

        neighbors = graph.get(u)
        if neighbors is not None:
            if source in neighbors: #we made it to the source
                curr_path.append(source)
            else:
                for v in neighbors:
                    others = graph.get(v)
                    # we need to start a new path if we've reached the source or a dead end
                    if curr_path[-1] != source and curr_path[-1] in others:
                        if v not in curr_path: # eliminate cycles
                            curr_path.append(v)
                            self.recover_paths(graph, v, source, paths, curr_path, max_path_length)

                    else:
                        # starting a new path
                        i = my_path.index(u)
                        curr_path = my_path[0:i+1]
                        if v not in curr_path:  # eliminate cycles
                            curr_path.append(v)
                            paths.append(curr_path)
                            # recursive call to extend the path
                            self.recover_paths(graph, v, source, paths, curr_path, max_path_length)



    def find_shortest_paths(self, graph, source, target):
        max_path_length = len(graph.keys())+1
        curr_path = [target]
        paths = [curr_path]
        self.recover_paths(graph, target, source, paths, curr_path, max_path_length)
        print(graph)
        print(paths)
        #filter invalid paths
        paths = [p for p in paths if (p[-1] == source and p[0] == target)]
        #find the minimal length
        min_length = len(graph.keys())+1
        for p in paths:
            path_length = len(p)
            if path_length <= min_length:
                min_length = path_length
        # take the shortest paths and reverse them
        paths = [p for p in paths if len(p) <= min_length]
        for p in paths:
            p.reverse()
        return paths

    def findLadders(self, begin_word, end_word, word_list): # name of function is dictated
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: List[str]
        :rtype: List[List[str]]
        """

        shortest_transformations = []
        if end_word in word_list:
            # build the an undirected  graph with nodes as the word list and the begin word
            # with an edge between word w1 and
            # word w2 if w1 if they are a transformation of each other
            transformations_graph = {}
            #word_list = word_list[:] uncomment to avoid changing the word list
            if begin_word not in word_list:
                word_list.append(begin_word) # add the begin word
            n = len(word_list)
            for i in xrange(n-1):
                for j in xrange((i+1), n):
                    w1 = word_list[i]
                    w2 = word_list[j]
                    if self.is_transformation_of(w1, w2):
                        w1_transformations = transformations_graph.get(w1)
                        if w1_transformations is None:
                            transformations_graph[w1] = [w2]
                        else:
                            w1_transformations.append(w2)
                        w2_transformations = transformations_graph.get(w2)
                        if w2_transformations is None:
                            transformations_graph[w2] = [w1]
                        else:
                            w2_transformations.append(w1)
            # find all shortest paths from begin word to end word
            if transformations_graph.get(begin_word) is not None \
                    and transformations_graph.get(end_word) is not None:
                shortest_transformations = self.find_shortest_paths(transformations_graph,
                                                                    begin_word, end_word)

        return shortest_transformations






