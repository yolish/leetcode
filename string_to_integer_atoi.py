#
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        INT_MAX = 2147483647  # pow(2,31)-1
        str_to_int = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        my_int = 0
        my_sign = 1
        skip_space = True
        for ch in str:
            if ch == " " and skip_space:
                continue
            else:
                if skip_space and (ch == "-" or ch == "+"):
                    if ch == "-":
                        my_sign = -1
                else:
                    my_digit = str_to_int.get(ch)
                    if my_digit == None:
                        break
                    else:
                        my_int = my_int * 10 + my_digit
                        if (my_sign == -1 and my_int > INT_MAX) or (my_sign == 1 and my_int >= INT_MAX):
                            if my_sign == -1:
                                my_int = INT_MAX + 1
                            else:
                                my_int = INT_MAX
                            break
                skip_space = False

        return my_sign * my_int
