
def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 0
    max_list = []

    for i in range(len(nums)):

        if nums[i] == 1:
            n += 1

        else:
            n = 0

        max_list.append(n)


    max = 0
    for i in max_list:
        if i > max:
            max =  i

    return max





print(findMaxConsecutiveOnes(0, nums = [1,1,0,1,1,1]))