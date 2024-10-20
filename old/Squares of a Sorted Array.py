class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            nums[i] **= 2
        return sorted(nums)



nums = [-7,-3,2,3,11]

print(Solution.sortedSquares(0, nums))