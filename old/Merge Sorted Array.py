# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Import time module
import time

# record start time
start = time.time()

class Solution(object):
    def merge(self, nums1, m, nums2, n):

        # version1
        num1_copy = nums1[:]

        # p1 = 0
        # p2 = 0
        # i = -1
        #
        # for _ in range(m + n):
        #     i += 1
        #
        #     if p1 > m - 1:
        #         nums1[i] = nums2[p2]
        #         p2 += 1
        #         continue
        #
        #     if p2 > n - 1:
        #         nums1[i] = num1_copy[p1]
        #         p1 += 1
        #         continue
        #
        #     if num1_copy[p1] < nums2[p2]:
        #         nums1[i] = num1_copy[p1]
        #         p1 += 1
        #
        #     else:
        #         nums1[i] = nums2[p2]
        #         p2 += 1
        #
        # return nums1

# #         version2
        index = m
        for i in nums2:
            nums1[index] = i
            index += 1

        nums1.sort()
        return nums1


        # version3
        # for i in range(len(nums1) - m):
        #     nums1.remove(0)
        # nums1.extend(nums2)
        # nums1.sort()
        # return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(Solution.merge(0, nums1, m, nums2, n))

# record end time
end = time.time()
print("The time of execution of above program is :",
	(end-start) * 10**3, "ms")