# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # version 1
        # l = len(nums)
        # while True:
        #     try:
        #         nums.remove(val)
        #         l -= 1
        #     except ValueError:
        #         break
        # return l

        # version2
        # n = len(nums)
        # while True:
        #     if val in nums:
        #
        #         n -= 1
        #         index = nums.index(val)
        #         for i in range(index + 1, len(nums)):
        #             nums[i - 1] = nums[i]
        #         nums[-1:] = '_'
        #
        #     else:
        #         break
        # return n

        # version3
        n = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[n] = nums[i]
                n += 1

        return n

















nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(Solution.removeElement(0, nums, val))