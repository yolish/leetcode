import word_ladder_ii


def test_solution(solution, test_set, description):
    print(description)
    for i, test_case in enumerate(test_set):
        print("Test case {}:".format(i+1))
        print(test_case)
        print("Solution:")
        print(solution(*test_case))


test_set = [
    ["hit","cog",["hot","dot","dog","lot","log","cog"]],
    ["hit", "cog", ["hot","dot","dog","lot","log"]],
["hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"]],
    ["hot","dog",["hot","dog","cog","pot","dot"]],
    ["red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]]
]
'''
Output:
[["red","ted","tex","tax"],["red","ted","tad","tax"]]
Expected:
[["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
'''

test_set = [test_set[-1]]
solution = word_ladder_ii.Solution()
test_solution(solution.findLadders, test_set, solution.description())




