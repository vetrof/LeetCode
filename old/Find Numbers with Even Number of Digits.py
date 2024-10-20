class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                n += 1
        return n