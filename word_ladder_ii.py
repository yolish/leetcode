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
               " Then find the shortest paths from the source to the target using a generalized version of " \
               " Dijkstra's algorithm followed by a recursive method to construct the paths."
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

    def construct_paths(self, tree, source, u, curr_path, paths, verbose):
        my_path = curr_path[:]
        prev = tree.get(u)
        if source in prev:
            curr_path.append(source)
            paths.append(curr_path)
            if verbose:
                print("path added: {}".format(curr_path))
        else:
            for v in prev:
                prev_of_last = tree.get(curr_path[-1])
                if curr_path[-1] != source and v in prev_of_last:
                    curr_path.append(v)
                    if verbose:
                        print("extending an existing path: {}".format(curr_path))
                else:
                    # starting a new path
                    i = my_path.index(u)
                    curr_path = my_path[0:i + 1]
                    if verbose:
                        print("starting a new path: {} and adding node {}".format(curr_path, v))
                    curr_path.append(v)
                    # recursive call to extend the path
                self.construct_paths(tree, source, v, curr_path, paths, verbose)


    def find_shortest_paths(self, graph, source, target, verbose=False):
        vertex_set = graph.keys()
        max_length_path = len(vertex_set)+1
        dist_to_source = {}
        prev_in_path = {}
        for v in vertex_set:
            prev_in_path[v] = []
            dist_to_source[v] = max_length_path

        prev_in_path[source].append(source)
        dist_to_source[source] = 0

        while len(vertex_set) > 0:
            min_dist = min([dist_to_source[v] for v in vertex_set])
            closest_vertices = [v for v in vertex_set if dist_to_source[v] == min_dist]
            #if target in closest_vertices:
            #    break
            for u in closest_vertices:
                vertex_set.remove(u)
            for u in closest_vertices:
                alt_dist = min_dist + 1
                neighbors = graph.get(u)
                for v in neighbors:
                    dist_v = dist_to_source.get(v)
                    if dist_v >= alt_dist:
                        dist_to_source[v] = alt_dist
                        prev_in_path[v].append(u)
        if verbose:
            print("shortest paths tree:\n {}".format(prev_in_path))
        curr_path = [target]
        paths = []
        self.construct_paths(prev_in_path, source, target, curr_path, paths, verbose)
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






