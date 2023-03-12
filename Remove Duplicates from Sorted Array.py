class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # v2

        print(nums)

        p1 = 1
        p2 = 1

        while p1 < len(nums):

            if nums[p1 - 1] == nums[p1]:
                p1 += 1

            else:
                nums[p2] = nums[p1]
                p1 += 1
                p2 += 1

        return p2





nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(0, nums))