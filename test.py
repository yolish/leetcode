import word_ladder_ii


def test_solution(solution, test_set, description):
    print(description)
    for i, test_case in enumerate(test_set):
        print("Test case {}:".format(i))
        print(test_case)
        print("Solution:")
        print(solution(*test_case))


test_set = [
    ["hit","cog",["hot","dot","dog","lot","log","cog"]],
    ["hit", "cog", ["hot","dot","dog","lot","log"]],
["hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"]]
]
test_set = [test_set[2]]
solution = word_ladder_ii.Solution()
test_solution(solution.findLadders, test_set, solution.description())




