class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # solution without hash table
        # for i in ransomNote:
        #     if i in magazine:
        #         magazine = magazine.replace(i, '-', 1)
        #         print(magazine)
        #     else:
        #         return False
        # return True

        # solution with hash table
        table = {}
        for i in magazine:
            table[i] = table.get(i, 0) + 1

        for i in ransomNote:
            if i in table and table[i] > 0:
                table[i] -= 1
            else:
                return False
        return True

ransomNote = "aa"
magazine = "aab"

print(Solution.canConstruct(0, ransomNote, magazine))