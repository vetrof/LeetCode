
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        l = len(arr)

        while i < l:

            if arr[i] == 0:
                arr.pop(l - 1)
                arr.insert(i, 0)
                i += 2
                continue

            i += 1

        return arr

print(Solution.duplicateZeros(0, [1,0,2,3,0,4,5,0]))