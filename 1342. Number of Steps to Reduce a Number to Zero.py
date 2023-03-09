
def numberOfSteps(self, num):
    """
    :type num: int
    :rtype: int
    """

    n = 0

    while num > 0:
        n += 1

        if not num % 2:
            num /= 2
            continue

        else:
            num -= 1

    return n

print(numberOfSteps(0, 123))