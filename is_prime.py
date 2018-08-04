def is_prime(self, x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0 or x % 3 == 0:
        return True
    else:
        upper_bound = int(math.sqrt(x)) + 1
        k = 1
        m = 5
        while m < upper_bound:
            if x % m == 0 or x % (m + 2) == 0:
                return False
            k = k + 1
            m = 6 * k - 1

    return True