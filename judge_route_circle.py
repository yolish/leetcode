#https://leetcode.com/problems/judge-route-circle/description/
class Solution(object):
    def description(self):
        return "Solution to the judge route circle problem"

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        made_circle = False
        move_count = {"U":0, "D":0, "L":0, "R":0}
        for m in moves:
            move_count[m] = move_count.get(m) + 1
        if move_count.get("U") - move_count.get("D") == 0 and move_count.get("R") - move_count.get("L") == 0:
            made_circle = True

        '''
        # another valid solution:
        original_pos = [0,0]
        for m in moves:
            if m == "U":
                original_pos[1] = original_pos[1]+1
            elif m=="D":
                original_pos[1] = original_pos[1]-1
            elif m=="R":
                original_pos[0] = original_pos[0]+1
            elif m=="L":
                original_pos[0] = original_pos[0]-1
        if original_pos[0] == 0 and original_pos[1] == 0:
            made_circle = True
        '''

        return made_circle



